# William Starks
# proj6.py
# 4/12/2025
# Rock Paper Scissors game

import random

ROCK = 0
PAPER = 1
SCISSORS = 2

def main(): # The actual game
    random.seed(164) #I could not replicate the sample output with seed 451, I'm not sure why.
    name = introduction()

    total_games = 0
    user_wins = 0
    comp_wins = 0
    ties = 0

    user_move = get_user_play()

    while user_move != -1:
        comp_move = get_computer_play()

        if user_move == 0:
            user_play = "Rock"
        elif user_move == 1:
            user_play = "Paper"
        else:
            user_play = "Scissors"

        if comp_move == 0:
            comp_play = "Rock"
        elif comp_move == 1:
            comp_play = "Paper"
        else:
            comp_play = "Scissors"

        print(f"{name} plays {user_play} computer plays {comp_play}")

        if user_move == comp_move:
            print("It's a tie!\n")
            ties += 1
        elif user_move == ROCK and comp_move == SCISSORS:
            print("Rock breaks scissors. CSC1170 wins!\n")
            user_wins += 1
        elif user_move == PAPER and comp_move == ROCK:
            print("Paper covers rock. CSC1170 wins!\n")
            user_wins += 1
        elif user_move == SCISSORS and comp_move == PAPER:
            print("Scissors cuts paper. CSC1170 wins!\n")
            user_wins += 1
        elif comp_move == ROCK and user_move == SCISSORS:
            print("Rock breaks scissors. Computer wins!\n")
            comp_wins += 1
        elif comp_move == PAPER and user_move == ROCK:
            print("Paper covers rock. Computer wins!\n")
            comp_wins += 1
        elif comp_move == SCISSORS and user_move == PAPER:
            print("Scissors cuts paper. Computer wins!\n")
            comp_wins += 1

        total_games += 1
        user_move = get_user_play()

    print_statistics(total_games, user_wins, comp_wins, ties, name)

def introduction(): #Gets user's name and introduces the user
    print("Welcome to the game Rock, Paper, Scissors.  You will be playing against the computer.")
    name = str(input("What is your name? "))
    print(f"Here are the rules {name}:")
    print("If a player chooses Rock and the other chooses Scissors, Rock wins.")
    print("If a player chooses Scissors and the other chooses Paper, Scissors wins.")
    print("If a player chooses Paper and the other chooses Rock, Paper wins.")
    print("If both players make the same choice, it's a tie.")
    print("Enter -1 to quit the game\n")
    return name

def get_user_play(): #Gets user's choice for the game
    user_input = int(input("Enter your move (0 for Rock, 1 for Paper, 2 for Scissors): "))
    return user_input

def get_computer_play(): #Gets computers choice for the game
    randnum = random.uniform(0, 1)
    if randnum < 0.25:
        return ROCK
    elif randnum < 0.65:
        return PAPER
    else:
        return SCISSORS

def print_statistics(total, user_wins, comp_wins, ties, name): #States final stats once game is over
    print(f"There were {total} games: {name} won {user_wins} games, the computer won {comp_wins} games, and there were {ties} ties.")

main()
