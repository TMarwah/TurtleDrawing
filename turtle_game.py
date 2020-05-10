import turtle
import random
from turtle import *

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

turtle.listen()

turtle.onkey(up(),'Up')
turtle.onkey(down(),'Down')
turtle.onkey(right(),'Right')
turtle.onkey(left(),'Left')

turtle.mainloop()

