class Card():
    SUITS = ("Hearts", "Clubs", "Spades", "Diamonds")
    RANKS = (
                "2", "3", "4", "5", "6", "7", "8", "9", "10",
                "Jack", "Queen", "King", "Ace"
            )

    @classmethod
    def create_standard_52_cards(cls):
        # use cls instead of name of class
        # to enhance reusibility.
        # What if name changes tomorrow?
        # cls will still work.

        return [
            cls(rank = rank, suit = suit)
            for suit in cls.SUITS
            for rank in cls.RANKS
        ]


    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank. Rank must be one of the following: {self.RANKS}")
        
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit. Suit must be one of the following: {self.SUITS}")

        self.rank = rank
        self.rank_index = self.RANKS.index(rank)
        self.suit = suit

    # string representation
    def __str__(self):
        return f"{self.rank} of {self.suit}"

    # technical representation
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"  

    # how equality should be checked
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit 
    
    # how to compare by ranks
    def __lt__(self, other):
        # can't compare values directly b/c
        # of string comparisons:
        # "Queen" alphabetically > "King"
        # and "10" < "9" b/c compares by first char
        # Ergo, must compare by index position
        # in ranks, as they're ordered there.
        if (self.rank == other.rank):
            return self.suit < other.suit
            
        return self.rank_index < other.rank_index