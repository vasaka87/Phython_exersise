import turtle
side=20
turtle.speed('fastest')
for x in range(8):
    for i in range(8):
        if  (x % 2 == 0 and i % 2 == 0) or (x % 2 != 0 and i % 2 != 0):
            #turtle.begin_fill()
        for n in range(4):
            turtle.forward(side)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(side)

    turtle.penup()
    turtle.goto(0, side + (side*x))
    turtle.pendown()

turtle.exitonclick()