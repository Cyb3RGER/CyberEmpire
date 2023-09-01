import os
import random
import shutil
import traceback
from statistics import mean

from cards import CardHelper
from compress import compress
from decks import Deck, DeckData
from extract import extract
from gen_card_props import CardProps
from mappers import *
from packs import PackDefData, Pack
from settings import RandomizerSettings, RandomDeckSettings, RandomShopPackSettings
from utils import prog_name, delete_folder

# from deck_data import *

seed_digits = 20
extract_path = 'extracted'
compress_path = 'to_compress'
out_path = 'out'
placement_path = 'placement'
custom_decks_path = 'custom_decks'

start_decks = [
    'initialdeck_1classic.ydc',
    'initialdeck_2gx.ydc',
    'initialdeck_3_5ds.ydc',
    'initialdeck_4zexal.ydc',
    'initialdeck_5arcv.ydc',
]


class Randomizer:
    CONFIG_PATH: str = "config.json"

    def __init__(self):

        self.pack_data: PackDefData | None = None
        self.deck_data: DeckData | None = None
        self.card_helper: CardHelper | None = None
        self.card_props: list[CardProps] = []
        self.random_decks: dict[str, Deck] = {}
        self.random_shop_packs: dict[str, Pack] = {}

        self.randomized_sig_cards: list[(str, str, str)] = []
        self.shuffled_arena_files: dict[str, str] = {}
        self.shuffled_deck_files: dict[str, str] = {}
        self.custom_decks: list[str] = []
        self.shuffled_shop_portraits: dict[str, str] = {}
        self.shuffled_shop_packs: dict[str, str] = {}
        # ToDo setup from config; config: yaml or json?
        self.settings: RandomizerSettings = RandomizerSettings()
        self.dry: bool = False
        self.force_extract: bool = False
        self.placement_folder: str = ""
        self.no_gui: bool = False
        self.seed: str | None = None
        self.random: random.Random = random.Random(self.seed)

        print(prog_name)

    def game_path_is_valid(self, val) -> bool:
        return val is not None and os.path.exists(val) and os.path.exists(f'{val}/YGO_2020.dat') and os.path.exists(
            f'{val}/YGO_2020.toc')

    def setup_from_args(self, args, check_valid=False):
        self.force_extract = args.force_extract
        self.no_gui = args.no_gui
        self.seed = args.seed
        self.placement_folder = args.placement_folder
        self.dry = args.dry
        self.settings = RandomizerSettings.load(args.settings_path)
        self.copy_game_files(args.game_path)
        if check_valid and not self.game_path_is_valid(args.game_path):
            raise "Invalid game_path"

    def run(self):
        step = 0
        max_step = 3
        try:
            yield ++step, "setting up randomizer...", max_step
            self.card_helper = CardHelper(self.settings)
            self.setup_seed()
            print(self.seed, self.settings)
            self.setup_game_files()
            self.get_custom_decks_file_list()
            # ToDo: self.write_default_placement_files()
            if self.placement_folder:
                yield ++step, "applying placement file(s)...", max_step
                # ToDo
                self.apply_placement()
            else:
                yield ++step, "randomizing...", 3
                gen = self.randomize()
                for i in gen:
                    if i[0] == -1:
                        yield i
                    else:
                        yield 1, "randomizing...", max_step, *i
            yield ++step, "writing output...", max_step
            self.output_result()
            # ToDo? self.copy_to_game_path()
            self.cleanup()
            yield ++step, "done...", max_step
        except Exception as e:
            yield -1, e, traceback.format_exc()

    def setup_seed(self):
        if self.seed is not None:
            seed = self.seed
        else:
            random.seed(None)
            seed = str(random.randint(0, pow(10, seed_digits) - 1))
            self.seed = seed
        self.random = random.Random(seed)

    def setup_game_files(self):
        if not os.path.exists(extract_path) or self.force_extract:
            extract(f'YGO_2020', extract_path)
        if os.path.exists(compress_path):
            delete_folder(compress_path, False)
        if not os.path.exists(compress_path) and not self.dry:
            os.mkdir(compress_path)

    def write_default_placement_files(self):
        deck_list = self.get_deck_file_list()
        with open(f'{placement_path}/vanilla/deck_data.txt', mode='w') as f:
            for v in deck_list:
                f.write(f'{v},{v}\n')

    def apply_placement(self):
        self.apply_deck_placement()

    def apply_deck_placement(self):
        with open(f'{placement_path}/{self.placement_folder}/deck_data.txt', mode='r') as f:
            self.shuffled_deck_files = {a.strip(): b.strip() for a, b in (v.split(',') for v in f.readlines())}

    def randomize(self):
        step = 0
        max_step = 6
        try:
            yield ++step, "randomizing deck_data...", max_step
            if self.settings.random_decks == RandomDeckSettings.Off:
                pass
            elif self.settings.random_decks == RandomDeckSettings.Balanced:
                self.randomize_decks()
            elif self.settings.random_decks == RandomDeckSettings.Shuffled:
                self.shuffle_decks()
            elif self.settings.random_decks == RandomDeckSettings.Full_Random:
                self.randomize_decks()
            elif self.settings.random_decks == RandomDeckSettings.By_Type:
                # ToDo
                pass
            elif self.settings.random_decks == RandomDeckSettings.Archtype:
                # ToDo
                pass
            yield ++step, "shuffling arenas...", max_step
            if self.settings.shuffle_arenas:
                self.shuffle_arenas()
            yield ++step, "randomizing shop packs...", max_step
            if self.settings.random_shop_packs == RandomShopPackSettings.Shuffled:
                self.shuffle_shop_packs()
            elif self.settings.random_shop_packs == RandomShopPackSettings.Randomized:
                self.randomize_shop_packs()
            yield ++step, "randomizing shop portraits...", max_step
            if self.settings.shuffle_shop_portraits:
                self.shuffle_shop_portraits()
            yield ++step, "randomizing shop prices...", max_step
            if self.settings.random_shop_prices:
                self.randomize_shop_prices()
            yield ++step, "randomizing signature cards...", max_step
            if self.settings.random_sig_cards:
                self.randomize_sig_cards()
        except Exception as e:
            yield -1, e, traceback.format_exc()

    def shuffle_decks(self):
        deck_files = self.get_deck_file_list()
        self.shuffled_deck_files = self.shuffle_file_list(deck_files, self.settings.include_custom_decks)

    def shuffle_arenas(self):
        arena_files = self.get_arena_file_list()
        self.shuffled_arena_files = self.shuffle_file_list(arena_files)

    def shuffle_file_list(self, file_list: list[str], include_custom_decks: bool = False) -> dict[str, str]:
        shuffled_list = file_list.copy()
        if include_custom_decks:
            shuffled_list += self.custom_decks
        self.random.shuffle(shuffled_list)
        return {x: shuffled_list[i] for i, x in enumerate(file_list)}

    def apply_random_deck_files(self, files):
        dst_folder = f'{compress_path}/decks.zib'
        if not os.path.exists(dst_folder):
            os.mkdir(dst_folder)
        for k, v in files.items():
            dst = f'{dst_folder}/{k}'
            deck = self.random_decks[v]
            print(f'writing {dst}')
            deck.write(dst)


    def apply_shuffled_files(self, subdir, shuffled_files):
        src_folder = f'{extract_path}/{subdir}'
        src_folder_custom = f'{custom_decks_path}'
        dst_folder = f'{compress_path}/{subdir}'
        if not os.path.exists(dst_folder):
            os.mkdir(dst_folder)
        for k, v in shuffled_files.items():
            src = f'{src_folder_custom if self.is_custom_deck(v) else src_folder}/{v}'
            dst = f'{dst_folder}/{k}'
            print(f'{src} -> {dst}')
            shutil.copyfile(src, dst)

    def get_out_path(self):
        return f'{out_path}/{self.seed}/'

    def output_result(self):
        # copy_extracted()
        if not os.path.exists(out_path):
            os.mkdir(out_path)
        if not os.path.exists(self.get_out_path()):
            os.mkdir(self.get_out_path())
        if not self.dry:
            # deck
            if self.settings.random_decks == RandomDeckSettings.Off:
                pass
            elif self.settings.random_decks == RandomDeckSettings.Shuffled:
                self.apply_shuffled_files('deck_data.zib', self.shuffled_deck_files)
            elif self.settings.random_decks in [RandomDeckSettings.Balanced, RandomDeckSettings.Full_Random,
                                                RandomDeckSettings.By_Type]:
                self.apply_random_deck_files(self.shuffled_deck_files)
            elif self.settings.random_decks == RandomDeckSettings.Archtype:
                # ToDo
                pass
            # arenas
            if self.settings.shuffle_arenas:
                self.apply_shuffled_files('arenas', self.shuffled_arena_files)
            # shops
            if self.settings.random_shop_packs == RandomShopPackSettings.Off:
                pass
            elif self.settings.random_shop_packs == RandomShopPackSettings.Shuffled:
                self.apply_shuffled_files('packs.zib', self.shuffled_shop_packs)
            elif self.settings.random_shop_packs == RandomShopPackSettings.Randomized:
                pass
            if self.settings.shuffle_shop_portraits:
                self.apply_shuffled_files('packs', self.shuffled_shop_portraits)
            if self.settings.random_shop_prices:
                self.pack_data.write(f'{compress_path}')
            # duelists
            if self.settings.random_sig_cards:
                self.deck_data.write(f'{compress_path}')
            compress(f'{compress_path}', f'{self.get_out_path()}/YGO_2020', f'YGO_2020')
        self.write_log()

    def write_log(self):
        with open(f'{self.get_out_path()}/log.txt', mode='w', encoding='utf-8') as f:
            f.write(f'seed: {self.seed}\n')
            f.write(f'settings: {self.settings.__str__()}\n')
            # decks
            if self.settings.random_decks != RandomDeckSettings.Off:
                f.write('-' * 16 + '\n')
                f.write(f'deck_data:\n')
                f.write('-' * 16 + '\n')
                for k, v in self.shuffled_deck_files.items():
                    f.write(f'{k} -> {v}\n')
            # arenas
            if self.settings.shuffle_arenas:
                f.write('-' * 16 + '\n')
                f.write(f'arenas:\n')
                f.write('-' * 16 + '\n')
                for k, v in self.shuffled_arena_files.items():
                    f.write(f'{k} -> {v}\n')
            # shops
            # ToDo: shop stuff...
            if self.settings.random_shop_prices != RandomShopPackSettings.Off:
                f.write('-' * 16 + '\n')
                f.write(f'shop packs:\n')
                f.write('-' * 16 + '\n')
                for k, v in self.shuffled_shop_packs.items():
                    f.write(f'{k} -> {v}\n')
            if self.settings.shuffle_shop_portraits:
                f.write('-' * 16 + '\n')
                f.write(f'shop portraits:\n')
                f.write('-' * 16 + '\n')
                for k, v in self.shuffled_shop_portraits.items():
                    f.write(f'{k} -> {v}\n')
            if self.settings.random_shop_prices:
                f.write('-' * 16 + '\n')
                f.write(f'shop prices:\n')
                f.write('-' * 16 + '\n')
                for pack_def in self.pack_data.pack_defs:
                    f.write(f'{pack_def.name}: {pack_def.price}\n')
            # duelists
            if self.settings.random_sig_cards:
                f.write('-' * 16 + '\n')
                f.write(f'sig cards:\n')
                f.write('-' * 16 + '\n')
                for a, b, c in self.randomized_sig_cards:
                    f.write(f'{a}: {b} -> {c}\n')

    def create_random_deck(self, i: int):
        deck = Deck(f'random_deck_{i}.ydc')
        # ToDo: Balancing ratios from settings
        deck.main_count = self.random.randint(40, 60)
        deck.extra_count = 0
        deck.side_count = 0
        if self.settings.random_decks == RandomDeckSettings.Full_Random:
            deck.extra_count = self.random.randint(0, 15)
            deck.side_count = self.random.randint(0, 15)
            deck.main_ids = [v.id_ for v in self.card_helper.get_random_cards(self.random, k=deck.main_count)]
            deck.extra_ids = [v.id_ for v in self.card_helper.get_random_cards(self.random, k=deck.extra_count)]
            deck.side_ids = [v.id_ for v in self.card_helper.get_random_cards(self.random, k=deck.side_count)]
        else:
            mon_count = round(deck.main_count * .5)
            spell_count = deck.main_count - mon_count
            type_ = None
            if self.settings.random_decks == RandomDeckSettings.By_Type:
                type_ = self.random.randint(0, 24)
            normal_mons = self.card_helper.get_normal_and_effect_monsters(self.random, mon_count, type_)
            spell_traps = self.card_helper.get_spell_and_trap_cards(self.random, spell_count)
            deck.main_ids = [v.id_ for v in normal_mons] + [v.id_ for v in spell_traps]
        return deck

    def get_custom_decks_file_list(self):
        self.custom_decks = []
        if not os.path.exists(custom_decks_path):
            os.mkdir(custom_decks_path)
            return
        for entry in os.scandir(custom_decks_path):
            if entry.is_file() and entry.name.endswith('.ydc'):
                self.custom_decks.append(entry.name)

    def is_custom_deck(self, name):
        return name in self.custom_decks

    def randomize_sig_cards(self):
        self.deck_data = DeckData(f'{extract_path}')
        for i in range(0, self.deck_data.deck_count):
            deck = self.deck_data.decks[i]
            og_card = card_name_mapper.get_name(deck.sig_card_id)
            # ToDo: pick card from deck (maybe as additional setting)
            deck.sig_card_id = self.card_helper.get_random_card(self.random).id_
            self.randomized_sig_cards.append(
                (deck.deck_name, og_card, card_name_mapper.get_name(deck.sig_card_id)))

    def get_deck_file_list(self) -> list[str]:
        result: list[str] = []
        if self.settings.only_starter_decks:
            return start_decks
        for entry in os.scandir(f"{extract_path}/deck_data.zib/"):
            if entry.name.endswith('.ydc'):
                result.append(entry.name)
        return result

    def randomize_decks(self):
        deck_files = self.get_deck_file_list()
        for i, v in enumerate(deck_files):
            deck = self.create_random_deck(i)
            self.random_decks[deck.name] = deck
            self.shuffled_deck_files[v] = deck.name

    def copy_game_files(self, game_path):
        if not self.game_path_is_valid(game_path):
            return
        shutil.copyfile(f'{game_path}/YGO_2020.dat', f'YGO_2020.dat')
        shutil.copyfile(f'{game_path}/YGO_2020.toc', f'YGO_2020.toc')

    def has_game_files(self):
        # ToDo: checksum?
        return os.path.isfile(f'YGO_2020.dat') and os.path.isfile(f'YGO_2020.dat')

    def get_arena_file_list(self):
        result: list[str] = []
        for entry in os.scandir(f"{extract_path}/arenas/"):
            if entry.is_file() and entry.name.endswith('.jpg'):
                result.append(entry.name)
        return result

    def cleanup(self):
        # delete_folder(compress_path)
        pass

    # def copy_to_game_path(self):
    #     #backup game files
    #     if not os.path.exists(f'{self.game_path}/backup'):
    #         os.mkdir(f'{self.game_path}/backup')
    #     shutil.copyfile(f'{self.game_path}/YGO_2020.dat',
    #                     f'{self.game_path}/backup/{datetime.datetime.now():%d_%m_%Y_%H_%M_%S}_YGO_2020.dat')
    #     shutil.copyfile(f'{self.game_path}/YGO_2020.toc',
    #                     f'{self.game_path}/backup/{datetime.datetime.now():%d_%m_%Y_%H_%M_%S}_YGO_2020.toc')
    #     shutil.copyfile(f'{self.get_out_path()}/YGO_2020.dat',f'{self.game_path}/YGO_2020.dat')
    #     shutil.copyfile(f'{self.get_out_path()}/YGO_2020.toc',f'{self.game_path}/YGO_2020.toc')

    def shuffle_shop_portraits(self):
        shop_portraits = self.get_shop_portraits_file_list()
        self.shuffled_shop_portraits = self.shuffle_file_list(shop_portraits)

    def randomize_shop_prices(self):
        if self.pack_data is None:
            self.pack_data = PackDefData(f'{extract_path}')
        for pack_def in self.pack_data.pack_defs:
            pack_def.price = round(self.random.randint(self.settings.shop_min_price, self.settings.shop_max_price), -1)

    def shuffle_shop_packs(self):
        shop_packs = self.get_shop_pack_file_list()
        self.shuffled_shop_packs = self.shuffle_file_list(shop_packs)

    def randomize_shop_packs(self):
        shop_pack_files = self.get_shop_pack_file_list()
        packs = []
        for i, v in enumerate(shop_pack_files):
            pack = Pack(v)
            pack.load(f'{extract_path}/packs.zib/{v}')
            packs.append(pack)
            pack = self.create_random_shop_pack(i)
            self.random_shop_packs[pack.name] = pack
            self.shuffled_deck_files[v] = pack.name
        sum_list = [v.common_count+v.rare_count for v in packs]
        common_list = [v.common_count for v in packs]
        rare_list = [v.rare_count for v in packs]
        def print_list_info(l, n):
            print(n, sum(l) / len(l), mean(l), min(l),max(l))
        print_list_info(sum_list, "sum")
        print_list_info(common_list, "common")
        print_list_info(rare_list, "rare")

    def get_shop_portraits_file_list(self):
        result: list[str] = []
        # ToDo: implement
        # ToDo: prolly should implement duelist portrait rando first as that might clash with this feature
        # this is wrong. these are just reward images
        # for entry in os.scandir(f"{extract_path}/packs/"):
        #     if entry.name.endswith('.png'):
        #         result.append(entry.name)
        return result

    def get_shop_pack_file_list(self):
        result: list[str] = []
        for entry in os.scandir(f"{extract_path}/packs.zib/"):
            if entry.name.startswith('packdata') and entry.name.endswith('.bin'):
                result.append(entry.name)
        return result

    def create_random_shop_pack(self, i: int):
        pack = Pack(f'random_pack_{i}.bin')
        # ToDo: Balancing ratios from settings
        pack.common_count = self.random.randint(200, 300)
        pack.rare_count = self.random.randint(50, 100)
        for i in range(0, pack.common_count):
            pack.common_ids += self.card_helper.get_random_cards(self.random, k=pack.common_count)
        return pack
