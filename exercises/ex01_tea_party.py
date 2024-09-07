"""This function calculates the quantity of tea 
bags needed, the number of treats to accompany 
the tea, and the expected cost of the party for 
user input number of guests"""

__author__ = "730763981"


def main_planner(guests: int) -> None:
    """main function to do tasks"""

    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


def tea_bags(people: int) -> int:
    """determines # of tea bags needed"""

    return people * 2


def treats(people: int) -> int:
    """determines # of treats needed"""

    # people will equal # of people at party
    # can just use people in return
    # instructions asked for 1.5 treats per TEA, not per PERSON
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """determines cost"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
