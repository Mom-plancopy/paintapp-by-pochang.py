#github copy editon
import re
import sys
import time
from turtle import *

screen = Screen()
screen.listen()
t = Turtle()
t.penup()
t.color("white")
t.pensize(0)
t.goto(-150,300)
t.color((27/255,42/255,53/255))
t.write("Use Q and E keys to switch colors.",font=("MS Sans Serif", 20, "normal"))
t.pensize(2)
t.left(45)

# variables
pendown = False
coloR = 0
colors = [
    (27/255,42/255,53/255), #black
    (196/255, 40/255, 28/255), #red
    (218/255,133/255,65/255), #orange
    (245/255,205/255,48/255), #yellow
    (75/255,151/255,75/255), #green
    (13/255,105/255,172/255), #blue
    (107/255,50/255,124/255) #purple
]

# functions
def pen(x, y):
    global pendown   # tell Python we mean the global variable
    if not pendown:
        pendown = True
        t.color(colors[coloR])
        t.goto(x, y)
        t.pendown()
        print("start line draw at x :" + str(x) + "y :" + str(y))
    else:
        pendown = False
        t.color(colors[coloR])
        t.goto(x, y)
        t.penup()
        print("end line draw at x :" + str(x) + "y :" + str(y))

def q():
    global coloR
    global colors
    if coloR < len(colors)-1:
        coloR = coloR + 1
        t.color(colors[coloR])
        print("changed color to " + str(coloR))
    else:
        print("highest color item :(")

def e():
    global coloR
    global colors
    if coloR > 0:
        coloR = coloR - 1
        t.color(colors[coloR])
        print("changed color to " + str(coloR))
    else:
        print("lowest color item :(")
# inputs
screen.onscreenclick(pen)
screen.onkey(e,r'q')
screen.onkey(q,r'e')

done()
