import turtle
w = turtle.Screen()
w.setup(500,500)
w.bgcolor('white')
w.title("Teknőcgrafika")
f = turtle.Turtle()

# az arc megrajzolása
f.penup()
f.goto(0, -75)
f.pendown()
f.width(2)
f.color('red')
f.fillcolor('yellow')
f.begin_fill()
f.circle(75)
f.end_fill()

#száj megrajzolása
f.width(14)
f.penup()
f.goto(0, -50)
f.circle(50, 300)
f.pendown()
f.circle(50, 120)
f.right(60)

# jobb szem megrajzolása
f.penup()
f.goto(27, 12)
f.pendown()
f.width(2)
f.fillcolor('red')
f.begin_fill()
f.circle(15)
f.end_fill()

# jobb szem megrajzolása
f.penup()
f.goto(-27, 12)
f.pendown()
f.begin_fill()
f.circle(15)
f.end_fill()

f.penup()
f.goto(0, 100)

w.exitonclick()