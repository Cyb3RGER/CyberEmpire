import csv
from typing import Literal


class NameMapper:

    def __init__(self):
        self.name_to_id: dict[str, int] = dict()
        self.id_to_name: dict[int, str] = dict()

    def load(self, file_path: str, id_base: int = 10, order: Literal['id_first', 'name_first'] = 'id_first'):
        if order not in ['id_first', 'name_first']:
            return
        with open(file_path, encoding='utf-8', newline='\n') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            for row in reader:
                if order == 'id_first':
                    self.id_to_name[int(row[0], id_base)] = row[1]
                    self.name_to_id[row[1]] = int(row[0], id_base)
                else:
                    self.name_to_id[row[0]] = int(row[1], id_base)
                    self.id_to_name[int(row[1], id_base)] = row[0]

    def __str__(self):
        result = ''
        for k, v in self.id_to_name.items():
            result += f'{k}: {v}\n'


class CardNameMapper(NameMapper):
    def __init__(self):
        super().__init__()
        self.load('data/cards.csv', order='name_first')

    def get_name(self, card_id: int) -> str:
        if card_id == 0xffffffff:
            return "None"
        if card_id not in self.id_to_name:
            return f"! Unknown Card {card_id:x} !"
        return self.id_to_name[card_id]

    def get_id(self, name: str) -> int:
        if name not in self.name_to_id:
            return -1
        return self.name_to_id[name]

    def is_valid_id(self, card_id: int) -> bool:
        return card_id in self.id_to_name

class CharNameMapper(NameMapper):
    def __init__(self):
        super().__init__()
        self.load('data/chars.csv', id_base=16)

    def get_name(self, char_id: int):
        if char_id not in self.id_to_name:
            return f"! Unknown Char {char_id:x} !"
        return self.id_to_name[char_id]

    def get_id(self, name: str) -> int:
        if name not in self.name_to_id:
            return -1
        return self.name_to_id[name]


class ArenaNameMapper(NameMapper):
    def __init__(self):
        super().__init__()
        self.load('data/arenas.csv', id_base=16)

    def get_name(self, arena_id: int):
        if arena_id not in self.id_to_name:
            return f"! Unknown Arena {arena_id:x} !"
        return self.id_to_name[arena_id]

    def get_id(self, name: str) -> int:
        if name not in self.name_to_id:
            return -1
        return self.name_to_id[name]


class EffectNameMapper(NameMapper):
    # ToDO: clean-up this list
    effects = {
        0: "normal monsters",
        1: "effect monsters",
        2: "fusion normal monsters",
        3: "fusion effect monsters",
        4: "normal ritual monsters",
        5: "effect ritual monsters",
        6: "toons",
        7: "spirit",
        8: "union",
        9: "gemini",
        10: "tokens",
        13: "spell",
        14: "trap",
        15: "normal tuners",
        16: "Tuners",
        17: "synchro monsters that have no effect, so just like Normal synchro",
        18: "synchro population that have effects",
        19: "synchro are also tuners",
        22: "normal xyz monsters",
        23: "xyz monsters with effects",
        24: "effect monsters",  # this is double for some reason
        25: "pendulum normal monsters",
        26: "pendulum effect monsters",
        27: "special summon monsters only",
        28: "toon special summons",
        29: "spirit monster",
        30: "trap monsters without effects",
        32: "tuner + flip",
        33: "pendulum + tuner",
        34: "xyz + pendulum",
        35: "pendulum + flip",
        36: "synchro + pendulum",
        37: "union + tuner",
        38: "ritual + spirit",
        39: "fusion + tuner",
        40: "pendulum monster",
        41: "fusion + pendulum monsters",
        42: "link with no effect/normal",
        43: "link with effect",
        44: "pendulum + tuner",
        45: "pendulum + spirit",
    }

    def __init__(self):
        super().__init__()
        self.load()

    def load(self):
        self.id_to_name = self.effects
        self.name_to_id = {v: k for k, v in self.id_to_name.items()}

    def get_name(self, id: int):
        if id not in self.id_to_name:
            return f"! Unknown effect {id:x} !"
        return self.id_to_name[id]

    def get_id(self, name):
        if name not in self.name_to_id:
            return -1
        return self.name_to_id[name]


