import turtle
import math
w = turtle.Screen()
w.setup(500,500)
w.bgcolor('white')
w.title("Teknőcgrafika")
f = turtle.Turtle()

a= 200
rk = a/math.sqrt(3)
rb = a/math.sqrt(3)/2

f.penup()
f.goto(0, -rk)
f.pendown()
f.pencolor('red')
f.fillcolor('red')
f.begin_fill()
f.circle(rk)
f.end_fill()


f.penup()
f.goto(-a/2, -rb)
f.pendown()
f.pencolor('yellow')
f.fillcolor('yellow')
f.begin_fill()
f.fd(a)
f.left(120)
f.fd(a)
f.left(120)
f.fd(a)
f.left(120)
f.end_fill()

f.penup()
f.goto(0, -rb)
f.pendown()
f.pencolor('blue')
f.fillcolor('blue')
f.begin_fill()
f.circle(rb)
f.end_fill()



w.exitonclick()