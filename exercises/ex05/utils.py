"""implement some more list utility functions."""

__author__ = "730763981"


def only_evens(nums: list[int]) -> list:
    """makes a new list of only even numbers from input list.
    args: nums: list of ints
    returns: evens: list of even ints
    """

    # can't call the var list
    evens: list[int] = []
    for x in nums:
        if x % 2 == 0:
            evens.append(x)
    return evens


def sub(nums: list[int], start: int, end: int) -> list:
    """generate a list which is a subset of the input list, between the specified start index and the end index.
    args: nums: list input
        start: start index
        end: end index (non inclusive)
    returns: shorter: subset of list
    """

    if start < 0:
        start = 0
    if end > len(nums):
        end = len(nums)
    # above if statement below
    shorter: list[int] = []
    if len(nums) == 0 or start >= len(nums) or end <= 0:
        return shorter
    for i in range(start, end):
        shorter.append(nums[i])
    return shorter


def add_at_index(nums: list[int], new: int, i: int) -> None:
    """modify the input list to place the element at the given index.
    args: nums: input list
        new: new element
        i: index for new
    returns: None
    """

    if i > len(nums) or i < 0:
        raise IndexError("Index is out of bounds for the input list")

    # makes a spot at end of list
    nums.append(0)
    # shifts everything after i back one
    for n in range(len(nums) - 1, i, -1):
        nums[n] = nums[n - 1]
    nums[i] = new
    print(nums)
    # need to return 'None'
    """# prevents 'None' from printing in terminal
    exit()"""

    # ignore (try 2)
    """front: list[int] = sub(nums, 0, i)
    back: list[int] = sub(nums, i, len(nums))
    print(front)
    print(back)"""

    # doesn't mutate its input list and requires return type list
    """front: list[int] = sub(nums, 0, i)
    front.append(new)
    for x in range(i, len(nums)):
        front.append(nums[x])
    return front"""
