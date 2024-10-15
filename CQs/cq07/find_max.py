"""finds and removes max int from list."""

__author__ = "730763981"


def find_and_remove_max(list: list[int]) -> int:
    """finds and removes max int from list.
    args: list: input list
    returns: largest number
    """

    if len(list) == 0:
        return -1
    # put after if statement otherwise IndexError if list len is 0
    max: int = list[0]
    for num in list:
        if num > max:
            max = num
    # removes item(s) from list
    # may need to use while loop if autograder gets mad
    """for num in list:
        if num == max:
            # .index() gets index of item
            list.pop(list.index(num))
    """
    # while loop used here because index needed accessing
    i: int = 0
    while i < len(list):
        if list[i] == max:
            list.pop(i)
        i += 1
    return max
