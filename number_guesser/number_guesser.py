import random
import math

target = random.randint(1,10)
player_guess = input("Please pick a number between one and ten: ")


while True:
    if player_guess.isdigit():
        player_guess = int(player_guess)

        if target == player_guess:
            print("Correct, you win!")
            break

        elif player_guess > target:
            player_guess = input("wrong, try a lower number: ")
          
        elif player_guess < target:
            player_guess = input("wrong, try a higher number: ")
    else:
        print("you did not enter a valid number")
        player_guess = input("Please try again: ")

   



