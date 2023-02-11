import turtle
turtle.speed(6)


def main():
    x_pos = int(input('input x position: '))
    y_pos = int(input('input y position: '))
    lengt = int(input('input length: '))
    inp_color = str(input('input color: '))
    draw(x_pos, y_pos, lengt, inp_color)
    turtle.done()


def draw(x, y, l, c):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(c)
    turtle.begin_fill()
    for x in range(3):
        turtle.forward(l)
        turtle.left(120)
    turtle.end_fill()


main()
