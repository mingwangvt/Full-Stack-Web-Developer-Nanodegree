import turtle

window = turtle.Screen()
window.bgcolor("red")
brad = turtle.Turtle()
    
def draw_shape(turtle_name, color, distance, shape = "rec", angle = 0, loop = 0):
    brad.shape(turtle_name)
    brad.color(color)

    if shape == "circle":
        brad.circle(distance)
    else:
        i = 0
        while i < loop:
            brad.forward(distance)
            brad.right(angle)
            i+=1

    
draw_shape("turtle", "yellow", 100, angle = 90, loop = 4)
draw_shape("arrow", "blue", 50, "circle")
draw_shape("triangle", "black", 200, angle = 120, loop = 3)
    
window.exitonclick()
