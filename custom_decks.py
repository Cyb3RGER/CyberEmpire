import os.path
import random
from datetime import datetime
from enum import IntEnum
from typing import Optional
import logging

from mappers import card_name_mapper


class ParsingMode(IntEnum):
    Init = 0,
    MainDeck = 1,
    ExtraDeck = 2,
    SideDeck = 3
    Filler = 4,
    EOF = 5


class CustomDeckCardGroup:
    def __init__(self, name: str, count: int, factor: int = 1):
        self.name: str = name
        self.count: int = count
        self.factor: int = factor
        self.ids: list[int] = []

    def __str__(self):
        return f'[{self.name} = {self.count}: {self.ids}]'


class CustomDeck:
    def __init__(self, name: str):
        self.name: str = name
        self.main_count: int = 0
        self.main_ids: list[int | CustomDeckCardGroup] = []
        self.extra_count: int = 0
        self.extra_ids: list[int | CustomDeckCardGroup] = []
        self.side_count: int = 0
        self.side_ids: list[int | CustomDeckCardGroup] = []
        self.filler_ids: list[int] = []

    def validate(self, parser):
        if self.main_count == 0:
            raise ParseException(parser, f'Main Deck is empty')
        # make sure groups fit in deck
        main_group_count = sum([i.count * i.factor for i in self.main_ids if type(i) == CustomDeckCardGroup])
        if self.main_count < main_group_count:
            raise ParseException(parser,
                                 f'card groups in Main Deck do not fit. There are {main_group_count - self.main_count} too many cards from groups.')
        extra_group_count = sum([i.count * i.factor for i in self.extra_ids if type(i) == CustomDeckCardGroup])
        if self.extra_count < extra_group_count:
            raise ParseException(parser,
                                 f'card groups in Extra Deck do not fit. There are {extra_group_count - self.extra_count} too many cards from groups.')
        side_group_count = sum([i.count * i.factor for i in self.side_ids if type(i) == CustomDeckCardGroup])
        if self.extra_count < extra_group_count:
            raise ParseException(parser,
                                 f'card groups in Side Deck do not fit. There are {side_group_count - self.side_count} too many cards from groups.')
        # ToDo:

    def __str__(self):
        result = ''

        def _str_ids(ids):
            result = ''
            for i in ids:
                result += '\t'
                if type(i) == type(CustomDeckCardGroup):
                    result += f'{i.name} = {i.count}:\n'
                    for j in i.ids:
                        result += f'\t\t{j}\n'
                else:
                    result += f'{i}\n'
            return result

        result += f'Main Deck = {self.main_count}:\n'
        result += _str_ids(self.main_ids)
        result += f'Extra Deck = {self.extra_count}:\n'
        result += _str_ids(self.extra_ids)
        result += f'Side Deck = {self.side_count}:\n'
        result += _str_ids(self.side_ids)
        result += f'Filler:\n'
        result += _str_ids(self.filler_ids)
        return result


