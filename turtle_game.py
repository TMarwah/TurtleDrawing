import turtle

from turtle import Turtle, Screen
screen = Screen()
screen.setup(1200,500)
def up():
    turtle.setheading(90)
    turtle.forward(100)

def down():
    turtle.setheading(270)
    turtle.forward(100)

def left():
    turtle.setheading(180)
    turtle.forward(100)

def right():
    turtle.setheading(0)
    turtle.forward(100)



turtle.Screen().onkeypress(up,'Up')
turtle.Screen().onkeypress(down,'Down')
turtle.Screen().onkeypress(right,'Right')
turtle.Screen().onkeypress(left,'Left')

screen.listen()
turtle.listen()
turtle.mainloop()

