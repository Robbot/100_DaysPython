from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.seth(0)
    tim.forward(10)


def move_backwards():
    tim.seth(180)
    tim.forward(10)

def move_counterclockwise():
    tim.seth(90)
    tim.forward(10)

def move_clockwise():
    tim.seth(270)
    tim.forward(10)

def clear():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counterclockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
