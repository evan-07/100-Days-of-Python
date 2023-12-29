from turtle import Turtle, Screen
from random import choice

tim = Turtle()
screen = Screen()
tim.penup()
tim.setpos(-50, -100)
tim.pendown()

colors = ["sea green", "blue", "lime green", "orange red", "medium violet red", "dark violet", "crimson", "peru", "gold"]


def draw_shape(start_num, end_num):
    for side_count in range(start_num, end_num):
        angle = 360 / side_count
        # perimeter = 1000 / side_count
        perimeter = 50
        # tim.pencolor(colors[side_count - 3])
        tim.pencolor(choice(colors))
        for _ in range(side_count):
            tim.forward(perimeter)
            tim.left(angle)
        screen.delay(5)
        # tim.clear()


draw_shape(3, 20)

screen.exitonclick()
