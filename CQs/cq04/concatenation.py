"""concatenates 2 strings"""

__author__ = "730763981"


def concat(str1: str, str2: str) -> str:
    """
    function: concatenates 2 strings
    args: str1: first string
        str2: second string
    returns: concatenated string
    """

    return str1 + str2


word1: str = "happy"
word2: str = "tuesday"

# function call still occurs when concatentation.py file runs,
# but not when imported
if __name__ == "__main__":
    print(concat(word1, word2))
