
import turtle
import math

GAME = 70
# turtle.forward(200)
if GAME == 10: # simple squar

    a = turtle.Turtle()
    a.color("red", "blue")
    a.begin_fill()
    a.left(90)
    a.forward(100)
    a.left(90)
    a.forward(100)
    a.left(90)
    a.forward(100)
    a.left(90)
    a.forward(100)
    a.end_fill()
    turtle.done() # print(a) types = it prints turtle
    
if GAME == 20:

    b = turtle.Turtle()
    tokens = 100
    while tokens > 0:
        b.forward(50)
        b.left(tokens)
        tokens -= 1

if GAME == 30:

    c = turtle.Turtle()
    tokens = 119
    while tokens > 40:
        c.forward(tokens - 40)
        c.left(tokens)
        if int(tokens%20) == 0:
            c.forward(100)

        tokens -= 1


if GAME == 40:
    
    d = turtle.Turtle()
    tokens = 210
    for i in range(190):
        d.forward(tokens - i)
        d.left(tokens - i)

if GAME == 50:

    e = turtle.Turtle()
    tokens = 170
    for i in range(240):
        e.forward(-tokens + i)
        e.left(tokens - i)
        if (i%2) == 0:
            e.penup()
            e.forward(tokens - i)
            e.right(tokens - i)
            e.pendown()

if GAME == 60:

    f = turtle.Turtle()
    f.color("blue")
    f.speed(10)
    tokens = 170
    for i in range(36):
        f.forward(500)
        f.left(tokens)

if GAME == 70:

    g = turtle.Turtle()
    g.color("blue")
    g.speed(10)
    tokens = 175
    for i in range(1000):
        g.forward(math.sqrt(i)*30)
        g.left(tokens)













turtle.done() # print(a) types = it prints turtle
