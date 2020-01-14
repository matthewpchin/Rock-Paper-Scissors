from easygui import *
import random
if ynbox("Hey user, would you like to play Rock, Paper, Scissors with me??","Rock Paper Scissors"): #Opening Yes/No Box
   pass #If yes continue
else:
    sys.exit(0) #If no exit
while True: #Used for Looping
   msg ="Choose your play"
   title = "Rock Paper Scissors"
   choices = ["Rock", "Paper", "Scissors"]
   choice = choicebox(msg, title, choices) #Choice between Rock/Paper/Scissors
   random.shuffle(choices) #Shuffles list of (Rock, Paper, and Scissors)
   if choice == "Rock" and choices[1] == "Rock": #All outcomes for choice of Rock
       msgbox("I choose Rock, It's a Tie!")
   elif choice == "Rock" and choices[1] == "Paper":
       msgbox("I choose Paper, You Lose :(")
   elif choice == "Rock" and choices[1] == "Scissors":
       msgbox("I choose Scissors, You Win :)")
   if choice == "Paper" and choices[1] == "Paper": #All outcomes for choice of Paper
       msgbox("I choose Paper, It's a Tie!")
   elif choice == "Paper" and choices[1] == "Scissors":
       msgbox("I choose Scissors, You Lose :(")
   elif choice == "Paper" and choices[1] == "Rock":
       msgbox("I choose Rock, You Win :)")
   if choice == "Scissors" and choices[1] == "Rock": #All outcomes for choice of Scissors
       msgbox("I choose Rock, You Lose :(")
   elif choice == "Scissors" and choices[1] == "Paper":
       msgbox("I choose Paper, You Win :)")
   elif choice == "Scissors" and choices[1] == "Scissors":
       msgbox("I choose Scissors, It's a Tie!")
   if ynbox("Would you like to play again?"): #Yes/No box
       continue #If yes loop back up to start of while loop
   else:
       msgbox("Thanks for Playing!")
       sys.exit(0) #If no exit



