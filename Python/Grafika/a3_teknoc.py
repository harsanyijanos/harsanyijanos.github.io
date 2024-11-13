import turtle

w = turtle.Screen()
w.setup(400,400)
w.bgcolor('white')
w.title("Grafika 3.")

f = turtle.Turtle()

h = 75

i = 1
while i<5:
    f.fd(h)
    f.left(90)
    i +=1
 
i = 1
while i<4:
    f.fd(h)
    f.left(120)
    i +=1

i = 1
while i<6:
    f.fd(h)
    f.left(72)
    i +=1  

i = 1
while i<7:
    f.fd(h)
    f.left(60)
    i +=1    

w.exitonclick()