from turtle import Turtle, Screen
from random import choice

colors = ["sea green", "blue", "lime green", "orange red", "medium violet red", "dark violet", "crimson", "peru",
          "gold"]
tim = Turtle()
screen = Screen()
screen.colormode(255)


# Random color
def set_attributes():
    # Set random color
    random_color = (choice(range(256)), choice(range(256)), choice(range(256)))
    tim.pencolor(random_color)
    # Set random angle
    random_angle = choice([0, 90, 180, 270])
    tim.setheading(random_angle)
    # Set random/fixed speed
    #tim.speed(choice(range(11)))
    tim.speed("fastest")
    # Set random/fixed width
    # tim.width(num)  # line gets thicker every iteration
    tim.width(5)  # line thickness is set to a fixed value


# Random distance
def move(num):
    random_distance = choice(range(1, 5)) * 3
    tim.forward(random_distance)


for num in range(1, 2000):
    set_attributes()
    move(num)

screen.exitonclick()
