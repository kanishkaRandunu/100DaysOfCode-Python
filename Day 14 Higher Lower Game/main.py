from art import logo, vs
from game_data import data
import random
from replit import clear

print(logo)

marks = 0
cont_game = True

def expand(data_i):
  name = data_i['name']
  desc = data_i['description']
  country = data_i['country']
  return(f"{name}, a {desc}, from {country}")

def compare(user_guess,data_a, data_b):
  a_flw = data_a["follower_count"]
  b_flw = data_b["follower_count"]

  if a_flw > b_flw:
    return user_guess == "A"
  else:
    return user_guess == "B"

data_b = random.choice(data)

while cont_game:

  data_a = data_b
  data_b = random.choice(data)
  if data_a == data_b:
    data_b = random.choice(data)
  
  print(f"Compare A: {expand(data_a)}")
  print(vs)
  print(f"Compare B: {expand(data_b)}")
  
  user_ans = input("who has more followers? A or B: ").upper()

  clear()
  print(logo)
  
  cont_game = compare(user_ans, data_a, data_b)
  
  if cont_game:
    marks += 1
    print(f"Your answer is right. Current Score: {marks}")
  else:
    print(f"Wrong answer. Final Score: {marks}")
  

