"""Reverse engineering algorithms and abstractions w/ lists."""

__author__ = "730763981"


# 1st line of doc strings need to end in . apparently
# Add a blank line between the summary line and the detailed description
def all(list: list[int], num: int) -> bool:
    """function: indicates whether or not all the ints in the list are the same as the given int.

    args: list: list given
        num: int given
    returns: true/false value
    """
    # return False immediately if the list is empty
    if len(list) == 0:
        return False

    i: int = 0
    matches: int = 0

    while i < len(list):
        if list[i] == num:
            matches += 1
        i += 1

    if matches == len(list):
        return True
    else:
        return False


def max(list: list[int]) -> int:
    """function: max should return the largest int in a list.

    args: list: the list
    returns: largest int
    """
    # may have error here b/c preset to 0
    # changed to first element of the list so it can
    # handle any type of number, positive or negative
    large: int = list[0]
    i: int = 0

    # above issue solved here
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")

    while i < len(list):
        if list[i] > large:
            large = list[i]
        i += 1
    return large


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """funtion: return True if every element at every.
        index is equal in both lists

    args: list1: first list
        list2: second list
    returns: t/f value
    """
    i: int = 0
    matches: int = 0

    # accidentally made len(list1) != len(list1)
    # didn't change second list to list2...
    if len(list1) != len(list2):
        return False
    while i < len(list1):
        if list1[i] == list2[i]:
            matches += 1
        i += 1
    if matches == len(list1):
        return True
    else:
        return False


def extend(list1: list[int], list2: list[int]) -> None:
    """function: mutate the first list of int values by.
        appending the second lists values to the end

    args: list1: first list
        list2: second list
    returns: None
    """
    i: int = 0

    while i < len(list2):
        list1.append(list2[i])
        i += 1
    # have to print the list out
    print(list1)
