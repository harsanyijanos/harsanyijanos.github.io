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

for i in range(10):
    if i%2==0:
        pY=0
    else:
        pY=oldal2
    f.penup()
    f.goto(pX, pY)
    f.pendown()
    teglalap(oldal1,oldal2)
    pX += oldal1
    


w.exitonclick()