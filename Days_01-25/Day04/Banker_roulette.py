# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

# n = len(names)
# number = random.randint(0,n-1)
# payer = names[number]

payer = random.choice(names)
print(f"Today's payer is {payer}")