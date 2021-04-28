from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput("Make your bet", prompt=f"Which turtle will win the race? {colors} Enter a color: ")
all_turtles = []

n = 0
for n in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[n])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + n * 50)
    n += 1
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won ! The {winning_color} turtle is the winner! ")
            else:
                print(f"You've lost ! The {winning_color} turtle is the winner! ")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()
