"""EX02 - Chardle - A small step toward Wordle"""

__author__ = "730763981"


def input_word() -> str:
    """
    function: gets user's word and checks for valid length
    args: None
    returns: user_word: user's input word
    """

    user_word: str = input("Enter a 5-character word: ")

    if len(user_word) == 5:
        return user_word
    else:
        print("Error: Word must contain 5 characters.")
        exit()


def input_letter() -> str:
    """
    function: gets user's letter guess and checks for valid length
    args: None
    returns: user_letter: user's input letter
    """

    user_letter: str = input("Enter a single character: ")
    if len(user_letter) == 1:
        return user_letter

    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    """
    function: searches for letter appearances in word
        also prints count of appearances
    args: word: input word
        letter: input letter
    returns: none
    """

    print(f"Searching for {letter} in {word}")
    # count goes up here
    count: int = 0
    # each one checks for matches
    if word[0] == letter:
        print(f"{letter} found at index 0")
        count += 1
    if word[1] == letter:
        print(f"{letter} found at index 1")
        count += 1
    if word[2] == letter:
        print(f"{letter} found at index 2")
        count += 1
    if word[3] == letter:
        print(f"{letter} found at index 3")
        count += 1
    if word[4] == letter:
        print(f"{letter} found at index 4")
        count += 1
    # count print statements
    if count == 0:
        print(f"No instances of {letter} found in {word}")
    # have to de-pluralize if only 1
    if count == 1:
        print(f"1 instance of {letter} found in {word}")
    if count != 0 and count != 1:
        print(f"{count} instances of {letter} found in {word}")


def main() -> None:

    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
