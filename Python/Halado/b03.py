"""
Fraktál rajzolása
Sierpinski-háromszög rajzolása
Megoldás rekurzív függvénnyel


"""

import turtle

def sierpinski_triangle(length, level):
    if level == 0:
        for _ in range(3):
            f.forward(length)
            f.left(120)
    else:
        length /= 2
        sierpinski_triangle(length, level - 1)
        f.forward(length)
        sierpinski_triangle(length, level - 1)
        f.backward(length)
        f.left(60)
        f.forward(length)
        f.right(60)
        sierpinski_triangle(length, level - 1)
        f.left(60)
        f.backward(length)
        f.right(60)

# Beállítások
screen = turtle.Screen()
screen.bgcolor("white")
f = turtle.Turtle()
f.speed(0)

# Sierpinski-háromszög rajzolása
f.penup()
f.goto(-200, -150)
f.pendown()
sierpinski_triangle(400, 5)

screen.mainloop()