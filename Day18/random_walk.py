# import turtle as t
# import random
#
# tim = t.Turtle()
#
# ########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#

from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("SeaGreen")
tim.pensize(15)

R = 0
G = 0
B = 0


def color():
    R = random.random()
    G = random.random()
    B = random.random()
    tim.color((R, G, B))


values = [0, 90, 180, 270]


def random_move():
    tim.forward(30)
    tim.right(random.choice(values))



for _ in range(200):
    color()
    random_move()
