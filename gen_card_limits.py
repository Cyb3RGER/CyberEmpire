import csv

from io_helper import read_int16
from mappers import card_name_mapper


def main():
    limited_cards: dict[int, int] = {}
    with open('extracted/bin/pd_limits.bin', mode='rb') as f:
        for j in range(0, 3):
            count = read_int16(f)
            for i in range(0, count):
                id_ = read_int16(f)
                limited_cards[id_] = j

    with open('data/card_limits.csv', encoding='utf-8', mode='w', newline='\n') as csvf:
        writer = csv.writer(csvf, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['id', 'limit'])
        for k, v in limited_cards.items():
            writer.writerow([k, v])


if __name__ == '__main__':
    main()
