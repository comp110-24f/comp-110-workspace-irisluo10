"""Wordle game"""

__author__ = "730763981"


# not like regular wordle, where you cannot choose len of word
def input_guess(guess_len: int) -> str:
    """
    function: user to enters a guess and until they provide a
        guess of the length specified in the function parameter
    args: guess_len: len of word to guess
    returns: guess: user's guess
    """

    guess: str = input("Enter a 5 character word ")

    while guess_len != len(guess):
        guess = input(f"That wasn't {guess_len} chars! Try again: ")

    return guess


def contains_char(string: str, letter: str) -> bool:

    assert len(letter) == 1
    i: int = 0
    while i < len(string):
        if string[i] == letter:
            return True
        else:
            return False
