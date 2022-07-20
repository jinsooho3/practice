from turtle import Screen, Turtle

DISTANCE = 40

def saddle(t, n, minimum=1):
    assert n % 2 == 1, "n should be odd"

    t.penup()

    for x in range(-n // 2 + 1, n // 2 + 1):
        t.setx(x * DISTANCE)

        for y in range(-n // 2 + 1, n // 2 + 1):
            t.sety(y * DISTANCE)
            t.dot(2 * (minimum + abs(x*2) + abs(y*2)))

screen = Screen()
screen.tracer(False)

turtle = Turtle()
turtle.hideturtle()

saddle(turtle, 7)

screen.tracer(True)
screen.exitonclick()