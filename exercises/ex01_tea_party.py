"""Planning a cozy tea party by inputing number of guests to calculate the quantity of tea bags and treats needed, and the expected cost of the party"""

__author__: str = "730774862"


def main_planner(guests: int) -> None:
    """calls and produces printed money output depending on guests"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """give number of tea bags needed based on people attending"""
    return people * 2


def treats(people: int) -> int:
    "give number of treats needed based on people attending"
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """gives cost of teas and treats combined"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
