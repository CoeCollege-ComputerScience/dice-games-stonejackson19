import random

class OverUnder:
    def __init__(self):
        self.scores = [0, 0]
        self.current_player = 0
        self.benchmark = None

    def roll_dice(self):
        return [random.randint(1, 6) for _ in range(3)]

    def play_round(self):
        if self.benchmark is None:
            input(f"Player {self.current_player + 1}, press Enter or type 'roll' to roll the dice: ")
            player1_roll = self.roll_dice()
            self.benchmark = sum(player1_roll)
            print(f"Player {self.current_player + 1} rolled {player1_roll} -> Total: {self.benchmark}")
            self.current_player = 1 - self.current_player
            return

        guess = input(f"Player {self.current_player + 1}, guess 'Over' or 'Under' against {self.benchmark}: ").strip().lower()
        input(f"Player {self.current_player + 1}, press Enter or type 'roll' to roll the dice: ")
        player_roll = self.roll_dice()
        player_total = sum(player_roll)
        print(f"Player {self.current_player + 1} rolled {player_roll} -> Total: {player_total}")

        if (guess == 'over' and player_total > self.benchmark) or (guess == 'under' and player_total < self.benchmark):
            print(f"Player {self.current_player + 1} wins this round!")
            self.scores[self.current_player] += 1
        else:
            print(f"Player {2 - self.current_player} wins this round!")
            self.scores[1 - self.current_player] += 1

        self.benchmark = player_total

    def play_game(self):
        while max(self.scores) < 6:
            self.play_round()
            print(f"Scores: Player 1 - {self.scores[0]}, Player 2 - {self.scores[1]}")
        winner = f"Player {self.scores.index(max(self.scores)) + 1} wins the game!"
        print(winner)

if __name__ == "__main__":
    game = OverUnder()
    game.play_game()