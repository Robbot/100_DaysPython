def turn_right():
    turn_left()
    turn_left()
    turn_left()
def loop():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for step in range(6):
    loop()

# while at_goal() == False :
#     loop()