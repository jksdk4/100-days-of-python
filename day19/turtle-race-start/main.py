from turtle import Turtle, Screen
import random

tim = Turtle(shape="turtle")
tanya = Turtle(shape="turtle")
tom = Turtle(shape="turtle")
terry = Turtle(shape="turtle")
tina = Turtle(shape="turtle")

turtles = [tim, tanya, tom, terry, tina]
colors = ["red", "orange", "yellow", "green", "blue"]

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


def set_colors():
    for idx, turtle in enumerate(turtles):
        turtle.color(colors[idx])


def set_starting_place(y, x=-230):
    """based on setup width, x shifts over a little bit from 250, y value splits into equals"""
    set_colors()
    half = y // 2
    for turtle in turtles:
        turtle.penup()
        turtle.speed('slowest')
        turtle.goto(x, y)
        y -= half


def start_race():
    racing = True
    winner = None
    for turtle in turtles:
        turtle.speed("slow")
    while racing:
        for turtle in turtles:
            increment = random.randint(5, 11)
            turtle.forward(increment)
            if turtle.xcor() >= 240:
                winner = turtle
                racing = False

    print(f"You bet on: {user_bet.title()}")
    if user_bet == winner.color()[0]:
        print("\nYou won the bet.")
    else:
        print(f"\nYou lost the bet.")
    print(f"{winner.color()[0].title()} won.")


set_starting_place(160)
start_race()

screen.exitonclick()
