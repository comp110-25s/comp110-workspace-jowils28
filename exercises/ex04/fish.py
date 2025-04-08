"""File to define Fish class."""

__author__: str = "730774862"


class Fish:
    """New class Fish"""

    age: int

    def __init__(self):
        """Initializes the fish class with age"""
        self.age = 0  # start age at 0
        return None

    def one_day(self):
        """What changes for each fish in one day"""
        self.age += 1  # each day age increases by 1
        return None
