import random

class BeatThat:
    def __init__(self):
        self.scores = [0, 0]
        self.current_player = 0

    def roll_dice(self):
        return random.randint(1, 6), random.randint(1, 6)

    def concatenate_roll(self, dice1, dice2):
        if dice1 > dice2:
            return dice1 * 10 + dice2
        elif dice2 > dice1:
            return dice2 * 10 + dice1
        else:
            return dice1 * 10 + dice2

    def play_round(self):
        player_scores = []
        for player in range(2):
            input(f"Player {player + 1}, press Enter or type 'roll' to roll the dice: ")
            dice1, dice2 = self.roll_dice()
            score = self.concatenate_roll(dice1, dice2)
            player_scores.append(score)
            print(f"Player {player + 1} rolled {dice1} and {dice2} -> Score: {score}")
        return player_scores

    def update_scores(self, player_scores):
        if player_scores[0] > player_scores[1]:
            self.scores[0] += player_scores[0]
        elif player_scores[1] > player_scores[0]:
            self.scores[1] += player_scores[1]
        # No points are added in case of a tie

    def play_game(self):
        while max(self.scores) < 100:
            player_scores = self.play_round()
            self.update_scores(player_scores)
            print(f"Scores after this round: {self.scores}")
        winner = self.scores.index(max(self.scores)) + 1
        print(f"Player {winner} wins the game with {self.scores[winner - 1]} points!")

if __name__ == "__main__":
    game = BeatThat()
    game.play_game()