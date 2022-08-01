import turtle, random

a = turtle.Turtle()
a.speed(0)
colorlist = ['black',"pink","red","blue","gold","brown","aquamarine2","coral3","cyan2","hotpink","firebrick1","maroon2","RoyalBlue2","tomato","snow2","DeepSkyBlue","IndianRed2","magenta3","PaleTurquoise","salmon","wheat1","OliveDrab"]
turtle.bgcolor('wheat4')
for i in range(300):
    if i < 180:
        a.color(random.choice(colorlist))
        a.forward(i)
        a.right(96)   
    else:
        a.color(random.choice(colorlist))
        a.forward(i)
        a.right(91)
a.setposition(0,0)
for i in range(30):
    for time in range(5):
        a.forward(350)
        a.right(144)
    a.right(12)

turtle.done()