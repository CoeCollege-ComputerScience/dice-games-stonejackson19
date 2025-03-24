import random

def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]

def add_roll(die1, die2):
    if die1 > die2:
        return die1 * 10 + die2
    elif die2 > die1:
        return die2 * 10 + die1
    else:
        return die1 * 10 + die2
    
def play_round():   
    player_scores = []
    for player in range(2):
        input(f"Player {player + 1}, press Enter or type 'roll' to roll the dice: ")
        dice = roll_dice()
        score = add_roll(dice[0], dice[1])
        player_scores.append(score)
        print(f"Player {player + 1} rolled {dice[0]} and {dice[1]} -> Score: {score}")
    return player_scores

def update_scores(scores, player_scores):
    if player_scores[0] > player_scores[1]:
        scores[0] += player_scores[0]
    elif player_scores[1] > player_scores[0]:
        scores[1] += player_scores[1]

def play_game():
    scores = [0,0]
    while max(scores) < 100:
        player_scores = play_round()
        update_scores(scores, player_scores)
        print(f"Scores after this round: {scores}")
    winner = scores.index(max(scores)) + 1
    print(f"Player {winner} wins the game with {scores[winner - 1]} points!")

if __name__ == "__main__":
    play_game()