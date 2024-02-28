#!/usr/bin/python3
"""class model that implements rock, paper ,scirrors game"""
import random
import time
class MyGame:

    def __init__(self):
        """initializatin process"""
        self.players_score = 0
        self.comps_score = 0
    
    def start_string(self):
    
        print('''WELCOME TO THE ROCK, PAPER ,SCIRRORS GAME!!
              These are the rules
              >>>rock vs paper => ROCK WIN'S
              >>>scirrors vs paper => SCIRRORS WIN'S
              >>>paper vs rock => PAPER WIN'S''')

    def player_input(self):
        """function that gets the player's input"""
        while True:
            user_input = str(input("\n\nchose your input \n>>>1:rock\n>>>2: paper\n>>>3:scirrors:\n>>>")).lower()
            if user_input in ["rock", "paper", "scirrors"]:
                return user_input
            else:
                print("invalid choice")
    
    def comp_input(self):
        """defines the computers input"""
        comp_data = random.randint(1,3)
        return "rock" if comp_data == 1 else("paper" if comp_data == 2 else "scirrors")
    
    def winner(self, user_choice, comp_choice):
        """function that defines the winner"""
        if user_choice == comp_choice:
            return ("It's a draw!!\n")
        elif (user_choice == "rock" and comp_choice == "scirrors") or \
             (user_choice == "scirrors" and comp_choice == "paper") or \
             (user_choice == "paper" and comp_choice == "rock"):
                 return"WOW you win!!"
        else:
            return "Too bad you lost"
           
    def game_on(self):
        """function that actualizes the game(main function)"""
        while True:
            self.start_string()
            comp_choice = self.comp_input()
            user_choice = self.player_input()
            print(f"player's choice is {user_choice}")
            time.sleep(3)
            print("\n\ncomputer's turn loading...")
            time.sleep(5)            
            print(f"computer's choice is {comp_choice}")
            result = self.winner(user_choice, comp_choice)
            time.sleep(3)
            print(f"\n\nyou entered>>{user_choice} vs computer entered>>{comp_choice}")
            if result == 'WOW  you win':
                self.players_score += 1
            elif result == "Too bad you lost":
                self.comps_score += 1
            else:
                print("\n\nDraw")
            time.sleep(3)
            print(f"\n\nyou scored {self.players_score}\ncomputer scored {self.comps_score}")
            time.sleep(3)
            play_again = input("\n\nwill you play again (yes or no) ").lower()
            if play_again != "yes":
                break

if __name__ == "__main__":
    play = MyGame()
    play.game_on()
