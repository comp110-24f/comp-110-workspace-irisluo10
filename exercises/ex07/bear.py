"""File to define Bear class."""


class Bear:
    """New Bear."""

    def __init__(self):
        """Initialize new bear w/ age and hunger."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Adds 1 to age and minus 1 from hunger."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Makes the bear eat fish."""
        self.hunger_score += num_fish
