"""This function calculates the quantity of tea 
bags needed, the number of treats to accompany 
the tea, and the expected cost of the party for 
user input number of guests"""

__author__ = "730763981"


def main_planner(guests: int) -> None:
    """
    function: main function to do tasks
    args: guests [int] to show number of guests present
    returns: None
    """

    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """
    function: determines # of tea bags needed
    args: people [int]: # of people attending party
    returns: people * 2 [int] because each person needs 2 tea bags
    """

    return people * 2


def treats(people: int) -> int:
    """
    function: determines # of treats needed
    args: people [int]: # of people attending party
    returns: int(tea_bags(people=people) * 1.5) [int]
        because each person needs 1.5 treats per tea bag (2/person)
    """

    # people will equal # of people at party
    # can just use people in return
    # instructions asked for 1.5 treats per TEA, not per PERSON
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """
    function: determines cost
    args: tea_count [int]: number of tea bags
        treat_count [int]: number of treats
    returns: tea_count * 0.5 + treat_count * 0.75 [float]:
        cost of tea bags and treats added together
    """
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
