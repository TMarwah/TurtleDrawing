import turtle
turtle.speed(100)
def red_set():
    turtle.penup()
    turtle.forward(110)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("red")
    turtle.circle(10)
    turtle.end_fill()
    turtle.penup()
    turtle.backward(110)
    turtle.left(10)
def white_set():
    turtle.penup()
    turtle.forward(110)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("white")
    turtle.circle(10)
    turtle.end_fill()
    turtle.penup()
    turtle.backward(110)
    turtle.left(10)

def blue_set():
    turtle.penup()
    turtle.forward(110)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("blue")
    turtle.circle(10)
    turtle.end_fill()
    turtle.penup()
    turtle.backward(110)
    turtle.left(10)

for i in range(12):
    red_set()
    white_set()
    blue_set()

turtle.Screen().exitonclick()