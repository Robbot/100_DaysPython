from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("SeaGreen")

R = 0
G = 0
B = 0


def color():
    R = random.random()
    G = random.random()
    B = random.random()
    tim.color((R, G, B))


def move_sequence(n):
    for seq in range(n):
        tim.forward(100)
        tim.rt(360 / n)


for k in range(8):
    n = k + 3
    move_sequence(n)
    color()

# And below is solution by Angela
# import turtle as t
# import random
#
# tim = t.Turtle()
#
# ########### Challenge 3 - Draw Shapes ########
#
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
# "SeaGreen"]
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()
