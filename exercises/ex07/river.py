"""File to define River class."""

__author__ = "730763981"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """New River."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove dead animals."""
        # new lists
        living_fish: list[Fish] = []
        living_bears: list[Bear] = []
        for f in self.fish:
            if not f.age > 3:
                living_fish.append(f)
        for b in self.bears:
            if not b.age > 5:
                living_bears.append(b)
        # setting old lists equal to new
        self.fish = living_fish
        self.bears = living_bears
        return None

    def bears_eating(self):
        """Makes bears eat fish."""
        for b in self.bears:
            if len(self.fish) >= 5:
                b.eat(3)
                # can have this above remove_fish function def.
                self.remove_fish(3)

        return None

    def check_hunger(self):
        """Kills hungry bears."""
        # new list
        living_bears: list[Bear] = []
        for b in self.bears:
            if not b.hunger_score < 0:
                living_bears.append(b)
        # setting old list equal to new
        self.bears = living_bears
        return None

    def repopulate_fish(self):
        """Adds new fish for each pair."""
        for i in range(0, len(self.fish) // 2):
            times: int = 0
            while times < 4:
                self.fish.append(Fish())
                times += 1
        return None

    def repopulate_bears(self):
        """Adds new bear for each pair."""
        # // divides and rounds down
        for i in range(0, len(self.bears) // 2):
            self.bears.append(Bear())

        return None

    def view_river(self):
        """Prints river contents."""
        print(f"~~~ Day {self.day}: ~~~")
        fish_count: int = len(self.fish)
        bear_count: int = len(self.bears)
        print(f"Fish population: {fish_count}")
        print(f"Bear population: {bear_count}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates a week at the river."""
        # new var to track how many days pass
        week_later: int = self.day + 7
        # adds a day seven times
        while self.day < week_later:
            for bear in self.bears:
                bear.one_day()
            for fish in self.fish:
                fish.one_day()
            self.day += 1

    def remove_fish(self, amount: int) -> None:
        """Remove specified # fish from river."""
        for i in range(0, amount):
            self.fish.pop(i)
