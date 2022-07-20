import turtle
import random

a = turtle.Turtle()

# line = 100
# for mo in range(5):
#     for time in range(90):
#         for draw in range(5):
#             a.forward(line)
#             a.rt(144)
#         a.rt(4)
#     line +=50
colorlist = ['red','black','blue','green','brown']
a.speed(0)
a.rt(90)

for time in range(40):
    randnum = random.randint(3,20)
    a.color(random.choice(colorlist))
    for line in range(randnum):
        a.forward(50)
        a.rt(180-(randnum-2)*180/randnum)
    a.fillcolor(random.choice(colorlist))

turtle.done()