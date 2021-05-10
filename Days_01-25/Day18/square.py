from turtle import Turtle
from turtle import Screen

tim = Turtle()
tim.shape("turtle")
tim.color("SeaGreen")

for loop in range(4):
    tim.forward(100)
    tim.rt(90)


screen = Screen()
screen.exitonclick()
