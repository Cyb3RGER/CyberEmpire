import csv

from cards import CardProps


def mask(val, size, shift=0):
    mask = 0
    for i in range(0, size):
        mask |= (1 << i)
    mask <<= shift
    return (val & mask) >> shift, shift + size


def main():
    with open('extracted/bin/CARD_Prop.bin', mode='rb') as f:
        f.seek(8)
        props_bytes = f.read()
    card_props: list[CardProps] = []
    for i in range(0, len(props_bytes), 8):
        prop_bytes = int.from_bytes(props_bytes[i:i + 8], byteorder="little")
        shift = 0
        _id, shift = mask(prop_bytes, 0xe, shift)
        atk, shift = mask(prop_bytes, 0x9, shift)
        atk *= 10
        _def, shift = mask(prop_bytes, 0x9, shift)
        _def *= 10
        enabled_val, shift = mask(prop_bytes, 0x1, shift)
        enabled = True if enabled_val else False
        effect, shift = mask(prop_bytes, 0x6, shift)
        attribute, shift = mask(prop_bytes, 0x4, shift)
        stars, shift = mask(prop_bytes, 0x4, shift)
        spell_type, shift = mask(prop_bytes, 0x3, shift)
        _type, shift = mask(prop_bytes, 0x5, shift)
        pendulum, shift = mask(prop_bytes, 0x4, shift)
        monster, shift = mask(prop_bytes, 0x2, shift)
        # unused, _ = mask(prop_bytes, 0x3, shift)
        card_props.append(
            CardProps(_id, atk, _def, enabled, effect, attribute, stars, spell_type, _type, pendulum, monster))

    with open('data/card_props.csv', encoding='utf-8', mode='w', newline='\n') as csvf:
        writer = csv.writer(csvf, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(CardProps.get_row_header())
        for card_prop in card_props:
            writer.writerow(card_prop.get_as_row())

    with open('data/card_props_readable.csv', encoding='utf-8', mode='w', newline='\n') as csvf:
        writer = csv.writer(csvf, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(CardProps.get_row_header())
        for card_prop in card_props:
            writer.writerow(card_prop.get_as_row(True))


if __name__ == '__main__':
    main()
