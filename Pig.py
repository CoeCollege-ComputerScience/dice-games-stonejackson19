import random

class Pig:
    def __init__(self):
        self.scores = [0, 0]
        self.current_player = 0
        self.turn_total = 0

    def roll_die(self):
        return random.randint(1, 6)

    def play_turn(self):
        while True:
            choice = input(f"Player {self.current_player + 1}, press Enter to roll or type 'hold' to hold: ").strip().lower()
            if choice == 'hold':
                self.scores[self.current_player] += self.turn_total
                print(f"Player {self.current_player + 1} holds. Total score: {self.scores[self.current_player]}")
                self.turn_total = 0
                self.current_player = 1 - self.current_player
                break
            else:
                roll = self.roll_die()
                print(f"Player {self.current_player + 1} rolled a {roll}")
                if roll == 1:
                    print(f"Player {self.current_player + 1} rolled a 1 and loses the turn total.")
                    self.turn_total = 0
                    self.current_player = 1 - self.current_player
                    break
                else:
                    self.turn_total += roll
                    print(f"Player {self.current_player + 1}'s turn total is now {self.turn_total}")
                    if self.scores[self.current_player] + self.turn_total >= 100:
                        self.scores[self.current_player] += self.turn_total
                        print(f"Player {self.current_player + 1} wins the game with {self.scores[self.current_player]} points!")
                        return True
        return False

    def play_game(self):
        while max(self.scores) < 100:
            if self.play_turn():
                break
            print(f"Scores: Player 1 - {self.scores[0]}, Player 2 - {self.scores[1]}")
        else:
            winner = f"Player {self.scores.index(max(self.scores)) + 1} wins the game!"
            print(winner)

if __name__ == "__main__":
    game = Pig()
    game.play_game()