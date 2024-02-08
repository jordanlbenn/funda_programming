# Jordan Bennett
# Fundamentals of Programming - Week 5 Homework

# Write a program that takes a digit as an input and returns the corresponding word.

list1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

num = int(input('Enter a digit between 0 and 9: '))
print(int(num))

dict1 = {  # This method, assigns the input to the string version of the number
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

print(dict1.get(num))

# ROCK, PAPER, SCISSOR GAME
import random

rand_num = random.random()  # generates a random number between 0 and 1
print(round(rand_num, 2))

import random  # defines a series of functions for generating or manipulating random integers

user_move = input('Pick a move - rock/paper/scissors: ')  # prompts the user, to type in one of the choices
rand_num = round(random.random(), 2)
comp_move = ''

if rand_num >= 0 and rand_num < 1 / 3:  # assigns the number, to one of the three choices.
    comp_move = 'rock'
elif rand_num >= 1 / 3 and rand_num < 2 / 3:
    comp_move = 'paper'
else:
    comp_move = 'scissors'

result = ''
if user_move == comp_move:  # if the user and computer's choices match, then the result will print 'Tie'
    result = 'Tie.'

elif user_move == 'rock':
    if comp_move == 'paper':
        result = 'You lose!'
    else:
        result = 'You win!'

elif user_move == 'paper':
    if comp_move == 'rock':
        result = 'You win!'
    else:
        result = 'You lose!'

elif user_move == 'scissors':
    if comp_move == 'rock':
        result = 'You lose!'
    else:
        result = 'You win!'

print(f'You picked {user_move}. Computer picked {comp_move}. {result}')

# Write a program that simulates that logic shown in the chart

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input(
    'You are at a cross road. Where do you want to go? "left" or "right" ').lower()  # This method here, returns the
# loweredcased strings from the given string by converting each uppercase character to lowercase, so it doesn't
# matter how the user inputs it.
if choice1 == "left":
    choice2 = input(
        'You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type '
        '"swim" to swim across.').lower()
    if choice2 == "wait":
        choice3 = input(
            "You arrive at the island safe. There is a building with 3 doors. One red, one yellow and one blue. Which "
            "colour do you choose?").lower()
        if choice3 == "red":
            print("You have been burned by the fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You were eaten by beats. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
