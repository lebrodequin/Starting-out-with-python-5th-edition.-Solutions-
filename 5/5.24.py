import turtle
import math

def main():
    height = float(input('input height: '))
    width = float(input('input width: '))
    for x in range(4):
        drawPattern(height, width)
        turtle.left(90)
    turtle.done()

def drawPattern(x, y):
    turtle.hideturtle()
    turtle.fillcolor('black')

    turtle.begin_fill()
    for z in range(2):
        turtle.forward(y/2)
        turtle.left(90)
        turtle.forward(x/2)
        turtle.left(90)
    turtle.end_fill()

    for z in range(2):
        turtle.forward(y/4*3)
        turtle.left(90)
        turtle.forward(x/4*3)
        turtle.left(90)

    for z in range(2):
        turtle.forward(y)
        turtle.left(90)
        turtle.forward(x)
        turtle.left(90)

    turtle.goto(y, x)

    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.right(45)

main()
