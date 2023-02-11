import turtle
turtle.speed(8)
turtle.setup(600, 600)

rad = turtle.numinput('input circle radius', 'i love julia', 50)

turtle.pensize(3)
turtle.pencolor('green')
turtle.bgcolor('yellow')

turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()
turtle.circle(rad)

turtle.penup()
turtle.goto(50, -50)
turtle.pendown()
turtle.circle(rad)

turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
turtle.circle(rad)

turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.circle(rad)

turtle.penup()
turtle.goto(100, 50)
turtle.pendown()
turtle.circle(rad)


turtle.done()
