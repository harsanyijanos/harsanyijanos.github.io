import turtle

def fraktal(szint, hossz):
    if szint>1:
        for _ in range(4):
            t.fd(hossz)
            t.left(90)
            fraktal(szint-1, hossz/3)



ablak =turtle.Screen()
ablak.setup(500,500)
ablak.bgcolor('#FFFFFF')
ablak.title('proba')
t = turtle.Turtle()
t.up()
t.goto(-200,-200)
t.down()

fraktal(6,400)

ablak.exitonclick()