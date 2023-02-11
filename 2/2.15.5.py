import turtle
turtle.hideturtle()
turtle.speed(6)
turtle.setup(600, 600)

turtle.penup()
turtle.goto(-200, 0)
turtle.write('West', align="left")

turtle.pendown()
turtle.goto(200, 0)
turtle.write('East', align="right")

turtle.penup()
turtle.goto(0, 200)
turtle.write('North', align="center")

turtle.pendown()
turtle.goto(0, -200)
turtle.write('South', align="center")

turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(100)

turtle.penup()
turtle.goto(0, 0)
turtle.dot(6)

turtle.done()
