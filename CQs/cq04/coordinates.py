"""prints each char of an x and y coordinate"""

__author__ = "730763981"


def get_coords(xs: str, ys: str) -> None:
    """
    function: prints each char of an x and y coordinate
    args: xs: first coordinate
        ys: second coordinate
    returns: None
    """

    # x index
    x_i: int = 0
    x_print: str = ""
    y_print: str = ""

    while x_i < len(xs):
        x_print = xs[x_i]
        # y index needs to be here so it resets
        y_i: int = 0
        while y_i < len(ys):
            y_print = ys[y_i]
            print(f"({x_print}, {y_print})")
            y_i += 1
        x_i += 1
