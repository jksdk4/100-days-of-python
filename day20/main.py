from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("S N A K E G A M E")

positions = [(0, 0), (-20, 0), (-40, 0)]


def make_segment(coords, shape="square", color="white"):
    segment = Turtle(shape=shape)
    segment.color(color)
    segment.goto(coords)
    segment.penup()
    return segment


for pos in positions:
    new_segment = make_segment(pos)





screen.exitonclick()

