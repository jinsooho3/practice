from turtle import *

color('pink','pink')
pensize(3)
begin_fill()
hideturtle()

def curve():
    for i in range(100):
        right(2)
        forward(2)

left(140)
forward(111)
curve()

left(120)
curve()
forward(111)
end_fill()
mainloop()