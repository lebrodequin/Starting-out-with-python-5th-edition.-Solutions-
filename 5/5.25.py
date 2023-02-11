import turtle


def main():
    x = -150
    y = -150
    c = 1
    turtle.speed(9)
    turtle.hideturtle()

    for z in range(5):
        for i in range(5):
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            square(c)
            x += 50
            c += 1
        x -= 250
        y += 50
    turtle.done()


def square(c):
    if c % 2 == 0:
        turtle.fillcolor('white')
        turtle.begin_fill()
        for x in range(4):
            turtle.forward(50)
            turtle.left(90)
        turtle.end_fill()
    else:
        turtle.fillcolor('black')
        turtle.begin_fill()
        for x in range(4):
            turtle.forward(50)
            turtle.left(90)
        turtle.end_fill()


main()
