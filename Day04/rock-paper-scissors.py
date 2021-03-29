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
random_integer = random.randint(1,3)
print(random_integer)

user = input("Choose Rock, Paper or Scissors ")
if user == "Rock":
    print(rock)
    if random_integer == 1:
        print("A draw - you choose Rock and computer Rock too")
        print(rock)
    elif random_integer == 2:
        print("Computer chose Paper - Paper covers Rock - You lost")
        print(paper)
    else:
        print("Computer chose Scissors - You won")
        print(scissors)
elif user == "Paper":
    print(paper)
    if random_integer == 1:
        print("Computer chose Rock - You won")
        print(rock)
    elif random_integer == 2:
        print("A draw - you chose Paper and computer too.")
        print(paper)
    else:
        print("Computer chose Scissors - You lost")
        print(scissors)
elif user == "Scissors":
    print(scissors)
    if random_integer == 1:
        print("Computer chose Rock -  You lost")
        print(rock)
    elif random_integer == 2:
        print("Computer chose Paper - You won")
        print(paper)
    else:
        print("Computer chose Scissors too. A draw")
        print(scissors)
else:
    print("You've made wrong choice - exiting the game")