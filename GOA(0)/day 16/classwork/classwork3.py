from turtle import *

def kvadratis_xazva():
    for i in range(4):
        forward(200)
        left(90)

kvadratis_xazva()

penup()
goto(-400, 0)
pendown()

kvadratis_xazva()

penup()
goto(-400, -300)
pendown()

kvadratis_xazva()

penup()
goto(0, -300)
pendown()

kvadratis_xazva()