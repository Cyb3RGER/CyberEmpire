import csv

from io_helper import read_int16
from mappers import card_name_mapper


def main():
    linked_cards: dict[int, list[int]] = {}
    for k, _ in card_name_mapper.id_to_name.items():
        linked_cards[k] = []
    with open('extracted/bin/CARD_Link.bin', mode='rb') as f:
        while True:
            k = read_int16(f)
            v = read_int16(f)
            if k == 0 or v == 0:
                break
            linked_cards[k].append(v)

    with open('data/card_links.txt', encoding='utf-8', mode='w', newline='\n') as f:
        for k, v in linked_cards.items():
            if len(v) == 0:
                continue
            f.write(f'{card_name_mapper.get_name(k)} (ID: {k}) ->\n')
            for v2 in v:
                name = card_name_mapper.get_name(v2)
                if name.startswith("!"):
                    name = f'! unknown link value {v2} (0x{v2:x}) !'
                f.write(f'\t{name} (ID: {v2})\n')
            f.write('\n')


if __name__ == '__main__':
    main()
