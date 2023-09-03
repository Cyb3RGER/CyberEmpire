import csv
import os.path
import random
from collections import Counter
from typing import Literal, Optional

from custom_decks import CustomDeck
from decks import Deck
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
        self.exclude_link_cards: bool = settings.exclude_link_cards
        self.exclude_union_cards: bool = settings.exclude_union_cards
        self.exclude_gemini_cards: bool = settings.exclude_gemini_cards
        self.exclude_tuner_cards: bool = settings.exclude_tuner_cards
        self.exclude_spirit_cards: bool = settings.exclude_spirit_cards
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

    def get_link_effects(self) -> list[int]:
        return [42, 43]

    def get_union_effects(self) -> list[int]:
        return [8, 37]

    def get_gemini_effects(self) -> list[int]:
        return [9]

    def get_tuner_effects(self) -> list[int]:
        return [15, 16, 19, 32, 33, 37, 39, 44]

    def get_spirit_effects(self) -> list[int]:
        return [7, 29, 38, 45]

    def get_normal_and_effect_monsters_effects(self) -> list[int]:
        return [0, 1, 24]

    def get_included_cards(self, type_: Optional[int] = None) -> list[CardProps]:
        def filter_func(x: CardProps) -> bool:
            if (self.exclude_xyz_cards and x.monster == 2
                    or self.exclude_synchro_cards and x.effect in self.get_synchro_effects()
                    or self.exclude_pendulum_cards and (x.pendulum != 0 or x.effect in self.get_pendulum_effects())
                    or self.exclude_link_cards and (x.monster == 3 or x.effect in self.get_link_effects())
                    or self.exclude_union_cards and x.effect in self.get_union_effects()
                    or self.exclude_gemini_cards and x.effect in self.get_gemini_effects()
                    or self.exclude_tuner_cards and x.effect in self.get_tuner_effects()
                    or self.exclude_spirit_cards and x.effect in self.get_spirit_effects()
                    or type_ is not None and x.type_ != type_):
                return False
            return True

        return [v for k, v in self.card_props.items() if filter_func(v)]

    def get_random_card(self, random: random.Random, population: list[CardProps] = None) -> CardProps | None:
        cards = self.get_random_cards(random, population)
        if len(cards) == 1:
            return cards[0]
        return None

    def get_random_cards(self, random: random.Random, population: list[CardProps] = None, k=1, limit: int = 3) -> list[
        CardProps]:
        if population is None:
            population = self.get_included_cards()
        assert len(population) > 0, f'how? {population}, {k}'
        cards = random.choices(population, k=k)
        # check for limit
        counter = Counter(cards)
        while any(v > limit for key, v in counter.items()):
            reroll_count = 0
            for key, v in counter.items():
                if v <= limit:
                    continue
                # remove card that is over limit from population
                population.remove(key)
                # calc how many over limit
                over_limit = v - limit
                # remove over limit cards
                for _ in range(over_limit):
                    cards.remove(key)
                # add over limit count to reroll count
                reroll_count += over_limit
            # reroll cards
            cards += random.choices(population, k=reroll_count)
            counter = Counter(cards)
        assert len(cards) == k, f"oops, looks like we fucked up the re-roll for limits: {len(cards)} != {k}"
        return cards

    def get_deck_from_custom_deck(self, custom_deck: CustomDeck, random: random.Random) -> Deck:
        deck = Deck(f'custom_{custom_deck.name}')
        deck.main_count = custom_deck.main_count
        deck.main_ids = self._get_id_list(random, custom_deck.main_ids, custom_deck.main_count, custom_deck.filler_ids)
        deck.extra_count = custom_deck.extra_count
        deck.extra_ids = self._get_id_list(random, custom_deck.extra_ids, custom_deck.extra_count,
                                           custom_deck.filler_ids)
        deck.side_count = custom_deck.side_count
        deck.side_ids = self._get_id_list(random, custom_deck.side_ids, custom_deck.side_count, custom_deck.filler_ids)
        return deck

    def _get_id_list(self, random: random.Random, id_list: list[int], count: int, filler: list[int]) -> list[int]:
        result: list[int]
        if len(id_list) > count:
            result = random.choices(id_list, k=count)
        else:
            result = id_list.copy()
        if len(result) < count:
            if len(filler) > 0:
                result += random.choices(filler, k=count - len(result))
            else:
                raise 'not enough cards to fill deck'
        return result
