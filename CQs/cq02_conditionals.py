"""number guessing game"""

__author__ = "730763981"


def guess_a_number() -> None:
    """
    function: makes a number guessing game
    args: none
    returns: none
    """
    secret: int = 7
    # need to put exactly what's on the directions.
    guess: str = input("Guess a number: ")
    print("Your guess was", guess + ".")

    if int(guess) == secret:
        print("You got it!")
    elif int(guess) < secret:
        print("Your guess was too low! The secret number is", str(secret))
    else:
        print("Your guess was too high! The secret number is", str(secret))

    return None


if __name__ == "__main__":
    guess_a_number()
