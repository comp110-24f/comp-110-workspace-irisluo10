"""tests for utils.py."""

__author__ = "730763981"

from exercises.ex05.utils import only_evens, sub, add_at_index


# tests for add_at_index
def test_add_at_index_UC_normal() -> None:
    """add_at_index use case for what it should return."""
    l: list[int] = [1, 2, 3, 4, 6, 7, 4, 3]
    # no return value
    assert add_at_index(l, 3, 6) is None


def test_add_at_index_UC_mutation() -> None:
    """add_at_index use case for mutation."""
    l: list[int] = [1, 2, 3, 4, 6, 7, 4, 3]
    add_at_index(l, 3, 6)
    assert l == [1, 2, 3, 4, 6, 7, 3, 4, 3]


def test_add_at_index_EC() -> None:
    """add_at_index edge case for if list is empty and value added to index 0."""
    l: list[int] = []
    add_at_index(l, 3, 0)
    assert l == [3]


# tests for sub
def test_sub_UC_normal() -> None:
    """sub use case for what it should return."""
    l: list[int] = [1, 2, 3, 4, 6, 7, 4, 3]
    assert sub(l, 3, 6) == [4, 6, 7]


def test_sub_UC_mutate() -> None:
    """sub use case for mutation (should not mutate list)."""
    l: list[int] = [1, 2, 3, 4, 6, 7, 4, 3]
    sub(l, 3, 6)
    assert l == [1, 2, 3, 4, 6, 7, 4, 3]


def test_sub_EC() -> None:
    """sub edge case testing for if start is greater length of the list"""
    l: list[int] = [1, 2, 3, 4, 6, 7, 4, 3]
    assert sub(l, 9, 6) == []


# tests for only_evens
def test_OE_UC_normal() -> None:
    """only_evens use case for what it should return."""
    l: list[int] = [1, 2, 3, 4, 6, 7, 4, 3]
    assert only_evens(l) == [2, 4, 6, 4]


def test_OE_UC_mutate() -> None:
    """only_evens use case for mutation (should not mutate list)."""
    l: list[int] = [1, 2, 3, 4, 6, 7, 4, 3]
    # calls function
    only_evens(l)
    # checks that list was not mutated
    assert l == [1, 2, 3, 4, 6, 7, 4, 3]


def test_OE_EC() -> None:
    """only_evens edge case testing for empty list input"""
    l: list[int] = []
    assert only_evens(l) == []
