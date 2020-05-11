import turtle
turtle.speed(100)
#function for red beads
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
#function for white beads
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
#function for blue beads
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
#loop to make bracelet
for i in range(12):
    red_set()
    white_set()
    blue_set()
#click to exit
turtle.Screen().exitonclick()