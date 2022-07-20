import turtle, random

a = turtle.Turtle()
a.speed(0)
colorlist = ['black',"pink","red","blue","gold","brown","aquamarine2","coral3","cyan2","hotpink","firebrick1","maroon2","RoyalBlue2","tomato","snow2"]

for i in range(300):
    if i < 180:
        a.color(random.choice(colorlist))
        a.forward(i)
        a.right(96)
    else:
        a.color(random.choice(colorlist))
        a.forward(i)
        a.right(91)

turtle.done()