"""File to define Fish class."""


class Fish:
    """New Fish."""

    def __init__(self):
        """Initialize fish w/ age."""
        self.age = 0
        return None

    def one_day(self):
        """Add 1 to age."""
        self.age += 1
        return None
