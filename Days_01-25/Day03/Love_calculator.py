# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()
two_names = lower_name1+lower_name2

word_true = two_names.count("t")+two_names.count("r")+two_names.count("u")+two_names.count("e")
word_love = two_names.count("l")+two_names.count("o")+two_names.count("v")+two_names.count("e")

if word_true !=0:
    score = str(word_true)+str(word_love)
score = int(score)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")