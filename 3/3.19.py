import turtle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_X = 100
TARGET_LLEFT_Y = 250
TARGET_WIDTH = 35
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)

turtle.penup()

turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1−10): "))

distance = force * FORCE_FACTOR

turtle.setheading(angle)

turtle.pendown()
turtle.forward(distance)

if turtle.xcor() >= TARGET_LLEFT_X and turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and turtle.ycor() >= TARGET_LLEFT_Y and turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH):
    print('Target hit!')
elif turtle.xcor() < TARGET_LLEFT_X and turtle.ycor() < TARGET_LLEFT_Y:
    print('increase force')
elif TARGET_LLEFT_X <= turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and turtle.ycor() < TARGET_LLEFT_Y :
    print('increase angle')
elif TARGET_LLEFT_Y <= turtle.yor() <= (TARGET_LLEFT_Y + TARGET_WIDTH) and turtle.xcor() < TARGET_LLEFT_X:
    print('decrease angle')
