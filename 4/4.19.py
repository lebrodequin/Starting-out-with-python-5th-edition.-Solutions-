import turtle

turtle.hideturtle()
turtle.speed(0)

distance = 100
sides = 8

angle = 360 / sides
my_color = "red"

turtle.penup()
turtle.goto(-50, 100)
turtle.pendown()
turtle.color(my_color)
turtle.begin_fill()
for i in range(sides):
   turtle.forward(distance)
   turtle.right(angle)

turtle.end_fill()
turtle.hideturtle()

turtle.penup()
turtle.right(90)
turtle.forward(distance*1.5)
turtle.color('white')
turtle.write('STOP', font=("Arial", 35, "normal"))

turtle.done()
