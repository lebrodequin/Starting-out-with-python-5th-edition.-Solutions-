import turtle


def main():
    turtle.hideturtle()
    turtle.speed(5)
    turtle.setup(500, 800)
    drawBase()
    drawMidSection()
    drawArms()
    drawHead()
    drawHat()
    turtle.done()


def drawBase():
    turtle.penup()
    turtle.goto(0, -350)
    turtle.pendown()
    turtle.circle(150)


def drawMidSection():
    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.circle(100)


def drawArms():
    turtle.penup()
    turtle.goto(100, 50)
    turtle.pendown()
    turtle.setheading(30)
    turtle.forward(70)
    turtle.left(30)
    turtle.forward(20)
    turtle.left(180)
    turtle.forward(20)
    turtle.left(120)
    turtle.forward(20)

    turtle.penup()
    turtle.goto(-100, 50)
    turtle.pendown()
    turtle.setheading(150)
    turtle.forward(50)
    turtle.right(70)
    turtle.forward(40)
    turtle.right(20)
    turtle.forward(20)
    turtle.left(180)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(20)


def drawHead():
    turtle.setheading(0)
    turtle.penup()
    turtle.goto(0, 150)
    turtle.pendown()
    turtle.circle(65)


def drawHat():
    turtle.penup()
    turtle.goto(-75, 250)
    turtle.pendown()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.end_fill()


main()
