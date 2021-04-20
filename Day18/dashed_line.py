from turtle import Turtle
from turtle import Screen

tim = Turtle()
tim.shape("turtle")
tim.color("SeaGreen")

for loop in range(50):
    tim.forward(3)
    tim.up()
    tim.forward(3)
    tim.down()

screen = Screen()
screen.exitonclick()
