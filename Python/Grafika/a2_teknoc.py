import turtle

w = turtle.Screen()
w.setup(400,400)
w.bgcolor('white')
w.title("Grafika 2.")

f = turtle.Turtle()

h = 75

i = 1
while i<5:
    f.fd(h)
    f.left(90)
    i +=1

w.exitonclick()