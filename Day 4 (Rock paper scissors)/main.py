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

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))
computer_choice = random.randint(0,2)
print(f"You Chose:\n{game_images[user_choice]}\n")
print(f"Computer Chose\n{game_images[computer_choice]}\n")

if (user_choice > 2  or user_choice < 0):
    print("Invalid Choice")
elif (user_choice == computer_choice):
    print("Its a draw")
elif(user_choice == 0 and computer_choice == 2):
    print("You Win")
elif(user_choice == 2 and computer_choice == 0):
    print("You Lose")
elif(user_choice > computer_choice):
    print("You Win")
else:
    print("You Lose")