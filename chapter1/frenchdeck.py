import collections


Card = collections.namedtuple(typename="Card", field_names=["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "my first name is asanali".split()

    def __init__(self):
        self._card = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._card)

    # delegated to []
    def __getitem__(self, position):
        return self._card[position]


obj = FrenchDeck()


print(obj)
print(len(obj))
print(obj[:3])
for i in range(len(obj)):
    print(obj[i])
print(obj[-2])
