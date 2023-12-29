# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 30 )
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(colors)
# print(rgb_colors)


from turtle import Turtle, Screen
from random import choice

color_list = [(244, 235, 48), (196, 12, 35), (218, 160, 70), (43, 80, 177), (237, 40, 140), (38, 215, 76), (237, 228, 5), (31, 40, 154), (206, 72, 22), (21, 149, 23), (201, 34, 98), (70, 11, 27), (182, 16, 11), (213, 164, 10), (218, 140, 195), (56, 15, 10), (17, 20, 48), (13, 95, 62), (79, 210, 159), (73, 73, 221), (83, 191, 220), (237, 158, 216), (94, 232, 200), (217, 82, 51), (5, 230, 239), (14, 64, 44)]

#Set classes
tim = Turtle()
screen = Screen()

#Set initial parameters
tim.penup() #raise pen
screen.colormode(255)

#Set initial position
tim.setheading(225)
tim.forward(70.71 * 5)
tim.setheading(0)

#print(choice(color_list))
for y in range(10):
    for x in range(10):
        tim.dot(20,choice(color_list)) #dot size set to 20 and random choice of color
        tim.forward(50) #dot space set to 50
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)



screen.exitonclick()