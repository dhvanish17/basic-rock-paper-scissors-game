import random

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

print("Welcome to Rock, Paper, Scissors!")
print('''
                _          _ __   __ _ _ __   ___ _ __                _                        
               | |        | '_ \ / _` | '_ \ / _ \ '__|              (_)                       
 _ __ ___   ___| | __     | |_) | (_| | |_) |  __/ |         ___  ___ _ ___ ___  ___  _ __ ___ 
| '__/ _ \ / __| |/ /     | .__/ \__,_| .__/ \___|_|        / __|/ __| / __/ __|/ _ \| '__/ __|
| | | (_) | (__|   <      | |         | |                   \__ \ (__| \__ \__ \ (_) | |  \___\\
|_|  \___/ \___|_|\_\     |_|         |_|                   |___/\___|_|___/___/\___/|_|  |___/ 
''')

game_images = [rock, paper, scissors]

user_choice = int(input('''
Please choose one of the following:

1. Press 0 for ROCK
2. Press 1 for PAPER
3. Press 3 for SCISSORS

'''))

if user_choice == 0 or user_choice == 1 or user_choice == 2:
  print("\nYou selected:")
  print(game_images[user_choice])
else:
  print("Invalid choice. Please try again!")

computer_choice = random.randint(0, 2)

if computer_choice == 0:
  print("Computer selected:")
  print(game_images[computer_choice])
  if user_choice == 0:
    print("IT'S A DRAW!")
  elif user_choice == 1:
    print("YOU WIN!!!")
  else:
    print("COMPUTER WINS!!!")
elif computer_choice == 1:
  print("Computer selected:")
  print(game_images[computer_choice])
  if user_choice == 1:
    print("IT'S A DRAW!")
  elif user_choice == 0:
    print("YOU WIN!!!")
  else:
    print("COMPUTER WINS!!!")
elif computer_choice == 2:
  print("Computer selected:")
  print(game_images[computer_choice])
  if user_choice == 2:
    print("IT'S A DRAW!")
  elif user_choice == 0:
    print("YOU WIN!!!")
  else:
    print("COMPUTER WINS!!!")
