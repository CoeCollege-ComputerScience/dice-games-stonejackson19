import random
from collections import Counter

def roll_dice(num_dice):
    return sorted([random.randint(1, 6) for _ in range(num_dice)])

def remove_multiples(rolls):
    counts = Counter(rolls)
    multiples = {num: count for num, count in counts.items() if count > 1}
    if not multiples:
        return 0, None
    if len(multiples) > 1:
        print(f"Multiple multiples found: {multiples}")
        choice = int(input(f"Choose a number to remove: "))
        return multiples[choice], choice
    max_multiple = max(multiples, key=multiples.get)
    return multiples[max_multiple], max_multiple

def play_round(current_player, dice):
    input(f"Player {current_player + 1}, press Enter or type 'roll' to roll the dice: ")
    rolls = roll_dice(dice)
    print(f"Player {current_player + 1} rolled: {rolls}")
    removed, number = remove_multiples(rolls)
    if removed > 0:
        dice -= removed
        print(f"Player {current_player + 1} removed {removed} dice of number {number}.")
    else:
        print(f"Player {current_player + 1} could not remove any dice.")
    return dice, removed > 0

def play_game():
    dice = 10
    current_player = 0
    while dice > 1:
        dice, successful = play_round(current_player, dice)
        if not successful:
            print(f"Player {current_player + 1} could not roll multiples. Game over!")
            winner = 2 - current_player
            print(f"Player {winner} wins the game!")
            return
        current_player = 1 - current_player
    winner = current_player + 1
    print(f"Player {winner} wins the game!")

if __name__ == "__main__":
    play_game()