import turtle
import random

def main():
    turtle.setup(400, 400)
    turtle.hideturtle()
    turtle.speed(8)

    turtle.fillcolor('black')
    turtle.begin_fill()
    drawHorizon()
    turtle.goto(200, 200)
    turtle.goto(-200, 200)
    turtle.goto(-200,-50)
    turtle.end_fill()

    drawStars()
    turtle.penup()
    turtle.goto(-200, -50)

    turtle.fillcolor('grey')
    turtle.begin_fill()
    drawHorizon()
    turtle.goto(200, -200)
    turtle.goto(-200,-200)
    turtle.end_fill()

    drawWindows(-120, -30)
    drawWindows(-70, 50)
    drawWindows(-20, 80)
    drawWindows(-30, 40)
    drawWindows(-40, -100)
    drawWindows(70, -30)

    turtle.done()


def drawHorizon():
    turtle.penup()
    turtle.goto(-200, -50)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)

def drawWindows(x,y):
    turtle.fillcolor('white')
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(10)
        turtle.right(90)
    turtle.end_fill()


def drawStars():
    z = 0
    turtle.penup()
    while z < 20:
        x = random.randint(-200, 200)
        y = random.randint(-100, 200)
        turtle.goto(x, y)
        turtle.dot(3, 'white')
        z += 1

main()
