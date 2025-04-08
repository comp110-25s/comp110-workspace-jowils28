"""File to define River class."""

__author__: str = "730774862"

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    """New class River"""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())
        return None

    def check_ages(self):
        """Remove bears and fish that are too old"""
        new_fish: list[Fish] = []
        new_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)  # adds fish that are not too old
        for bears in self.bears:
            if bears.age <= 5:
                new_bears.append(bears)  # adds bears that are not too old
        self.fish = new_fish  # sets original list to new one with young fish
        self.bears = new_bears  # sets original id to new id with young bears
        return None

    def remove_fish(self, amount: int):
        """Removes front fish from the fish list"""
        new_fish: list[Fish] = []
        for _ in range(amount, len(self.fish)):
            new_fish.append(self.fish[_])
        self.fish = new_fish
        return None

    def bears_eating(self):
        """Bears can eat if there are more than 5 fish"""
        index: int = 0
        while len(self.fish) >= 5:  # bear will eat 3 fish until there is not 5
            self.bears[index].eat(3)
            self.remove_fish(3)  # removes 3 fish because 3 were eaten
            index += 1
        return None

    def check_hunger(self):
        """Checks the hunger levels of bears and removes starved bears"""
        full_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                full_bears.append(bear)  # adds bears with hunger score above 0
        self.bears = full_bears  # set original id to new id
        return None

    def repopulate_fish(self):
        """Reproducing fish"""
        new_fish_amount: int = (len(self.fish) // 2) * 4  # 4 fish born per pair
        for _ in range(len(self.fish), (len(self.fish) + new_fish_amount)):
            self.fish.append(Fish())  # adds new baby fish
        return None

    def repopulate_bears(self):
        """Reproducing bears"""
        new_bears_amount: int = len(self.bears) // 2  # 1 bear born per pair
        for _ in range(len(self.bears), (len(self.bears) + new_bears_amount)):
            self.bears.append(Bear())  # adds baby bear
        return None

    def view_river(self):
        """Shows count of river days, fish, and bears"""
        print(f"~~~ Day {str(self.day)}: ~~~")
        print(f"Fish population: {str(len(self.fish))}")
        print(f"Bear population: {str(len(self.bears))}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """One week of life in the river"""
        for _ in range(0, 7):  # runs through one day seven times
            self.one_river_day()
        return None
