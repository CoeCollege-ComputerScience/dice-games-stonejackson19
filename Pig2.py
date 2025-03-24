import random

def roll_die():
    return random.randint(1, 6)

def play_turn(player, scores):
    turn_total = 0
    while True:
        choice = input(f"Player {player + 1}, press Enter to roll or type 'hold' to hold: ").strip().lower()
        if choice == 'hold':
            scores[player] += turn_total
            print(f"Player {player + 1} holds. Total score: {scores[player]}")
            return
        else:
            roll = roll_die()
            print(f"Player {player + 1} rolled a {roll}")
            if roll == 1:
                print(f"Player {player + 1} rolled a 1 and loses the turn total.")
                return
            else:
                turn_total += roll
                print(f"Player {player + 1}'s turn total is now {turn_total}")
                if scores[player] + turn_total >= 100:
                    scores[player] += turn_total
                    print(f"Player {player + 1} wins the game with {scores[player]} points!")
                    return
                
def play_game():
    scores = [0, 0]
    player = 0
    while max(scores) < 30:
        play_turn(player, scores)
        player = 1 - player
        print(f"Scores: Player 1 - {scores[0]}, Player 2 - {scores[1]}")
    else:
        winner = f"Player {scores.index(max(scores)) + 1} wins the game!"
        print(winner)

if __name__ == "__main__":
    play_game()