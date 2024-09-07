__author__ = "730763981"


def mimic(message: str) -> str:
    """This function takes input and repeats it back"""

    return message


def main() -> None:
    "print result of calling mimic function"

    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    """runs in 'Run' but not in 'Interact'"""
    main()
