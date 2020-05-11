import turtle

from turtle import Turtle, Screen
screen = Screen()
screen.setup(500,500)
def up():
    turtle.forward(100)

def back():
    turtle.backward(100)

def left():
    turtle.left(40)

def right():
    turtle.right(40)



turtle.Screen().onkeypress(up,'Up')
turtle.Screen().onkeypress(back,'Down')
turtle.Screen().onkeypress(right,'Right')
turtle.Screen().onkeypress(left,'Left')

screen.listen()
turtle.listen()
turtle.mainloop()

