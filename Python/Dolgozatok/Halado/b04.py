import turtle

def fractal_tree(t, branch_length, level):
    if level == 0:
        return
    else:
        t.forward(branch_length)
        t.left(30)
        fractal_tree(t, branch_length * 0.7, level - 1)
        t.right(60)
        fractal_tree(t, branch_length * 0.7, level - 1)
        t.left(30)
        t.backward(branch_length)

# Beállítások
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.left(90)
t.penup()
t.goto(0, -200)
t.pendown()

# Fraktálfa rajzolása
fractal_tree(t, 100, 5)

screen.mainloop()