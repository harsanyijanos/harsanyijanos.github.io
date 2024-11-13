import turtle


def fraktal(szint, hossz):
    uhossz=hossz/5
    if szint>0:
        for _ in range(4):
            t.fd(hossz)
            t.left(90)
            fraktal(szint-1, uhossz)
            t.fd(uhossz)
            fraktal(szint-1, uhossz)
            t.fd(2*uhossz)
            fraktal(szint-1, uhossz)
            t.backward(3*uhossz)
  

ablak =turtle.Screen()
ablak.setup(500,500)
ablak.bgcolor('#FFFFFF')
ablak.title('proba')
t = turtle.Turtle()
t.speed(0)
t.up()
t.goto(-200,-200)
t.down()

fraktal(1,400)

t.getscreen().getcanvas().postscript(file='proba.eps')

ablak.exitonclick()