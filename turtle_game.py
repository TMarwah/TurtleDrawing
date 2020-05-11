#import turtle package
import turtle
from turtle import Turtle, Screen

#screen setup
screen = Screen()
screen.setup(500,500)
#move forward
def up():
    turtle.forward(100)
#move backward
def back():
    turtle.backward(100)
#turn left
def left():
    turtle.left(40)
#turn right
def right():
    turtle.right(40)


#handle keypresses
turtle.Screen().onkeypress(up,'Up')
turtle.Screen().onkeypress(back,'Down')
turtle.Screen().onkeypress(right,'Right')
turtle.Screen().onkeypress(left,'Left')
#listen for key input
screen.listen()
turtle.listen()
#keep running program till exited
turtle.mainloop()

