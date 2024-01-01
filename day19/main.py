from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_backward():
    tim.backward(10)


def move_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_counterclockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def move_forward():
    tim.forward(10)


def clear():
    # offers nice sliding effect instead of sudden tim.reset()
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key='a', fun=move_counterclockwise)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
