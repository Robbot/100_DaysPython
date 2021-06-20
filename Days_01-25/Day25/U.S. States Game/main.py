import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
answer_state = answer_state.capitalize()

data = pandas.read_csv("50_states.csv")
print(data)
states = data.state.to_list()
cor_x = data.x
cor_y = data.y

while True:
    n = 0
    for state in states:
        n += 1
        if answer_state == state:
            print(states[n - 1], cor_x[n - 1], cor_y[n - 1])
            states.remove(states[n - 1])
            print('Updated states list: ', states)
            print(len(states))
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    answer_state = answer_state.title()
    if len(states) == 0:
        exit()
