import turtle
turtle.speed(8)
turtle.setup(600, 600)
turtle.penup()

turtle.goto(-100, -100)
turtle.pendown()
turtle.pensize(3)
turtle.pencolor('green')
turtle.bgcolor('grey')
turtle.fillcolor("blue")

turtle.begin_fill()

turtle.showturtle()
turtle.goto(0, 0)
turtle.goto(100, -100)
turtle.goto(-100, -100)
turtle.end_fill()

turtle.goto(0, 100)
turtle.goto(100, -100)

turtle.done()
