import turtle
turtle.speed(100)
for i in range(36):
    turtle.penup()
    turtle.forward(110)
    turtle.pendown()
    turtle.circle(10)
    turtle.penup()
    turtle.backward(110)
    turtle.left(10)


turtle.Screen().exitonclick()