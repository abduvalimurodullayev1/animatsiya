import turtle as tr
import colorsys as cs

tr.setup(800, 800)
tr.speed(0)
tr.tracer(10)
tr.width(2)

tr.bgcolor("black")

for j in range(25):
    for i in range(15):
        tr.color(cs.hsv_to_rgb(i / 15, j / 25, 1))
        tr.right(90)
        tr.circle(200 - j * 4, 90)
        tr.left(90)
        tr.circle(200 - j * 4, 90)
        tr.right(180)
        tr.circle(50, 24)
tr.hideturtle()
tr.done()