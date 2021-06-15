import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

data = pandas.read_csv("50_states.csv")
states = data(data.state)
cor_x = data.x
cor_y = data.y
print(type(states))
print(states[0],cor_x[0],cor_y[0])