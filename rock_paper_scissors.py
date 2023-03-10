import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

points_of_player = 0
points_of_computer = 0
draws = 0

how_many_games = int(input("How many games you wanna play? "))

for game in range(how_many_games):
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock

    elif player_move == "p":
        player_move = paper

    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Your choice is invalid. Try again...")

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        points_of_player += 1
        print("You score a point!")
    elif (player_move == rock and computer_move == paper) or \
            (player_move == paper and computer_move == scissors) or \
            (player_move == scissors and computer_move == rock):
        points_of_computer += 1
        print("I'm sorry, but you lose that point!")
    else:
        draws += 1
        print("Draw!")

if points_of_player > points_of_computer:
    print("Congratulations! You won!")
elif points_of_player < points_of_computer:
    print("I'm really sorry, but you lost!")
else:
    print("Amazing! It's a draw!")