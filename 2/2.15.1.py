import turtle
turtle.speed(5)
turtle.setup(600, 600)
turtle.penup()
turtle.goto(140, -140)
turtle.pendown()

turtle.pensize(5)
turtle.pencolor('green')
turtle.bgcolor('red')

turtle.fillcolor("blue")
turtle.begin_fill()

turtle.showturtle()
turtle.left(45)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(400)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(400)

turtle.end_fill()

turtle.done()
