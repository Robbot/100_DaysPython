# import colorgram
#
#
# rgb_colors= []
# colors = colorgram.extract('hirst.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as t
import random
t.colormode(255)
t.speed("fastest")
t.penup()
t.hideturtle()

colors = [(21, 114, 173), (142, 163, 184), (204, 137, 166), (190, 173, 17), (145, 17, 32), (238, 213, 62), (67, 24, 31), (17, 138, 59), (219, 161, 88), (122, 71, 100), (49, 29, 26), (197, 65, 28), (7, 107, 64), (227, 169, 197), (240, 78, 29), (29, 177, 84), (21, 172, 188), (243, 214, 4), (110, 192, 140), (182, 94, 115), (35, 37, 46), (188, 182, 213), (157, 206, 215), (240, 168, 154), (147, 215, 171), (127, 32, 26)]

t.setheading(225)
t.forward(300)
t.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots):
    t.dot(20 , (colors[random.randint(0,25)]))
    t.fd(50)
    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)
t.dot(20 , (colors[random.randint(0,25)]))

screen = t.Screen()
screen.exitonclick()
