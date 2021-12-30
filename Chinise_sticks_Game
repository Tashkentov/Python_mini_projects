print("Choose number of sticks : 10, 20, 30, 40 or 50")

number_sticks = int(input())
print("Enter name of first player")
name1 = input()
print("Enter name of second player")
name2 = input()
player_turn = name1

def can_take(sticks):
    return sticks >= 1 and sticks <= 3

def switch_player(turn):
    return name1 if player_turn == name2 else name2

def end_game(sticks):
    return sticks <=0

while not end_game(number_sticks):
    print(f" {player_turn} take you sticks. Remaining {number_sticks}")
    taken = int(input())

    if not can_take(taken):
        print("Please, take 1,2 or 3 sticks.")
        continue

    number_sticks -= taken
    print(f"{taken} sticks taken. \n")

    if end_game(number_sticks):
        print(f"No more stiiiiicks in game. \n - Player {player_turn} has lost :'( ")
        break
    player_turn = switch_player(player_turn)
