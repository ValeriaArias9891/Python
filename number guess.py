import random
from replit import clear
import Art

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def welcome():
  print(Art.logo)
  print("Welcome to your guessing numbers game!")

welcome()
dificulty= input("please choose your difficulty between hard and easy \n").lower()
chosen= False
while not chosen:
  if dificulty == "hard":
    turns = 5 
    chosen= True
  elif dificulty == "easy":
    turns = 10
    chosen= True
  else:
    dificulty= input("please choose your difficulty between hard and easy \n").lower()
    chosen=True 
    
answer= random.randint(1,100)
print(f"Pssst. The answer is {answer}.")
good_guess=False

while not good_guess:
  guess= int(input("Guess a number between 1 and 100: "))
  if guess == answer:
    print("You guessed it right!")
    good_guess= True
  elif guess > answer:
    print(f"Too high, you have {turns} turns left")
  elif guess < answer:
    print(f"Too low, you have {turns} turns")
  else:
    print(f"Please try again, you have {turns} turns left")
  turns -= 1
  if turns < 0 and guess != answer:
    print("You ran out of turns")
    good_guess=True