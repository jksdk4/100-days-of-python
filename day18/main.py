import random
from turtle import Turtle, Screen, colormode

theo = Turtle()
theo.shape("turtle")
theo.pensize(2)
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
    theo.color(r, g, b)

# interior angle of a polygon with n sides: (n - 2) * 180 / n
# exterior angles: 360 / n
# sum of angles: (n - 2) * 180. if a polygon has n sides, there are n-2 triangles inside.

# def draw_shape(num_sides):
#     change_color()
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         theo.forward(100)
#         theo.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)


# random walk
directions = [0, 90, 180, 360]
theo.speed("fastest")

for _ in range(300):
    change_color()
    theo.forward(30)
    theo.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
