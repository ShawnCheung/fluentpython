import collections

Cards = collections.namedtuple("card", ['rank', 'suit'])


class FrenchDeck:
    rank = [str(n) for n in range(2, 11)] + list("JQKA")
    suit = "spads diamonds clubs hearts".split()

    def __init__(self,):
        self._card = [Cards(rank=r, suit=s) for r in self.rank
                                            for s in self.suit]

    def __len__(self,):
        return len(self._card)

    def __getitem__(self, position):
        return self._card[position]

card = Cards('7', 'diamond')
deck  = FrenchDeck()
print(len(deck), deck[10])


from random import choice

print(choice(deck))
print(choice(deck))
print(choice(deck))
print(choice(deck))

print(deck[1:10])

for item in deck:
    print(item)

print(Cards(rank='10', suit='spads') in deck)
print(Cards(rank=10, suit='spadss') in deck)

suit_values = dict(spads=3, hearts=2, diamonds=1, clubs=0)

def spads_high(card):
    rank_value = FrenchDeck.rank.index(card.rank)
    return rank_value*len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key = spads_high):
    print(card)
