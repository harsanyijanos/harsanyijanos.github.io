def teglalap(a, b):
    f.fd(a)
    f.left(90)
    f.fd(b)
    f.left(90)
    f.fd(a)
    f.left(90)
    f.fd(b)
    f.left(90)

import turtle
w = turtle.Screen()
w.setup(500,500)
w.bgcolor('white')
w.title("Teknőcgrafika")
f = turtle.Turtle()

oldal1=30 
oldal2=20
pX=-150
pY=150

for _ in range(10):
    f.penup()
    f.goto(pX, pY)
    f.pendown()
    teglalap(oldal1,oldal2)
    pX += oldal1
    pY -= oldal2


w.exitonclick()