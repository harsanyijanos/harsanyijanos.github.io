def tree(n, ihossz, szog, szorzo):
    f.fd(ihossz)
    if n>1:
        uhossz=ihossz*szorzo
        f.left(szog)
        tree(n-1,uhossz,szog,szorzo)
        f.right(2*szog)
        tree(n-1,uhossz,szog,szorzo)
        f.left(szog)
    f.bk(ihossz)


import turtle

w = turtle.Screen()
w.setup(400,400)
w.bgcolor('white')
w.title("program_1")
f = turtle.Turtle()
tree(9,60,70,0.7)
w.exitonclick()