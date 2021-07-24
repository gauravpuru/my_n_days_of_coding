import turtle

myturtle = turtle.Turtle()


for i in range(100):

    myturtle.forward(i*5)
    myturtle.left(90)
    myturtle.forward(i*5)

turtle.done()