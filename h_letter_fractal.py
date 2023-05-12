import turtle
from queue import Queue

# A CODE THAT GENERATES H FRACTAL

#
# SETTINGS 
#
pen_size = 10 # thickness of first h (it is recommended to 10)
h_size = 300 # size of first h (it is recommended to 300)
num_of_layer = 6 # number of h layers (it is recommended to 6)

queue = Queue() # The queue of the vertex coordinates

t = turtle.Turtle() # Pen turtle
t.speed(100)
t.penup()
t.pensize(pen_size)
t.goto(0,-375)
t.write(f"The number of H written is:", align="center", font=("Courier",30,"normal"))

text = turtle.Turtle() # Text turtle
text.hideturtle()
text.penup()
text.goto(370,-375)

queue.put((0,0)) # Add the coordinates of the first H shape to the queue


# Define a function to draw an H shape at a given coordinate
def setH(cor): 

    # Draw the left line of the H shape and add its endpoints to the queue
    goWithoutPen((cor[0] - h_size/2, cor[1] + h_size/2))
    queue.put(t.position()) # top left corner
    go(270,h_size)
    queue.put(t.position()) # bot left corner

    # Draw the middle line of the H shape
    goWithoutPen((cor[0] - h_size/2, cor[1]))
    go(0,h_size)

    # Draw the right line of the H shape and add its endpoints to the queue
    goWithoutPen((cor[0] + h_size/2, cor[1] + h_size/2))
    queue.put(t.position()) # top right corner
    go(270,h_size)
    queue.put(t.position()) # bot right corner


# Define a function to move the turtle to a given coordinate without drawing
def goWithoutPen(cor):
    t.penup()
    t.goto(cor)
    t.pendown()


# Define a function to move the turtle a given distance in a given direction
def go(x,len):
    t.setheading(x)
    t.forward(len)

# Define a function to write the value of `num_of_h` at the center of the screen
def writeNumber():
    text.clear()
    text.write(f"{num_of_h}", align="center", font=("Courier",30,"normal"))


# Initialize variables for tracking the current layer, the number of H shapes drawn,
# and the number of H shapes needed for the next layer
current_layer = 0
num_of_h_for_next_layer = 1
num_of_h = 0


while current_layer < num_of_layer:
    setH(queue.get()) # Draw an H shape at the next coordinate in the queue
    num_of_h += 1
    writeNumber()

    # If the number of H shapes drawn equals the number needed for the next layer,
    # update the tracking variables and adjust the size and thickness of the turtle's pen
    if(num_of_h == num_of_h_for_next_layer):
        current_layer += 1
        num_of_h_for_next_layer += 4**current_layer
        h_size /=2
        pen_size /=1.5
        t.pensize(pen_size)

turtle.done()
