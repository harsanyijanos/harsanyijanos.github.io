import turtle
w = turtle.Screen()
w.setup(500,500)
w.bgcolor('white')
w.title("Teknőcgrafika")
f = turtle.Turtle()

a= 200
f.penup()
f.goto(-a/2, -a/2)
f.pendown()

f.width(3)
f.pencolor('red')
f.fillcolor('blue')
f.begin_fill()
f.fd(a)
f.left(90)
f.fd(a)
f.left(90)
f.fd(a)
f.left(90)
f.fd(a)
f.left(90)
f.end_fill()

f.fillcolor('yellow')
f.begin_fill()
f.circle(a, 90)
f.left(90)
f.circle(a, 90)
f.end_fill()

w.exitonclick()