class AttributesNameMapper(NameMapper):
    attributes = {
        0: "?",
        1: "Light",
        2: "Dark",
        3: "Water",
        4: "Fire",
        5: "Earth",
        6: "Wind",
        7: "Divine",
        8: "Spell",
        9: "Trap",
    }

    def __init__(self):
        super().__init__()
        self.load()

    def load(self):
        self.id_to_name = self.attributes
        self.name_to_id = {v: k for k, v in self.id_to_name.items()}

    def get_name(self, id):
        if id not in self.id_to_name:
            return f"! Unknown attribute {id:x} !"
        return self.id_to_name[id]

    def get_id(self, name):
        if name not in self.name_to_id:
            return -1
        return self.name_to_id[name]


class SpellTypeNameMapper(NameMapper):
    spell_types = {
        0: "?",
        1: "Counter trap",
        2: "Field",
        3: "Equip",
        4: "Continous",
        5: "Quick-Play",
        6: "Ritual",
    }

    def __init__(self):
        super().__init__()
        self.load()

    def load(self):
        self.id_to_name = self.spell_types
        self.name_to_id = {v: k for k, v in self.id_to_name.items()}

    def get_name(self, id):
        if id not in self.id_to_name:
            return f"! Unknown spell type {id:x} !"
        return self.id_to_name[id]

    def get_id(self, name):
        if name not in self.name_to_id:
            return -1
        return self.name_to_id[name]


class TypeNameMapper(NameMapper):
    types = {
        0: "?",
        1: "Dragon",
        2: "Zombie",
        3: "Fiend",
        4: "Pyro",
        5: "Sea Serpent",
        6: "Rock",
        7: "Machine",
        8: "Fish",
        9: "Dinosaur",
        10: "Insect",
        11: "Beast",
        12: "Beast Warrior",
        13: "Plant",
        14: "Aqua",
        15: "Warrior",
        16: "Winged Beast",
        17: "Fairy",
        18: "Spellcaster",
        19: "Thunder",
        20: "Reptile",
        21: "Psychic",
        22: "Wyrm",
        23: "Cyberse",
        24: "Divine Beast",
        30: "Spell",
        31: "Trap",
    }

    def __init__(self):
        super().__init__()
        self.load()

    def load(self):
        self.id_to_name = self.types
        self.name_to_id = {v: k for k, v in self.id_to_name.items()}

    def get_name(self, id):
        if id not in self.id_to_name:
            return f"! Unknown type {id:x} !"
        return self.id_to_name[id]

    def get_id(self, name):
        if name not in self.name_to_id:
            return -1
        return self.name_to_id[name]


class MonsterNameMapper(NameMapper):
    monsters = {
        0: "?",
        1: "Normal",
        2: "XYZ",
        3: "Link",
    }

    def __init__(self):
        super().__init__()
        self.load()

    def load(self):
        self.id_to_name = self.monsters
        self.name_to_id = {v: k for k, v in self.id_to_name.items()}

    def get_name(self, id):
        if id not in self.id_to_name:
            return f"! Unknown attribute {id:x} !"
        return self.id_to_name[id]

    def get_id(self, name):
        if name not in self.name_to_id:
            return -1
        return self.name_to_id[name]


card_name_mapper = CardNameMapper()
char_name_mapper = CharNameMapper()
arena_name_mapper = ArenaNameMapper()
effect_name_mapper = EffectNameMapper()
attribute_name_mapper = AttributesNameMapper()
spell_type_name_mapper = SpellTypeNameMapper()
type_name_mapper = TypeNameMapper()
monster_name_mapper = MonsterNameMapper()
