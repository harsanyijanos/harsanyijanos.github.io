import turtle

w = turtle.Screen()
w.setup(400,400)
w.bgcolor('white')
w.title("Grafika 6.")

f = turtle.Turtle()

r = 75

f.color('red')
f.width(3)
f.fillcolor('yellow')

f.begin_fill()

f.circle(r)

f.end_fill()


w.exitonclick()