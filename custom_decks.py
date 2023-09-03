import os.path
import random
from enum import IntEnum

from mappers import card_name_mapper


class ParsingMode(IntEnum):
    Init = 0,
    MainDeck = 1,
    ExtraDeck = 2,
    SideDeck = 3
    Filler = 4,
    EOF = 5


class CustomDeck:
    def __init__(self, name: str, main_count: int, main_ids: list[int], extra_count: int, extra_ids: list[int],
                 side_count: int, side_ids: list[int], filler_ids: list[int]):
        self.name: str = name
        self.main_count: int = main_count
        self.main_ids: list[int] = main_ids
        self.extra_count: int = extra_count
        self.extra_ids: list[int] = extra_ids
        self.side_count: int = side_count
        self.side_ids: list[int] = side_ids
        self.filler_ids: list[int] = filler_ids


class CustomDeckParser:
    def __init__(self):
        self.file_name: str = ""
        self.line_num: int = 0
        self.mode: ParsingMode = ParsingMode.Init
    def load(self, path) -> CustomDeck:
        self.mode = ParsingMode.Init
        main_count = 0
        main_ids = []
        extra_count = 0
        extra_ids = []
        side_count = 0
        side_ids = []
        filler_ids = []
        _, self.file_name = os.path.split(path)
        main_found = False
        extra_found = False
        side_found = False
        filler_found = False
        try:
            with open(path, mode='r') as f:
                lines = f.read().splitlines()
            self.line_num = 0
            for line in lines:
                self.line_num += 1
                if line.lower().startswith('main'):
                    if main_found:
                        raise ParseException(self, "Main Deck should only appear once")
                    main_found = True
                    self.mode = ParsingMode.MainDeck
                    main_count = self.get_count(line)
                elif line.lower().startswith('extra'):
                    if extra_found:
                        raise ParseException(self, "Extra Deck should only appear once")
                    extra_found = True
                    self.mode = ParsingMode.ExtraDeck
                    extra_count = self.get_count(line)
                elif line.lower().startswith('side'):
                    if side_found:
                        raise ParseException(self, "Side Deck should only appear once")
                    side_found = True
                    self.mode = ParsingMode.SideDeck
                    side_count = self.get_count(line)
                elif line.lower().startswith('filler'):
                    if filler_found:
                        raise ParseException(self, "Side Deck should only appear once")
                    filler_found = True
                    self.mode = ParsingMode.Filler
                else:
                    id_ = self.get_id(line)
                    if id_ is not None:
                        if self.mode == ParsingMode.MainDeck:
                            main_ids.append(id_)
                        elif self.mode == ParsingMode.ExtraDeck:
                            extra_ids.append(id_)
                        elif self.mode == ParsingMode.SideDeck:
                            side_ids.append(id_)
                        elif self.mode == ParsingMode.Filler:
                            filler_ids.append(id_)
        except:
            raise
        finally:
            self.mode = ParsingMode.EOF
        # validate
        # ToDo: should we enforce card limits here??
        if main_count > len(main_ids) and len(filler_ids) == 0:
            raise ParseException(self, "not enough cards to fill Main Deck")
        if extra_count > len(extra_ids) and len(filler_ids) == 0:
            raise ParseException(self, "not enough cards to fill Extra Deck")
        if side_count > len(side_ids) and len(filler_ids) == 0:
            raise ParseException(self, "not enough cards to fill Side Deck")
        return CustomDeck(os.path.splitext(self.file_name)[0], main_count, main_ids, extra_count, extra_ids, side_count,
                          side_ids, filler_ids)

    def get_id(self, line):
        if line.strip() == '':
            return None
        try:
            id_ = int(line.strip())
            if card_name_mapper.is_valid_id(id_):
                return id_
            else:
                raise ParseException(self, f'unknown card id {id_}')
        except ParseException:
            raise
        except:
            raise ParseException(self, f'invalid card id {line}')

    def get_count(self, line):
        try:
            return int(line.split('=')[-1].strip())
        except:
            return 0


class ParseException(Exception):
    def __init__(self, parser_: CustomDeckParser, text: str, *args):
        self.file_name = parser_.file_name
        self.line_num = parser_.line_num
        self.mode: ParsingMode = parser_.mode
        self.text: str = text
        super().__init__(args)

    def __str__(self):
        line_num_str = f':{self.line_num}' if self.mode not in [ParsingMode.Init, ParsingMode.EOF] else ''
        return f'Custom deck parsing error: {self.file_name}{line_num_str}: {self.mode.name}: {self.text}'


if __name__ == '__main__':
    parser = CustomDeckParser()
    custom_deck = parser.load(f'custom_decks/ultimate_reduction.txt')
    deck = custom_deck.get_deck(random.Random())
    deck.print()
