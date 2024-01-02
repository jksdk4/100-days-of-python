from turtle import Turtle, Screen
import random

turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=500, height=600)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


def set_starting_place(y, x=-230):
    """based on setup width, x shifts over a little bit from 250, y value splits into equals"""
    half = y // 2
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.speed('slowest')
        new_turtle.goto(x, y)
        turtles.append(new_turtle)
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
    if user_bet == winner.pencolor():
        print("\nYou won the bet.")
    else:
        print(f"\nYou lost the bet.")
    print(f"{winner.pencolor()} won.")


set_starting_place(160)
start_race()

screen.exitonclick()
