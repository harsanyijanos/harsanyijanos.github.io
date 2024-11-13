import turtle

w = turtle.Screen()
w.setup(400,400)
w.bgcolor('white')
w.title("Grafika 5.")

f = turtle.Turtle()

r = 25

while r<75:
    f.circle(r)
    r += 10


w.exitonclick()