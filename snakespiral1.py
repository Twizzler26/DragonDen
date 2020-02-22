
import turtle

window = turtle.Screen()

#f08bbd
window.bgcolor("#f08bbd")

window.title("IT'S SPINNING!!")

turtle_pen = turtle.Pen()

#7fdbe3
turtle_pen.pencolor("#7fdbe3")

for counter in range(1000):
    print("counter is", counter)

    turtle_pen.forward(counter)
    turtle_pen.left(45)
    if(counter > 25):
        turtle_pen.pensize(3)

        window.bgcolor("blue")
    else:
        turtle_pen.pensize(2)

        window.bgcolor("red")
