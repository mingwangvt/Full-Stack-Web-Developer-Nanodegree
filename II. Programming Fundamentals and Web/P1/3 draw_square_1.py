import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()  ##brad is an object of Turtle, this line of code will call def __init__() inside the class of Turtle
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1)  ##speed range from 0-10,0 fatest,10 fast,6 normal,3 slow, 1 slowest,slower than 0.5 and larger than 10 will set to 0
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    
    window.exitonclick()

draw_square()
    
