import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
directions = [0, 90, 180, 270]
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.setheading(tim.heading() + size_of_gap)
        tim.color(random.choice(colours))
        tim.circle(100)


size_of_gap = float(input("provide the size of gap from 1 to 90: "))

draw_spirograph(size_of_gap)
screen = t.Screen()
rootwindow = screen.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

screen.exitonclick()
