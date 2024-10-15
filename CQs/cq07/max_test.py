"""unit tests that test find_and_remove_max."""

__author__ = "730763981"

from CQs.cq07.find_max import find_and_remove_max


def test_success() -> None:
    """tests if returns the expected value."""
    a: list[int] = [20, 10, 8, 7, 10]
    assert find_and_remove_max(a) == 20


def test_mutate() -> None:
    """tests if mutates to give the expected value."""
    l: list[int] = [20, 10, 8, 7, 10]
    find_and_remove_max(l)
    # samme var name as above
    assert l == [10, 8, 7, 10]


def test_weird() -> None:
    """tests if returns the correct value in case of an unconventional input."""
    list = []
    assert find_and_remove_max(list) == -1
