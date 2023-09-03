# Format for custom decks

``<name of deck> = <amount of cards>`` followed by a list of card ids.

If more card ids are listed then ``<amount of cards>``,  ``<amount of cards>`` random card ids are picked from the list.

If less card ids are listed then ``<amount of cards>``, empty space will be filled up with the card specified under Filler.
If Fill is not specified empty space will be fill with duplicates form that deck.

``Filler``
followed by a list of card ids that will fill up empty space in **any** deck.

``<id>`` is the decimal id of the card.
For a full list of card ids see ``data/cards.csv``. 

```
Main Deck = <amount of cards>
<id>
<id>
<id>
...
Extra Deck = <amount of cards>
<id>
<id>
<id>
...
Side Deck = <amount of cards>
<id>
<id>
<id>
...
Filler 
<id>
<id>
<id>
...
```

