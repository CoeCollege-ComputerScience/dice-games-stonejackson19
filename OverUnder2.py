import random

def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]

def play_round(current_player, scores, benchmark):
    if benchmark is None:
        input(f"Player {current_player + 1}, press Enter or type 'roll' to roll the dice: ")
        player1_roll = roll_dice()
        benchmark = sum(player1_roll)
        print(f"Player {current_player + 1} rolled {player1_roll} -> Total: {benchmark}")
        return 1 - current_player, scores, benchmark

    guess = input(f"Player {current_player + 1}, guess 'Over' or 'Under' against {benchmark}: ").strip().lower()
    input(f"Player {current_player + 1}, press Enter or type 'roll' to roll the dice: ")
    player_roll = roll_dice()
    player_total = sum(player_roll)
    print(f"Player {current_player + 1} rolled {player_roll} -> Total: {player_total}")

    if (guess == 'over' and player_total > benchmark) or (guess == 'under' and player_total < benchmark):
        print(f"Player {current_player + 1} wins this round!")
        scores[current_player] += 1
    else:
        print(f"Player {2 - current_player} wins this round!")
        scores[1 - current_player] += 1

    return 1 - current_player, scores, player_total

def play_game():
    scores = [0, 0]
    current_player = 0
    benchmark = None
    while max(scores) < 6:
        current_player, scores, benchmark = play_round(current_player, scores, benchmark)
        print(f"Scores: Player 1 - {scores[0]}, Player 2 - {scores[1]}")
    winner = f"Player {scores.index(max(scores)) + 1} wins the game!"
    print(winner)

if __name__ == "__main__":
    play_game()