import turtle
turtle.speed(8)
turtle.setup(600, 600)

turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()

turtle.pensize(3)
turtle.pencolor('green')
turtle.bgcolor('yellow')

turtle.showturtle()

turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.goto(0, -100)
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
turtle.goto (100,-100)
turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
turtle.goto (0, 100)


turtle.done()
