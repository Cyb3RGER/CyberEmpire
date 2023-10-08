from decks import Deck
from randomizer import compress_path


def main():
    deck = Deck("test.ydc")
    deck.load(f'{compress_path}/decks.zib/1classic_01a_yugimuto.ydc')
    print(deck)


if __name__ == '__main__':
    main()
