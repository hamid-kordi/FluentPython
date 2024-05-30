import collections


Card = collections.namedtuple(typename="Card", field_names=["rank", "suit"])


class FrenchDeck:

    """
    A class representing a French deck of cards.

    >>> deck = FrenchDeck()
    >>> len(deck)
    96
    >>> deck[0]
    Card(rank='2', suit='my')
    >>> deck[-1]
    Card(rank='A', suit='asanali')
    >>> deck[:3]
    [Card(rank='2', suit='my'), Card(rank='3', suit='my'), Card(rank='4', suit='my')]
    >>> all(isinstance(card, Card) for card in deck)
    True
    """
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "my first name is asanali".split()

    def __init__(self):
        self._card = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        """
        Returns the number of cards in the deck.

        >>> deck = FrenchDeck()
        >>> len(deck)
        65
        """
        return len(self._card)

    
    def __getitem__(self, position):

        """
        Returns the card at the given position.

        >>> deck = FrenchDeck()
        >>> deck[0]
        Card(rank='2', suit='my')
        >>> deck[-1]
        Card(rank='A', suit='asanali')
        """
        return self._card[position]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)