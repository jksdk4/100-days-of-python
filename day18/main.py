import random
from turtle import Turtle, Screen, colormode

theo = Turtle()
theo.shape("turtle")
# theo.color("violetred")

# make a square
# for _ in range(4):
#     theo.forward(100)
#     theo.left(90)
#
# make a dashed line
# for _ in range(12):
#     theo.down()
#     theo.forward(25)
#     theo.up()
#     theo.forward(25)
#
# theo.home()
# resetscreen()

# underscore is a value that's not very important here. like I'm not modifying it, so I ignore.
# can also be used akin to JS -> a,,b = [1, 2, 3] where a=1 and b=3
# so in python a,_,b=[1,2,3], _ = 2 here.
# similarly, a,*_,b=(7,6,5,4,3,2,1) behaves similarly to spread operator, so _ = [6,5,4,3,2]
# no asterisk is an error, too many values to unpack. doesn't have to be on the end like spread.


def change_color():
    colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

# interior angle of a polygon with n sides: (n - 2) * 180 / n
# exterior angles: 360 / n
# sum of angles: (n - 2) * 180. if a polygon has n sides, there are n-2 triangles inside.


# def draw_shape(num_sides):
#     theo.color(change_color())
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         theo.forward(100)
#         theo.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)


# random walk
# directions = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
# theo.pensize(3)
# theo.speed("fastest")
#
# for _ in range(500):
#     theo.color(change_color())
#     theo.forward(15)
#     theo.setheading(random.choice(directions))

theo.pensize(2)
theo.speed('fastest')
# for _ in range(0, 361, 5):
#     theo.setheading(_)
#     theo.color(change_color())
#     theo.circle(70)
# or,


def draw_spirograph(gap_size):
    for _ in range(360 // gap_size):
        theo.setheading(theo.heading() + gap_size)
        theo.color(change_color())
        theo.circle(150)


draw_spirograph(4)

screen = Screen()
screen.exitonclick()
