import random
print("Welcome to rock, paper and scissor")
user_choice = int(
    input("What would you like to go with? Rock 0, paper 1, scissor 2? "))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

___________________________
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
___________________________
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
___________________________
'''

weapon = [rock, paper, scissors]

# user_choice = None
computer_choice = random.randint(0, 2)
computer = weapon[computer_choice]
if user_choice == 0:
    print("User chose:")
    print(rock)
    # user_choice == rock
    print("Computer chose:")
    print(computer)
elif user_choice == 1:
    print("User chose:")
    print(paper)
    print("Computer chose:")
    print(computer)
    # user_choice == paper

elif user_choice == 2:
    print("User chose:")
    print(scissors)
    print("Computer chose:")
    print(computer)

    # user_choice == scissors


if user_choice >= 3:
    print("Invalid number, try again!")
elif user_choice == 0 and computer_choice == 2:
    print("User Won!")
elif user_choice == 2 and computer_choice == 0:
    print("Computer Won!")
elif user_choice < computer_choice:
    print("Computer Won!")
elif user_choice > computer_choice or user_choice == 0 and computer_choice == 2:
    print("User Won!")
elif user_choice == computer_choice:
    print("Game tie!")
