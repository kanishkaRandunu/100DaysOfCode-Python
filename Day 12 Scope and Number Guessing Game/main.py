#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint
from art import logo, win

easy_chances = 10
hard_chances = 5
comp_number = randint(1,100)
print(comp_number)

def check_answ(guess, answ, rounds):
  if guess > answ:
    print("Too High")
    return rounds-1
  elif guess < answ:
    print("Too Low")
    return rounds-1

def select_difficulty():
  difficulty = input("Choose a difficulty 'easy' or 'hard': ")
  if difficulty == 'easy':
    return easy_chances
  elif difficulty == 'hard':
    return hard_chances
  else:
    print("Mention the correct difficulty level")


def run_game():
  print(logo)
  print('Welcome to the Number Guessing Game ')
  print("I am thinking of a number between 1 and 100")
  
  rounds = select_difficulty()
  
  guess = 0
  while guess != comp_number:
  
    guess = int(input("Guess a number between 1-100: "))
    rounds = check_answ(guess, comp_number, rounds)
    if rounds == 0:
      print("You have finished all your guessing chances ")
      return
    elif guess == comp_number:
      print(win)
    elif guess != comp_number:
      print("Guess again")
      print(f"You have {rounds} remaining guesses ")
    print("\n")

run_game()
