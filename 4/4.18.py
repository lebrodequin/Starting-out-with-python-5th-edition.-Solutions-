import turtle
size = 4

turtle.setup(600, 600)
turtle.speed(0)

turtle.hideturtle()
turtle.setheading(90)

for x in range(30):
    for y in range(4):
        turtle.forward(size)
        turtle.left(90)
        size +=4

turtle.done()