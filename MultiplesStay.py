import random
from collections import Counter

class MultiplesStay:
    def __init__(self):
        self.dice = 10
        self.current_player = 0
        self.last_successful_player = None

    def roll_dice(self, num_dice):
        return sorted([random.randint(1, 6) for _ in range(num_dice)])

    def remove_multiples(self, rolls):
        counts = Counter(rolls)
        multiples = {num: count for num, count in counts.items() if count > 1}
        if not multiples:
            return 0, None
        if len(multiples) > 1:
            print(f"Multiple multiples found: {multiples}")
            choice = int(input(f"Player {self.current_player + 1}, choose a number to remove: "))
            return multiples[choice], choice
        max_multiple = max(multiples, key=multiples.get)
        return multiples[max_multiple], max_multiple

    def play_round(self):
        input(f"Player {self.current_player + 1}, press Enter or type 'roll' to roll the dice: ")
        rolls = self.roll_dice(self.dice)
        print(f"Player {self.current_player + 1} rolled: {rolls}")
        removed, number = self.remove_multiples(rolls)
        if removed > 0:
            self.dice -= removed
            self.last_successful_player = self.current_player
            print(f"Player {self.current_player + 1} removed {removed} dice of number {number}.")
        else:
            print(f"Player {self.current_player + 1} could not remove any dice.")
        return removed

    def play_game(self):
        while self.dice > 1:
            removed = self.play_round()
            if removed == 0:
                print(f"Player {self.current_player + 1} could not roll multiples. Game over!")
                break
            self.current_player = 1 - self.current_player
        winner = self.last_successful_player + 1
        print(f"Player {winner} wins the game!")

if __name__ == "__main__":
    game = MultiplesStay()
    game.play_game()