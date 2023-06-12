rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random as rd

gesture_names = ['rock', 'paper', 'scissors']

user_ip = int(input('Wat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
print(f'You chose: {gesture_names[user_ip]}')
comp_int = rd.randint(0,2)
gestures = [rock, paper, scissors]

print(gestures[user_ip]) 
print('\n')
print(f'Computer chose: {gesture_names[comp_int]}')
print(gestures[comp_int])
print('\n')

map1 = ['Play again', 'You lose', 'You win']
map2 = ['You win', 'Play again', 'You lose']
map3 = ['You lose', 'You win', 'Play again']
  
map = [map1, map2, map3]

print(map[user_ip][comp_int])

