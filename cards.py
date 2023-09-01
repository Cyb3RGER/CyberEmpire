import csv
import os.path
import random
from collections import Counter
from typing import Literal, Optional

# from gen_card_props import main
from mappers import effect_name_mapper, attribute_name_mapper, spell_type_name_mapper, type_name_mapper, \
    monster_name_mapper
from settings import RandomizerSettings


class CardProps:

    def __init__(self, id_, atk, def_, enabled, effect, attribute, stars, spell_type, type_, pendulum, monster):
        self.id_: int = id_
        self.atk: int = atk
        self.def_: int = def_
        self.enabled: bool = enabled
        self.effect: int = effect
        self.attribute: int = attribute
        self.stars: int = stars
        self.spell_type: int = spell_type
        self.type_: int = type_
        self.pendulum: int = pendulum
        self.monster: int = monster

    @staticmethod
    def get_from_row(row, from_readable: bool = False):
        id_ = int(row['id'])
        atk = row['atk'] if row['atk'] == '?' and from_readable else int(row['atk'])
        def_ = row['def'] if row['def'] == '?' and from_readable else int(row['def'])
        enabled = bool(row['enabled'])
        effect = effect_name_mapper.get_id(row['effect']) if from_readable else int(row['effect'])
        attribute = attribute_name_mapper.get_id(row['attribute']) if from_readable else int(row['attribute'])
        stars = int(row['stars'])
        spell_type = spell_type_name_mapper.get_id(row['spell_type']) if from_readable else int(row['spell_type'])
        type_ = type_name_mapper.get_id(row['type']) if from_readable else int(row['type'])
        pendulum = int(row['pendulum'])
        monster = monster_name_mapper.get_id(row['monster']) if from_readable else int(row['monster'])
        return CardProps(id_, atk, def_, enabled, effect, attribute, stars, spell_type, type_, pendulum, monster)

    def get_as_row(self, readable: bool = False):
        return [self.id_,
                '?' if readable and self.atk == 5110 else self.atk,
                '?' if readable and self.def_ == 5110 else self.def_,
                self.enabled,
                effect_name_mapper.get_name(self.effect) if readable else self.effect,
                attribute_name_mapper.get_name(self.attribute) if readable else self.attribute,
                self.stars,
                spell_type_name_mapper.get_name(self.spell_type) if readable else self.spell_type,
                type_name_mapper.get_name(self.type_) if readable else self.type_,
                self.pendulum,
                monster_name_mapper.get_name(self.monster) if readable else self.monster]

    @staticmethod
    def get_row_header():
        return ['id', 'atk', 'def', 'enabled', 'effect', 'attribute', 'stars', 'spell_type', 'type', 'pendulum',
                'monster']

    def __str__(self):
        return self.get_as_row(True)


class CardHelper:
    def __init__(self, settings: RandomizerSettings):
        self.card_props: dict[int, CardProps] = {}
        self.exclude_xyz_cards: bool = settings.exclude_xyz_cards
        self.exclude_pendulum_cards: bool = settings.exclude_pendulum_cards
        self.exclude_synchro_cards: bool = settings.exclude_synchro_cards
        self.load_card_props()

    def load_card_props(self):
        # if not os.path.exists('data/card_props.csv'):
        #     main()
        self.card_props = {}
        with open('data/card_props.csv', encoding='utf-8', newline='\n') as f:
            reader = csv.DictReader(f, delimiter=',', quotechar='"')
            for row in reader:
                self.card_props[int(row['id'])] = CardProps.get_from_row(row)

    def get_xyz_efffects(self) -> list[int]:
        return [22, 23, 34]

    def get_pendulum_effects(self) -> list[int]:
        return [25, 26, 33, 34, 35, 40, 41, 44, 45]

    def get_synchro_effects(self) -> list[int]:
        return [17, 18, 19, 36]

    def get_normal_and_effect_monsters_effects(self) -> list[int]:
        return [0, 1, 24]

    def get_included_cards(self, type_: Optional[int] = None) -> list[CardProps]:
        def filter_func(x: CardProps) -> bool:
            if self.exclude_xyz_cards and x.monster == 2:
                return False
            if self.exclude_synchro_cards and x.effect in self.get_synchro_effects():
                return False
            if self.exclude_pendulum_cards and x.pendulum != 0:
                return False
            if type_ is not None and x.type_ != type_:
                return False
            return True

        return [v for k, v in self.card_props.items() if filter_func(v)]

    def get_random_card(self, random: random.Random, population: list[CardProps] = None) -> CardProps | None:
        cards = self.get_random_cards(random, population)
        if len(cards) == 1:
            return cards[0]
        return None

    def get_random_cards(self, random: random.Random, population: list[CardProps] = None, k=1) -> list[CardProps]:
        if population is None:
            population = self.get_included_cards()
        cards = random.choices([v for v in population], k=k)
        counter = Counter(cards)
        while any(v > 3 for key, v in counter.items()):
            c = 0
            for key, v in counter.items():
                if v <= 3:
                    continue
                for c in range(v - 3):
                    population.remove(key)
                c += v - 3
            cards += random.choices(population, k=c)
        return cards
    def get_normal_and_effect_monsters(self, random: random.Random, k=1, type_: Optional[int] = None) -> list[
        CardProps]:
        low_level_count = round(k * .75)
        high_level_count = k - low_level_count
        monster_cards = [v for v in self.get_included_cards(type_) if
                         v.effect in self.get_normal_and_effect_monsters_effects()]
        low_level_cards = [v for v in monster_cards if v.stars <= 4]
        high_level_cards = [v for v in monster_cards if v.stars > 4]
        deck = (self.get_random_cards(random, low_level_cards, low_level_count) +
                self.get_random_cards(random, high_level_cards, high_level_count))

        return deck

    def get_spell_and_trap_cards(self, random: random.Random, k=1) -> list[CardProps]:
        spell_count = round(k * .5)
        trap_count = k - spell_count
        included_cards = self.get_included_cards()
        spell_cards = [v for v in included_cards if v.attribute == 8]
        trap_cards = [v for v in included_cards if v.attribute == 9]
        return random.choices(spell_cards, k=spell_count) + random.choices(trap_cards, k=trap_count)
