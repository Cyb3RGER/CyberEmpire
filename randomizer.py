import os
import random
import shutil
import traceback
from statistics import mean
from typing import Optional

from cards import CardHelper
from custom_decks import CustomDeckParser, ParseException, CustomDeck
from dfymoo import Dfymoo
from compress import compress
from decks import Deck, DeckData
from extract import extract
from gen_card_props import CardProps
from mappers import *
from packs import PackDefData, Pack
from seed_word_tbl import word_tbl
from settings import RandomizerSettings, RandomDeckSettings, RandomShopPackSettings, RandomBattlePacksSettings, \
    RandomDuelistPortraitSettings
from utils import prog_name, delete_folder

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
        self.pack_wrappers_dfymoo: Dfymoo | None = None
        self.char_dfymoo: Dfymoo | None = None
        self.pack_data: PackDefData | None = None
        self.deck_data: DeckData | None = None
        self.card_helper: CardHelper | None = None
        self.card_props: list[CardProps] = []
        self.decks: dict[str, Deck] = {}
        self.random_shop_packs: dict[str, Pack] = {}

        self.randomized_sig_cards: list[(str, str, str)] = []
        self.shuffled_arena_files: dict[str, str] = {}
        self.shuffled_deck_files: dict[str, str] = {}
        self.custom_decks: list[CustomDeck] = []
        self.broken_custom_decks: list[str] = []
        self.shuffled_shop_portraits: dict[str, str] = {}
        self.shuffled_pack_reward_images: dict[str, str] = {}
        self.shuffled_shop_packs: dict[str, str] = {}
        self.shuffled_battle_packs: dict[str, str] = {}
        self.shuffled_bust_files: dict[str, str] = {}
        self.shuffled_dialog_files: dict[str, str] = {}
        self.shuffled_combat_portrait_names: dict[str, str] = {}
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
            yield step, "setting up randomizer...", max_step
            step += 1
            self.card_helper = CardHelper(self.settings)
            self.setup_seed()
            print(self.seed, self.settings)
            self.setup_game_files()
            self.get_custom_decks()
            # ToDo: self.write_default_placement_files()
            if self.placement_folder:
                yield step, "applying placement file(s)...", max_step
                step += 1
                # ToDo
                self.apply_placement()
            else:
                yield step, "randomizing...", 3
                step += 1
                gen = self.randomize()
                for i in gen:
                    if i[0] == -1:
                        yield i
                    else:
                        yield 1, "randomizing...", max_step, *i
            yield step, "writing output...", max_step
            step += 1
            self.output_result()
            # ToDo? self.copy_to_game_path()
            self.cleanup()
            yield step, "done...", max_step
        except Exception as e:
            yield -1, e, traceback.format_exc()

    def setup_seed(self):
        if self.seed is not None:
            seed = self.seed
        else:
            random.seed(None)
            if word_tbl is None or len(word_tbl) == 0:
                seed = str(random.randint(0, pow(10, seed_digits) - 1))
                self.seed = seed
            else:
                seed = ''.join(random.choices(word_tbl, k=3))
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
        deck_list = self.get_deck_file_list(False)
        with open(f'{placement_path}/vanilla/decks.txt', mode='w') as f:
            for v in deck_list:
                f.write(f'{v},{v}\n')

    def apply_placement(self):
        self.apply_deck_placement()

    def apply_deck_placement(self):
        with open(f'{placement_path}/{self.placement_folder}/decks.txt', mode='r') as f:
            self.shuffled_deck_files = {a.strip(): b.strip() for a, b in (v.split(',') for v in f.readlines())}

    def randomize(self):
        step = 0
        max_step = 7
        try:
            yield step, "randomizing decks...", max_step
            step += 1
            if self.settings.random_decks == RandomDeckSettings.Off:
                pass
            elif self.settings.random_decks in [RandomDeckSettings.Balanced, RandomDeckSettings.Full_Random,
                                                RandomDeckSettings.By_Type]:
                self.randomize_decks()
            elif self.settings.random_decks == RandomDeckSettings.Shuffled:
                self.shuffle_decks()
            elif self.settings.random_decks == RandomDeckSettings.Archetype:
                # ToDo
                pass
            yield step, "randomizing arenas...", max_step
            step += 1
            if self.settings.shuffle_arenas:
                self.shuffle_arenas()
            yield step, "randomizing shop packs...", max_step
            step += 1
            if self.settings.random_shop_packs == RandomShopPackSettings.Off and self.settings.random_battle_packs != RandomBattlePacksSettings.Off:
                # we need to make sure shop packs are also in the compress folder, if they are not random,
                # when we change packs.zib content, otherwise the compress script will not repack them
                self.set_default_shop_packs()
            if self.settings.random_shop_packs == RandomShopPackSettings.Shuffled:
                self.shuffle_shop_packs()
            elif self.settings.random_shop_packs == RandomShopPackSettings.Randomized:
                self.randomize_shop_packs()
            yield step, "randomizing shop portraits...", max_step
            step += 1
            if self.settings.shuffle_shop_portraits:
                self.shuffle_shop_portraits()
            yield step, "randomizing shop prices...", max_step
            step += 1
            if self.settings.random_shop_prices:
                self.randomize_shop_prices()
            yield step, "randomizing signature cards...", max_step
            step += 1
            if self.settings.random_sig_cards:
                self.randomize_sig_cards()
            yield step, "randomizing portraits...", max_step
            step += 1
            if self.settings.random_duelist_portraits != RandomDuelistPortraitSettings.Off:
                self.shuffle_duelists_portraits()
            yield step, "randomizing battle packs...", max_step
            step += 1
            if self.settings.random_battle_packs == RandomBattlePacksSettings.Off and self.settings.random_shop_packs != RandomShopPackSettings.Off:
                # we need to make sure battle packs are also in the compress folder, if they are not random,
                # when we change packs.zib content, otherwise the compress script will not repack them
                self.set_default_battle_packs()
        except Exception as e:
            yield -1, e, traceback.format_exc()

    def shuffle_decks(self):
        deck_files = self.get_deck_file_list(self.settings.only_starter_decks)
        custom_deck_list: list[CustomDeck] = self.custom_decks.copy()
        if self.settings.random_custom_decks:
            custom_deck_list = random.sample(self.custom_decks,
                                             k=self.random.randint(0, min(len(self.custom_decks), len(deck_files))))
        for v in custom_deck_list:
            deck = self.card_helper.get_deck_from_custom_deck(v, self.random)
            self.decks[deck.name] = deck
        self.shuffled_deck_files = self.shuffle_list(deck_files, [f'custom_{v.name}' for v in custom_deck_list],
                                                     not self.settings.random_custom_decks)
        if self.settings.only_starter_decks:
            temp = set(deck_files)
            deck_files = self.get_deck_file_list(False)
            temp = set(deck_files) - temp
            for v in temp:
                self.shuffled_deck_files[v] = v

    def shuffle_arenas(self):
        arena_files = self.get_arena_file_list()
        self.shuffled_arena_files = self.shuffle_list(arena_files)

    def shuffle_list(self, list_: list[str], include_extra: list[str] = None, extra_first: bool = True) -> dict[
        str, str]:
        shuffled_list = list_.copy()
        if include_extra is not None:
            if extra_first:
                k = max(0, len(list_) - len(include_extra))
                shuffled_list = self.random.sample(list_, k=k)
                shuffled_list += include_extra
            else:
                shuffled_list += include_extra
        self.random.shuffle(shuffled_list)
        return {x: shuffled_list[i] for i, x in enumerate(list_)}

    def apply_deck_files(self, files: dict[str, str]):
        src_folder = f'{extract_path}/decks.zib'
        dst_folder = f'{compress_path}/decks.zib'
        if not os.path.exists(dst_folder):
            os.mkdir(dst_folder)
        for k, v in files.items():
            dst = f'{dst_folder}/{k}'
            if v not in self.decks:
                src = f'{src_folder}/{v}'
                print(f'{src} -> {dst}')
                shutil.copyfile(src, dst)
            else:
                deck = self.decks[v]
                print(f'writing {dst}')
                deck.write(dst)

    def apply_shuffled_files(self, subdir, shuffled_files: dict[str, str]):
        src_folder = f'{extract_path}/{subdir}'
        dst_folder = f'{compress_path}/{subdir}'
        if not os.path.exists(dst_folder):
            os.makedirs(dst_folder, exist_ok=True)
        for k, v in shuffled_files.items():
            dst = f'{dst_folder}/{k}'
            src = f'{src_folder}/{v}'
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
                self.apply_deck_files(self.shuffled_deck_files)
            elif self.settings.random_decks in [RandomDeckSettings.Balanced, RandomDeckSettings.Full_Random,
                                                RandomDeckSettings.By_Type]:
                self.apply_deck_files(self.shuffled_deck_files)
            elif self.settings.random_decks == RandomDeckSettings.Archetype:
                # ToDo
                pass
            # arenas
            if self.settings.shuffle_arenas:
                self.apply_shuffled_files('arenas', self.shuffled_arena_files)
            # shops
            if self.settings.random_shop_packs == RandomShopPackSettings.Off and self.settings.random_battle_packs != RandomBattlePacksSettings.Off:
                self.apply_shuffled_files('packs.zib', self.shuffled_shop_packs)
            elif self.settings.random_shop_packs == RandomShopPackSettings.Shuffled:
                self.apply_shuffled_files('packs.zib', self.shuffled_shop_packs)
            elif self.settings.random_shop_packs == RandomShopPackSettings.Randomized:
                self.apply_random_shop_pack_files(self.shuffled_shop_packs)
            if self.settings.shuffle_shop_portraits:
                self.pack_wrappers_dfymoo.write(f'{compress_path}/pdui/PackWrappers.dfymoo')
                self.apply_shuffled_files('packs', self.shuffled_pack_reward_images)
            if self.settings.random_shop_prices:
                self.pack_data.write(f'{compress_path}')
            # duelists
            if self.settings.random_sig_cards:
                self.deck_data.write(f'{compress_path}')
            if self.settings.random_duelist_portraits != RandomDuelistPortraitSettings.Off:
                self.apply_shuffled_files('busts.zib', self.shuffled_bust_files)
                self.apply_shuffled_files('pdui/dialog_chars', self.shuffled_dialog_files)
                self.char_dfymoo.write(f'{compress_path}/pdui/chars.dfymoo')
            if self.settings.random_battle_packs == RandomBattlePacksSettings.Off and self.settings.random_shop_packs != RandomShopPackSettings.Off:
                self.apply_shuffled_files('packs.zib', self.shuffled_battle_packs)
            # finally we compress the files together for the game to use
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
            mon_count = round(deck.main_count * self.settings.mon_percent / 100)
            spell_trap_count = deck.main_count - mon_count
            type_ = None
            if self.settings.random_decks == RandomDeckSettings.By_Type:
                type_ = self.random.randint(1, 23)
            normal_mons = self.get_normal_and_effect_monsters(self.random, mon_count, type_)
            spell_traps = self.get_spell_and_trap_cards(self.random, spell_trap_count)
            deck.main_ids = [v.id_ for v in normal_mons] + [v.id_ for v in spell_traps]
        return deck

    def get_normal_and_effect_monsters(self, random: random.Random, k=1, type_: Optional[int] = None) -> list[
        CardProps]:
        low_level_count = round(k * self.settings.low_level_percent / 100)
        high_level_count = k - low_level_count
        monster_cards = [v for v in self.card_helper.get_included_cards(type_) if
                         v.effect in self.card_helper.get_normal_and_effect_monsters_effects()]
        low_level_cards = [v for v in monster_cards if v.stars <= 4]
        high_level_cards = [v for v in monster_cards if v.stars > 4]
        assert len(monster_cards) > 0, f"not enough mon cards for {type_}"
        assert len(low_level_cards) > 0, f"not enough low mon cards for {type_}"
        assert len(high_level_cards) > 0, f"not enough high mon cards for {type_}"
        cards = (self.card_helper.get_random_cards(random, low_level_cards, k=low_level_count) +
                 self.card_helper.get_random_cards(random, high_level_cards, k=high_level_count))
        return cards

    def get_spell_and_trap_cards(self, random: random.Random, k=1) -> list[CardProps]:
        spell_count = round(k * self.settings.spell_percent / 100)
        trap_count = k - spell_count
        included_cards = self.card_helper.get_included_cards()
        spell_cards = [v for v in included_cards if v.attribute == 8]
        trap_cards = [v for v in included_cards if v.attribute == 9]
        return random.choices(spell_cards, k=spell_count) + random.choices(trap_cards, k=trap_count)

    def get_custom_decks(self):
        parser = CustomDeckParser()
        self.custom_decks = []
        self.broken_custom_decks = []
        if not os.path.exists(custom_decks_path):
            os.mkdir(custom_decks_path)
            return
        for entry in os.scandir(custom_decks_path):
            if entry.is_file() and entry.name.endswith('.txt'):
                try:
                    deck = parser.load(entry)
                except ParseException:
                    self.broken_custom_decks.append(entry)
                    continue
                self.custom_decks.append(deck)

    def is_custom_deck(self, v):
        return isinstance(v, Deck)

    def randomize_sig_cards(self):
        self.deck_data = DeckData(f'{extract_path}')
        for i in range(0, self.deck_data.deck_count):
            deck = self.deck_data.decks[i]
            og_card = card_name_mapper.get_name(deck.sig_card_id)
            # ToDo: pick card from deck (maybe as additional setting)
            deck.sig_card_id = self.card_helper.get_random_card(self.random).id_
            self.randomized_sig_cards.append(
                (deck.deck_name, og_card, card_name_mapper.get_name(deck.sig_card_id)))

    def get_deck_file_list(self, only_starter_decks: bool) -> list[str]:
        result: list[str] = []
        if only_starter_decks:
            return start_decks
        for entry in os.scandir(f"{extract_path}/decks.zib/"):
            if entry.name.endswith('.ydc'):
                result.append(entry.name)
        return result

    def randomize_decks(self):
        custom_deck_list: list[CustomDeck] = self.custom_decks.copy()
        deck_files = self.get_deck_file_list(self.settings.only_starter_decks)
        if self.settings.random_custom_decks:
            custom_deck_list = random.sample(self.custom_decks,
                                             k=self.random.randint(0, min(len(self.custom_decks), len(deck_files))))
        custom_deck_placements = enumerate(
            self.random.sample(deck_files, k=min(len(deck_files), len(custom_deck_list))))
        custom_deck_placements = {k: custom_deck_list[i] for i, k in custom_deck_placements}
        for i, v in enumerate(deck_files):
            if v in custom_deck_placements:
                deck = self.card_helper.get_deck_from_custom_deck(custom_deck_placements[v], self.random)
                self.decks[deck.name] = deck
                self.shuffled_deck_files[v] = deck.name
            else:
                deck = self.create_random_deck(i)
                self.decks[deck.name] = deck
                self.shuffled_deck_files[v] = deck.name
        if self.settings.only_starter_decks:
            temp = set(deck_files)
            deck_files = self.get_deck_file_list(False)
            temp = set(deck_files) - temp
            for v in temp:
                self.shuffled_deck_files[v] = v

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
        self.pack_wrappers_dfymoo = Dfymoo()
        self.pack_wrappers_dfymoo.load(f'{extract_path}/pdui/PackWrappers.dfymoo')
        shop_portraits = [v for v in self.pack_wrappers_dfymoo.get_names() if
                          'battlepack' not in v and v != 'wrap_locked']
        self.shuffled_shop_portraits = self.shuffle_list(shop_portraits)
        for v in self.pack_wrappers_dfymoo.vals:
            image_name_og = self.convert_wrapper_name_to_reward_image(v.n)
            if v.n in self.shuffled_shop_portraits:
                v.n = self.shuffled_shop_portraits[v.n]
            if 'wrap_locked' in image_name_og:
                continue
            image_name_new = self.convert_wrapper_name_to_reward_image(v.n)
            self.shuffled_pack_reward_images[image_name_og] = image_name_new

    def convert_wrapper_name_to_reward_image(self, wrapper_name):
        return f'reward_{wrapper_name}.png'

    def get_pack_reward_images(self):
        result: list[str] = []
        for entry in os.scandir(f"{extract_path}/packs/"):
            if entry.name.endswith('.png'):
                result.append(entry.name)
        return result

    def randomize_shop_prices(self):
        if self.pack_data is None:
            self.pack_data = PackDefData(f'{extract_path}')
        for pack_def in self.pack_data.pack_defs:
            pack_def.price = round(self.random.randint(self.settings.shop_min_price, self.settings.shop_max_price), -1)

    def shuffle_shop_packs(self):
        shop_packs = self.get_shop_pack_file_list()
        self.shuffled_shop_packs = self.shuffle_list(shop_packs)

    def randomize_shop_packs(self):
        shop_pack_files = self.get_shop_pack_file_list()
        for i, v in enumerate(shop_pack_files):
            pack = self.create_random_shop_pack(i)
            self.random_shop_packs[pack.name] = pack
            self.shuffled_shop_packs[v] = pack.name

    def get_battle_pack_file_list(self):
        result: list[str] = []
        for entry in os.scandir(f"{extract_path}/packs.zib/"):
            if entry.name.startswith('bpack') and entry.name.endswith('.bin'):
                result.append(entry.name)
        return result

    def get_shop_pack_file_list(self):
        result: list[str] = []
        for entry in os.scandir(f"{extract_path}/packs.zib/"):
            if entry.name.startswith('packdata') and entry.name.endswith('.bin'):
                result.append(entry.name)
        return result

    def create_random_shop_pack(self, i: int):
        pack = Pack(f'random_pack_{i}.bin')
        # ToDo: Balancing ratios from settings?
        pack.common_count = self.random.randint(150, 300)
        pack.rare_count = self.random.randint(25, 75)
        pack.common_ids = [v.id_ for v in self.card_helper.get_random_cards(self.random, k=pack.common_count, limit=1)]
        pack.rare_ids = [v.id_ for v in self.card_helper.get_random_cards(self.random, k=pack.rare_count, limit=1)]
        return pack

    def apply_random_shop_pack_files(self, files):
        dst_folder = f'{compress_path}/packs.zib'
        if not os.path.exists(dst_folder):
            os.mkdir(dst_folder)
        for k, v in files.items():
            dst = f'{dst_folder}/{k}'
            deck = self.random_shop_packs[v]
            print(f'writing {dst}')
            deck.write(dst)

    def get_char_name_for_bust_file(self, bust_file):
        return bust_file[:-(len('_neutral.png'))]

    def shuffle_duelists_portraits(self):
        bust_files = self.get_bust_file_list()
        self.shuffled_bust_files = self.shuffle_list(bust_files)
        dialog_files = self.get_dialog_file_list()
        if self.settings.random_duelist_portraits == RandomDuelistPortraitSettings.Coherent:
            mapping: dict[str, str] = {}
            for k, v in self.shuffled_bust_files.items():
                mapping[self.get_char_name_for_bust_file(k)] = self.get_char_name_for_bust_file(v)

            temp = []
            for df in dialog_files:
                for k, v in mapping.items():
                    if df.startswith(k.lower()):
                        potential_match = df.replace(k, v)
                        if os.path.exists(f'{extract_path}/pdui/dialog_chars/{potential_match}'):
                            self.shuffled_dialog_files[df] = potential_match
                            temp.append(df)
                            break
                        break
            for v in temp:
                dialog_files.remove(v)
        self.shuffled_dialog_files |= self.shuffle_list(dialog_files)
        self.char_dfymoo = Dfymoo()
        self.char_dfymoo.load(f"{extract_path}/pdui/chars.dfymoo")
        combat_portrait_names = self.char_dfymoo.get_names()
        combat_portrait_names.remove('icon_char_locked')
        if self.settings.random_duelist_portraits == RandomDuelistPortraitSettings.Coherent:
            temp = []
            for k, v in self.shuffled_bust_files.items():
                k_removed_png = k[:-len('.png')]
                v_removed_png = v[:-len('.png')]
                actual_v = [v2 for v2 in combat_portrait_names if v_removed_png.lower() == v2.lower()]
                if actual_v is not None and len(actual_v) == 1:
                    actual_v = actual_v[0]
                    actual_k = [v2 for v2 in combat_portrait_names if k_removed_png.lower() == v2.lower()]
                    assert len(actual_k) == 1, f"'putt 'emacht :( {k_removed_png} {combat_portrait_names}"
                    actual_k = actual_k[0]
                    self.shuffled_combat_portrait_names[actual_v] = actual_k
                    temp.append(actual_v)
            for v in temp:
                combat_portrait_names.remove(v)
        self.shuffled_combat_portrait_names |= self.shuffle_list(combat_portrait_names)
        self.shuffled_combat_portrait_names['icon_char_locked'] = 'icon_char_locked'  # force this to be vanilla
        for v in self.char_dfymoo.vals:
            v.n = self.shuffled_combat_portrait_names[v.n]

    def get_bust_file_list(self):
        result: list[str] = []
        for entry in os.scandir(f"{extract_path}/busts.zib/"):
            if entry.name.endswith('.png'):
                result.append(entry.name)
        return result

    def get_dialog_file_list(self):
        result: list[str] = []
        for entry in os.scandir(f"{extract_path}/pdui/dialog_chars"):
            if entry.name.endswith('.png'):
                result.append(entry.name)
        return result

    def set_default_battle_packs(self):
        if self.settings.random_battle_packs == RandomBattlePacksSettings.Off:
            battle_pack_files = self.get_battle_pack_file_list()
            self.shuffled_battle_packs = {v: v for v in battle_pack_files}

    def set_default_shop_packs(self):
        if self.settings.random_battle_packs == RandomBattlePacksSettings.Off:
            shop_pack_files = self.get_shop_pack_file_list()
            self.shuffled_shop_packs = {v: v for v in shop_pack_files}
