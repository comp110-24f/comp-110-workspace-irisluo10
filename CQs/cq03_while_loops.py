"""while loop to iterate over a string"""

__author__ = "730763981"


def num_instances(phrase: str, search_char: str) -> int:
    """
    purpose: while loop to iterate over a string
    args: phrase: phrase to search
        search_char: char to search for
    returns: num of times char is in str
    """
    # count and index vars
    count: int = 0
    index: int = 0

    # iterates through each char in the str
    while index < len(phrase):
        # searches for match
        if search_char == phrase[index]:
            # adds to count
            count += 1
        # adds to index
        index += 1

    return count