class CustomDeckParser:
    def __init__(self):
        self.file_name: str = ""
        self.line_num: int = 0
        self.mode: ParsingMode = ParsingMode.Init
        self.logger = logging.getLogger('cyber_empire.custom_deck_parser')
        self.logger.setLevel(logging.DEBUG)

    def parse(self, data: str, file_name: Optional[str] = None) -> CustomDeck:
        if file_name:
            self.file_name = file_name
        self.logger.info(f'parsing {self.file_name}...')
        self.mode = ParsingMode.Init
        main_found = False
        extra_found = False
        side_found = False
        filler_found = False
        current_group: Optional[CustomDeckCardGroup] = None
        deck = CustomDeck(os.path.splitext(self.file_name)[0])
        lines = data.splitlines()
        try:
            self.line_num = 0
            for line in lines:
                line = line.strip()
                self.line_num += 1
                if '=' in line or line.startswith('-'):
                    if current_group is not None:
                        if current_group.count == 0:
                            self.logger.warning(
                                f'{self.file_name}:{self.line_num}: ignoring card group "{current_group.name}" with count 0 as it has no effect.')
                        elif len(current_group.ids) <= 0:
                            self.logger.warning(
                                f'{self.file_name}:{self.line_num}: ignoring empty card group "{current_group.name}".')
                        else:
                            if self.mode == ParsingMode.MainDeck:
                                deck.main_ids.append(current_group)
                            elif self.mode == ParsingMode.ExtraDeck:
                                deck.extra_ids.append(current_group)
                            elif self.mode == ParsingMode.SideDeck:
                                deck.side_ids.append(current_group)
                        current_group = None
                if '=' in line:
                    split = line.split('=')
                    if split[0].lower().strip() == 'main deck':
                        if main_found:
                            raise ParseException(self, "Main Deck should only appear once")
                        main_found = True
                        self.mode = ParsingMode.MainDeck
                        deck.main_count = self.get_count(line)
                    elif split[0].lower().strip() == 'extra deck':
                        if extra_found:
                            raise ParseException(self, "Extra Deck should only appear once")
                        extra_found = True
                        self.mode = ParsingMode.ExtraDeck
                        deck.extra_count = self.get_count(line)
                    elif split[0].lower().strip() == 'side deck':
                        if side_found:
                            raise ParseException(self, "Side Deck should only appear once")
                        side_found = True
                        self.mode = ParsingMode.SideDeck
                        deck.side_count = self.get_count(line)
                    elif split[0].lower().strip() == 'filler':
                        if filler_found:
                            raise ParseException(self, "Filler should only appear once")
                        filler_found = True
                        self.mode = ParsingMode.Filler
                    elif self.mode in [ParsingMode.MainDeck, ParsingMode.ExtraDeck, ParsingMode.SideDeck]:
                        group_name = self.get_name(line)
                        group_count, group_factor = self.get_count_and_factor(line)
                        current_group = CustomDeckCardGroup(group_name, group_count, group_factor)
                elif line.isnumeric():
                    id_ = self.get_id(line)
                    if id_ is not None:
                        if current_group is not None:
                            current_group.ids.append(id_)
                        if self.mode == ParsingMode.MainDeck:
                            deck.main_ids.append(id_)
                        elif self.mode == ParsingMode.ExtraDeck:
                            deck.extra_ids.append(id_)
                        elif self.mode == ParsingMode.SideDeck:
                            deck.side_ids.append(id_)
                        elif self.mode == ParsingMode.Filler:
                            deck.filler_ids.append(id_)
                # else:
                #     raise ParseException(self, f'invalid line: {line}')
            # validate
            self.mode = ParsingMode.EOF
            deck.validate(self)
        except ParseException as e:
            self.logger.error(f'{e}')
            raise
        except Exception:
            self.logger.exception('')
            raise
        finally:
            self.mode = ParsingMode.EOF
        self.logger.info('done!')
        return deck

    def load(self, path: str) -> CustomDeck:
        try:
            _, self.file_name = os.path.split(path)
            with open(path, mode='r') as f:
                data = f.read()
            return self.parse(data)
        except IOError:
            self.logger.exception('')
            raise

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

    def get_name(self, line) -> str:
        val = line.split('=')[0].strip()
        if val == '':
            self.logger.warning(f"{self.file_name}:{self.line_num}: missing group name")
        return val

    def get_count(self, line) -> int:
        try:
            cnt = int(line.split('=')[-1].strip())
            if cnt < 0:
                raise ParseException(self, 'invalid count.')
            return cnt

        except:
            raise ParseException(self, 'invalid count.')

    def get_count_and_factor(self, line) -> (int, int):
        try:
            if 'x' not in line:
                return self.get_count(line), 1
            else:
                x_pos = line.find('x')
                return self.get_count(line[:x_pos]), int(line.split('x')[-1].strip())
        except:
            raise ParseException(self, 'invalid factor.')


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
    from logger import setup_logging

    setup_logging()
    parser = CustomDeckParser()
    custom_deck = parser.load(f'custom_decks/test_groups.txt')
    print(custom_deck)
    print('done')
    # deck = custom_deck.get_deck(random.Random())
    # deck.print()
