"""Mutating functions."""

__author__ = "730763981"


def manual_append(list: list[int], num: int) -> None:
    """
    function: appends int to list of ints
    args: list: input list
        num: int to append
    returns: None
    """

    # don't need list = ...; can just do list.append()
    list.append(num)


def double(list: list[int]) -> None:
    i: int = 0
    while i < len(list):
        list[i] *= 2
        i += 1


list_1: list[int] = [1, 2, 3]
# if you set list_2 = list_1, it will change list_1 too
# must make copy?? .copy()
# point of assignment is to show both lists are the same
list_2: list[int] = list_1
double(list=list_2)
print(list_1)
print(list_2)
