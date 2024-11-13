import turtle

w = turtle.Screen()
w.setup(400,400)
w.bgcolor('white')
w.title("Grafika 7.")

f = turtle.Turtle()

r = 100

f.color('red')
f.width(3)
f.fillcolor('yellow')

f.penup()
f.goto(0, -r)
f.pendown()

f.begin_fill()
f.circle(r)
f.end_fill()

r = 50

f.penup()
f.goto(0, -r)
f.pendown()

f.fillcolor('red')

f.begin_fill()
f.circle(r)
f.end_fill()

w.exitonclick()