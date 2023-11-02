# Made by Piotr Zięba on 01.11.2023.
# Game's name is "Higher or lower". Today's class is the last from the beginner's series.
# Teacher's version checks popularity but to make my version valid for longer I will use people's age.

import random
from art import logo, vs
from game_data import famous

# To-Do List
# 1. Display logos and a pre-selected question to start the game.
# 2. Create a list to store available questions/options about famous people/description.
# 3. Implement the game logic:
#    a. Players select option A or B.
#    b. Compare the selected options and determine if the answer is correct or wrong.
#    c. If the answer is correct, increment the player's score and present a new question.
#    d. If the answer is wrong, end the game and display the player's score.
# 4. After finishing the game, provide an option to restart.


def high_low_game(age, random_a, random_b, points):
    """Game logic. Checks user's choice and allows him to play more with each right answer,
     but ends the game once it finds a mistake."""
    while True:   # Game goes in a loop as long as the user gives good answers.
        if (random_a['age'] > random_b['age']) and (age == "a"):    # Scenario for A.
            points += 1   # Right answers increment points.
            random_a = random_b   # Here we switch b to a. Later we assign a new option for b.
            random_b = random.choice(famous)
            if random_a == random_b:   # Checks for repetition.
                random_b = random.choice(famous)
        elif (random_a['age'] < random_b['age']) and (age == "b"):   # Scenario for B.
            points += 1
            random_a = random_b
            random_b = random.choice(famous)
            if random_a == random_b:
                random_b = random.choice(famous)
        else:    # In case of a wrong answer else statement ends the game.
            if points == 1:    # Fix for 1 point / 2 points.
                return print(f"You're wrong. You've got {points} point. Game over!")
            else:
                return print(f"You're wrong. You've got {points} points. Game over!")
        print("-------------------------------------------------------------------------------------------------------")
        print(logo)  # Starting screen again with slight changes. Instead of rules we have information about the score.
        print(f"Compare A: {random_a['name']}, {random_a['job']}, from {random_a['country']}.")
        print(vs)
        print(f"Compare B: {random_b['name']}, {random_b['job']}, from {random_b['country']}.")
        if points == 1:
            print(f"Your current score is: {points} point.")
        else:
            print(f"Your current score is: {points} points.")
        age = input("Select option 'A' or 'B': ").lower()  # User's answer.


choice = "y"
while choice == "y":    # Loop for restarting the game.
    random_pick_a = random.choice(famous)  # Randomly selected number.
    random_pick_b = random.choice(famous)
    if random_pick_a == random_pick_b:    # checks for repetition.
        random_pick_b = random.choice(famous)
    starting_points = 0
    print("-------------------------------------------------------------------------------------------------------")
    print(logo)  # Starting screen.
    print(f"Compare A: {random_pick_a['name']}, {random_pick_a['job']}, from {random_pick_a['country']}.")
    print(vs)
    print(f"Compare B: {random_pick_b['name']}, {random_pick_b['job']}, from {random_pick_b['country']}.")
    print("Rules: You must choose either an individual who is older, or a company.")
    higher_age = input("Select option 'A' or 'B': ").lower()  # User's answer.
    high_low_game(higher_age, random_pick_a, random_pick_b, starting_points)  # Function for the game logic.
    choice = input("Do you want to play again? y or n")
