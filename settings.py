import json
from collections import namedtuple
from enum import IntEnum
from json import JSONEncoder


class RandomizerSettingsEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def decode_randomizer_settings(dict):
    obj = RandomizerSettings()
    for k, v in dict.items():
        if hasattr(obj, k):
            setattr(obj, k, v)
    return obj


class RandomDeckSettings(IntEnum):
    Off = 0,
    Balanced = 1,
    Full_Random = 2,
    By_Type = 3,
    Shuffled = 4,
    Archtype = 5,


class RandomShopPackSettings(IntEnum):
    Off = 0,
    Shuffled = 1
    Randomized = 2


class RandomBattlePacksSettings(IntEnum):
    Off = 0,
    Shuffled = 1
    Randomized = 2


class RandomizerSettings:
    def __init__(self):
        # deck_data
        self.random_decks: int = RandomDeckSettings.Balanced  # ToDo: Archtype
        self.exclude_xyz_cards: bool = True
        self.exclude_synchro_cards: bool = True
        self.exclude_pendulum_cards: bool = True
        self.include_custom_decks: bool = True
        self.only_starter_decks: bool = False
        # ToDo: custom balancing options? like monster percentage etc.
        # deck balancing
        self.mon_percent: int = 50
        self.low_level_percent: int = 75
        self.high_level_percent: int = 25
        self.spell_trap_percent: int = 50
        self.spell_percent: int = 50
        self.trap_percent: int = 50
        # duelists
        self.random_duelist_portraits: bool = True  # ToDo
        self.link_duelists_portraits: bool = True  # ToDo
        self.link_duelists_decks: bool = False  # ToDo
        self.random_sig_cards: bool = True
        # shop
        self.random_shop_packs: int = RandomShopPackSettings.Randomized
        self.shuffle_shop_portraits: bool = True # ToDo
        self.random_shop_prices: bool = True
        self.shop_min_price: int = 100  # ToDo: better default values?
        self.shop_max_price: int = 1000  # ToDo: better default values?
        # arenas
        self.shuffle_arenas: bool = True

        self.random_battle_packs: int = RandomBattlePacksSettings.Off  # ToDo

    @staticmethod
    def load(path):
        try:
            with open(path, mode='r') as f:
                return json.load(f, object_hook=decode_randomizer_settings)
        except:
            temp = RandomizerSettings()
            temp.save(path)
            return temp

    def save(self, path):
        with open(path, mode='w') as f:
            json.dump(self, f, indent=4, cls=RandomizerSettingsEncoder)

    def __str__(self):
        return json.dumps(self, indent=4, cls=RandomizerSettingsEncoder)
