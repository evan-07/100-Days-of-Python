from turtle import Turtle, Screen
from random import choice

tim = Turtle()
tim.speed("fastest")
screen = Screen()
screen.colormode(255)


def set_attributes():
    # Set random color
    random_color = (choice(range(256)), choice(range(256)), choice(range(256)))
    return random_color


heading = 0

while heading <= 360:
    tim.color(set_attributes())
    tim.setheading(heading)
    tim.circle(100)
    heading += 3


screen.exitonclick()