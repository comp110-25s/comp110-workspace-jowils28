"""File to define Bear class."""

__author__: str = "730774862"


class Bear:
    """New class Bear"""

    age: int
    hunger_score: int

    def __init__(self):
        """initializes the bear class with age and hunger_score"""
        self.age = 0  # start age at 0
        self.hunger_score = 0  # start hunger_score at 0
        return None

    def one_day(self):
        """What changes for each bear in one day"""
        self.age += 1  # each day age increases by 1
        self.hunger_score -= 1  # each day hunger score decreases by 1
        return None

    def eat(self, num_fish: int):
        """updates bears hunger score based on fish eaten"""
        self.hunger_score += num_fish  # hunger score is how many fish are eaten
        return None
