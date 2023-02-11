import turtle
turtle.setup(600, 600)
turtle.hideturtle()
turtle.speed(0)

turtle.penup()
turtle.goto(-200, -100)
turtle.pendown()

num_of_ends = 8
angle = 180 - 360 / num_of_ends

for x in range(num_of_ends):
    turtle.forward(400)
    turtle.left(angle)

turtle.done()
