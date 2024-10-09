"""Summing the elements of a list using different loops."""

__author__ = "730763981"


# ending first line of docstrings w/ .
def w_sum(vals: list[float]) -> float:
    """returns the sum of all elements of list using while loop.
    args: vals: list of floats
    returns: sum of nums
    """

    sum: float = 0
    i: int = 0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """returns the sum of all elements of list but using for loop.
    args: vals: list of floats
    returns: sum of nums
    """

    sum: float = 0
    for x in vals:
        sum += x
    return sum


def f_range_sum(vals: list[float]) -> float:
    """returns the sum of all elements of list but using for loop w/ range().
    args: vals: list of floats
    returns: sum of nums
    """

    sum: float = 0
    for i in range(0, len(vals)):
        # get index
        sum += vals[i]
    # forgot the return statement
    return sum
