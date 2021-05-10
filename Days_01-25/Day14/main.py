from art import logo, vs
from game_data import data
from replit import clear
import random

print(logo)

n = random.randint(0,49)
m=n-1
end_game = False
counter = 0
while end_game == False:
    if counter != 0:
        print(f"You're right! Current score: {counter}")

    compare1 = data[n]
    print("Compare A: "+ compare1['name'] + ", a "+ compare1['description'] + ", from " + compare1['country'])
    print(vs)
    compare2 = data[m]
    print("Against B: "+ compare2['name'] + ", a "+ compare2['description'] + ", from " + compare2['country'])
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if int(compare1['follower_count'])>int(compare2['follower_count']):
        print(str(compare1['follower_count'])+" it is A")
        if choice == "a":
            print("You win")
            counter += 1
            m = n
            n = random.randint(0, 49)
        else:
            end_game = True
            clear()
            print(f"Sorry that's wrong. Final score {counter}")
    else:
        print(str(compare2['follower_count'])+" it is B")
        if choice == "b":
            print("You win")
            counter += 1
            n = m
        else:
            end_game = True
            clear()
            print(f"Sorry that's wrong. Final score {counter}")
