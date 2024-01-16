import random
import numpy as np


# Declaring the player class (aka gamemaster)
class Player:
    guesses = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    table = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    winning_arrays = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    computer_guesses = []
    user_guesses = []

    # Welcome screen
    def __init__(self):
        print("Welcome, you are the x and the computer is the o")

    # Game winner announcement
    def win_game(self, winner):
        if winner == "Computer":
            print("Sorry, you lost") 
        else:
            print("Yay! You won")

    # print table
    def check_table(self):
        i=0
        if i<2:
            print(self.table[i], "|", self.table[i+1], "|", self.table[i+2])
            i=3
        if i<5:
            print(self.table[i], "|", self.table[i+1], "|", self.table[i+2])
            i=6
        if i<8:
            print(self.table[i], "|", self.table[i+1], "|", self.table[i+2])
            i=8


# The computer that the player will play against
class Computer(Player): 
    computer_current_guess = 0

    def computers_turn(self):
        super()
        self.computer_current_guess = random.choice(self.guesses)
        self.computer_guesses.append(self.computer_current_guess)
        self.guesses.remove(self.computer_current_guess)
        self.table[self.computer_current_guess] = "o"


# The player
class User(Player):
    user_current_guess = 0

    def users_turn(self):
        while True:
            self.user_current_guess = int(input("Please enter where you want to place your token: "))
            super()

            if self.user_current_guess in self.guesses:
                self.user_guesses.append(self.user_current_guess)
                self.guesses.remove(self.user_current_guess)
                self.table[self.user_current_guess] = "x"
                break
            else:
                print("That not a valid position")
                print(self.user_current_guess)


# Function for checking if someone has won or not
def check_winner(winning_arrays_func, user_guesses_func, computer_guesses_func):
    for group in winning_arrays_func:
        winners = np.array(group)
        array_user = np.array(user_guesses_func)
        array_computer = np.array(computer_guesses_func)
        bool_user = np.isin(winners, array_user)
        bool_computer = np.isin(winners, array_computer)

        
        if bool_user.all() == True:
            player.win_game("User")
            return True

        if bool_computer.all() == True:
            player.win_game("Computer")
            return True


# initialising the classes 
computer = Computer()
user = User()
player = Player()


# Beginning the game
player.check_table()

while True:  
    # accessing classes for turns
    user.users_turn()
    computer.computers_turn()
    player.check_table()
    
    # checking for a winner
    if check_winner(player.winning_arrays, player.user_guesses, player.computer_guesses):
        break
    
