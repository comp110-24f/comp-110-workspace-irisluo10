"""EX03 - Wordle game"""

__author__ = "730763981"


# not like regular wordle, where you cannot choose len of word
def input_guess(guess_len: int) -> str:
    """
    function: user enters a guess and until they provide a
        guess of the length specified in the function parameter
    args: guess_len: len of word to guess
    returns: guess: user's guess
    """

    guess: str = input(f"Enter a {guess_len} character word ")

    while guess_len != len(guess):
        guess = input(f"That wasn't {guess_len} chars! Try again: ")

    return guess


def contains_char(string: str, letter: str) -> bool:
    """
    function: checks if letter is in string (word)
    args: string: the word
        letter: the letter
    return: whether the letter is in the word or not
    """

    # assumption in our code (error raised if not found to be true)
    assert len(letter) == 1
    i: int = 0
    while i < len(string):
        if string[i] == letter:
            return True
        i += 1
    # make False return here so while loop iterates through all indexes
    return False


def emojified(guess: str, answer: str) -> str:
    """
    function: prints emojis based on if guess is correct
    args: guess: user's guess
        answer: actual answer
    returns: emoji string
    """

    # assume strings of equal length provided
    assert len(guess) == len(answer)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    boxes: str = ""
    while i < len(guess):
        if guess[i] == answer[i]:
            boxes = boxes + GREEN_BOX
            i += 1
        # instead of searching for __ in ___, use contains_char()
        elif contains_char(string=answer, letter=guess[i]):
            boxes = boxes + YELLOW_BOX
            i += 1
        else:
            boxes = boxes + WHITE_BOX
            i += 1
    # return goes down here so while loop iterates completely
    return boxes


def main(secret: str) -> None:
    """
    function: The entrypoint of the program and main game loop.
    args: secret: answer user is trying to guess
    returns: None
    """

    turn: int = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        # prompts user for a word guess
        # set guess_len equal to length of secret so any word can be
        # secret, not just a set length
        user_guess: str = input_guess(guess_len=len(secret))
        # prints emoji line
        print(emojified(guess=user_guess, answer=secret))
        turn += 1
        if secret == user_guess:
            print(f"You won in {turn}/6 turns!")
            # need to exit so code doesn't keep running
            exit()

    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
