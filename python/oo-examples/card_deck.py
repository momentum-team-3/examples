
from random import shuffle
import pprint


class Card:

    ranks = ("A", '2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K")
    suits = ("Clubs", "Diamonds", "Hearts", "Spades")

    def __init__(self, rank, suit, ace_high=True):
        if rank not in self.ranks:
            raise ValueError("That is not a valid rank")
        if suit not in self.suits:
            raise ValueError("That is not a valid suit")

        # instance attributes
        self.rank = rank
        self.suit = suit
        self.ace_high = ace_high

    def number_value(self):
        # Convert rank to a numeric value
        # If aces are low, this is just one more than the
        # index. Otherwise, it's the index itself, or the length
        # of the ranks tuple for aces
        if self.ace_high:
            if self.rank == "A":
                return len(self.ranks)

            else:
                return self.ranks.index(self.rank)

        else:
            return self.ranks.index(self.rank) + 1

    def __repr__(self):
        return f"<Card rank={self.rank} suit={self.suit}>"

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Hand:
    """ This class holds cards and implements methods for scoring a hand.
    """
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)



class Player:
    """ Base class for entities that will play the game.
    """
    def __init__(self):
        self.hand = []
        self.dealer = 

    def hit(self, deck):
        # Add a card to self.hand from the supplied deck
        card = deck.deal()
        self.hand.append(card)
        
    def stay(self):
        # This method does nothing at present
        return

    def score(self):
        return sum([card.number_value() for card in hand()])

    def __str__(self):
        pass


class Deck:
    def __init__(self):
        self.cards = []
        for rank in Card.ranks:
            for suit in Card.suits:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        shuffle(self.cards)

    def deal(self):
        # Remove the top card from the deck and return it.
        # For convenience, we count the end of the list
        # self.cards as the 'top' of the deck (but it doesn't matter).
        return self.cards.pop()
 
    def __str__(self):
        return f"<Deck total_cards={len(self.cards)}>"
