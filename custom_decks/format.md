# Format for custom decks

```
Main Deck = <amount of cards>
<id>
<id>
<id>
...
or
<name of group> = <amount of cards> x <factor>
<id>
<id>
<id>
...
<group>
<group>
<group>
...
or
<group>
-
<id>
<id>
<group>
...
Extra Deck = <amount of cards>
<deck>
Side Deck = <amount of cards>
<deck>
Filler 
<id>
<id>
<id>
...
```

## Decks (``<deck>``)

Starts with ``<name of deck> = <amount of cards>`` followed by a ``<deck>``.

``<deck>`` is either a list of card ids ([see ``<id>``](#ids-id)) or list of card groups ([see ``<group>``](#groups-group)).


## Groups (``<group>``)

``<group>`` is a card group.

A card group starts with ``<name of group> = <amount of cards> x <factor>`` followed by a list of [``<id>``](#ids-id).

``<name of group>`` can be any string not containing a whitespace.

``x <factor>`` is optional and will copy the picked cards ``<factor>`` times. Keep in mind that the group then effectively becomes ``<amount of cards> * <factor>`` cards big.

You can use ``-`` to indicate the end of a card group.


## IDs (``<id>``)

``<id>`` is the decimal id of the card.

For a full list of card ids see ``data/cards.csv``. 

## Filler

``Filler`` followed by a list of [card ids](#ids-id) that will fill up empty space in **any** deck.


## Fill rules

For [decks](#decks-deck) and [groups](#groups-group) applies:

- If more card ids are listed then ``<amount of cards>``,  ``<amount of cards>`` random card ids are picked from the list.
- If less card ids are listed then ``<amount of cards>``, empty space will be filled with duplicates form that list.

For [decks](#decks-deck) applies:

- If Filler is specified, empty space will be filled up with the cards specified under Filler instead.

## Example

ToDo




