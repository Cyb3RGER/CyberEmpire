import os
import random

from io_helper import *
from mappers import *


class Deck:

    def __init__(self, name: str):
        self.name: str = name
        self.magic_value: int = 0x648c
        self.main_count: int = 0
        self.main_ids: list[int] = []
        self.extra_count: int = 0
        self.extra_ids: list[int] = []
        self.side_count: int = 0
        self.side_ids: list[int] = []

    def load(self, file_path: str):
        with open(file_path, mode='rb') as f:
            self.magic_value = read_int64(f)
            self.main_count = read_int16(f)
            for i in range(0, self.main_count):
                self.main_ids.append(read_int16(f))
            self.extra_count = read_int16(f)
            for i in range(0, self.extra_count):
                self.extra_ids.append(read_int16(f))
            self.side_count = read_int16(f)
            for i in range(0, self.side_count):
                self.side_ids.append(read_int16(f))

    def write(self, file_path: str):
        with open(file_path, mode='wb') as f:
            write_int64(f, self.magic_value)
            write_int16(f, self.main_count)
            for i in range(0, self.main_count):
                write_int16(f, self.main_ids[i])
            write_int16(f, self.extra_count)
            for i in range(0, self.extra_count):
                write_int16(f, self.extra_ids[i])
            write_int16(f, self.side_count)
            for i in range(0, self.side_count):
                write_int16(f, self.side_ids[i])

    def print(self):
        print(f"Main Deck ({self.main_count} cards):")
        for i in range(0, self.main_count):
            print(i + 1, self.main_ids[i], card_name_mapper.get_name(self.main_ids[i]))
        print(f"Extra Deck ({self.extra_count} cards):")
        for i in range(0, self.extra_count):
            print(i + 1, self.extra_ids[i], card_name_mapper.get_name(self.extra_ids[i]))
        print(f"Side Deck ({self.side_count} cards):")
        for i in range(0, self.side_count):
            print(i + 1, self.side_ids[i], card_name_mapper.get_name(self.side_ids[i]))


class DeckInfo:

    def __init__(self, file: IO):
        self.cards: list[Deck] = []
        self.deck_id: int = 0
        self.deck_id_2: int = 0
        self.series_id: int = 0
        self.sig_card_id: int = 0
        self.char_id: int = 0
        self.dlc_flag: int = 0
        self.deck_id_name_ptr: int = 0
        self.deck_name_ptr: int = 0
        self.unknown_str_ptr: int = 0
        self.unknown_str_2_ptr: int = 0
        self.deck_id_name: str = ""
        self.deck_name: str = ""
        self.unknown_str: str = ""
        self.unknown_str_2: str = ""
        self.load(file)

    def load(self, f: IO):
        self.deck_id = read_int32(f)
        self.deck_id_2 = read_int32(f)
        self.series_id = read_int32(f)
        self.sig_card_id = read_int32(f)
        self.char_id = read_int32(f)
        self.dlc_flag = read_int32(f)
        self.deck_id_name_ptr = read_int64(f)
        self.deck_name_ptr = read_int64(f)
        self.unknown_str_ptr = read_int64(f)
        self.unknown_str_2_ptr = read_int64(f)

    def write(self, f: IO):
        write_int32(f, self.deck_id)
        write_int32(f, self.deck_id_2)
        write_int32(f, self.series_id)
        write_int32(f, self.sig_card_id)
        write_int32(f, self.char_id)
        write_int32(f, self.dlc_flag)
        write_int64(f, self.deck_id_name_ptr)
        write_int64(f, self.deck_name_ptr)
        write_int64(f, self.unknown_str_ptr)
        write_int64(f, self.unknown_str_2_ptr)

    def load_strings(self, f: IO):
        f.seek(self.deck_id_name_ptr, 0)
        self.deck_id_name = read_string_u8(f)
        f.seek(self.deck_name_ptr, 0)
        self.deck_name = read_string_u16(f)
        f.seek(self.unknown_str_ptr, 0)
        self.unknown_str = read_string_u16(f)
        f.seek(self.unknown_str_2_ptr, 0)
        self.unknown_str_2 = read_string_u16(f)

    def write_strings(self, f: IO):
        f.seek(self.deck_id_name_ptr, 0)
        write_string_u8(f, self.deck_id_name)
        f.seek(self.deck_name_ptr, 0)
        write_string_u16(f, self.deck_name)
        f.seek(self.unknown_str_ptr, 0)
        write_string_u16(f, self.unknown_str)
        f.seek(self.unknown_str_2_ptr, 0)
        write_string_u16(f, self.unknown_str_2)

    def load_cards(self, game_path: str):
        self.cards = Deck(f"{game_path}/decks.zib/{self.deck_id_name}.ydc")

    def print(self):
        print("deck", f"{self.deck_id}", f"{self.deck_id_name}", f"{self.deck_name}",
              f"{card_name_mapper.get_name(self.sig_card_id)}", f"{char_name_mapper.get_char_name(self.char_id)}")
        if self.cards:
            self.cards.print()


class DeckData:
    def __init__(self, path):
        self.deck_count: int = 0
        self.decks: list[DeckInfo] = []
        self.load(path)

    def load(self, path):
        with open(f'{path}/main/deckdata_E.bin', mode='rb') as f:
            self.deck_count = read_int64(f)
            for i in range(0, self.deck_count):
                self.decks.append(DeckInfo(f))
            for i in range(0, self.deck_count):
                self.decks[i].load_strings(f)

    def write(self, path):
        if not os.path.exists(f'{path}/main'):
            os.mkdir(f'{path}/main')
        with open(f'{path}/main/deckdata_E.bin', mode='wb') as f:
            write_int64(f, self.deck_count)
            for i in range(0, self.deck_count):
                self.decks[i].write(f)
            for i in range(0, self.deck_count):
                self.decks[i].write_strings(f)

    def print(self):
        print(f"deck data: {self.deck_count} decks\n")
        for i in range(0, self.deck_count):
            self.decks[i].print()

    def get_deck_by_sig_card_id(self, card) -> DeckInfo:
        return [deck for deck in self.decks if deck.sig_card_id == card][0]
