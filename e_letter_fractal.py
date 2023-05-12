import turtle
from queue import Queue

# A CODE THAT GENERATES E FRACTAL

#
# SETTINGS 
#
pen_size = 10 # thickness of first e (it is recommended to 10)
e_size = 243 # size of first e (it is recommended to 243)
num_of_layer = 7 # number of e layers

queue = Queue() # The queue of the vertex coordinates

t = turtle.Turtle()
t.speed(100)
t.penup()
t.pensize(pen_size)

queue.put((-200,0)) # Add the coordinates of the first E shape to the queue


# Define a function to draw an E shape at a given coordinate
def setE(cor): 

    # Draw the first vertical line of the E shape and add its endpoint to the queue
    reset(cor)
    go(90)
    go(0)
    queue.put(t.position())

    # Draw the second vertical line of the E shape and add its endpoint to the queue
    reset(cor)
    go(0)
    queue.put(t.position())

    # Draw the third vertical line of the E shape and add its endpoint to the queue
    reset(cor)
    go(-90)
    go(0)
    queue.put(t.position())


# Define a function to move the turtle to a given coordinate
def reset(cor):
    t.penup()
    t.goto(cor)
    t.pendown()


# Define a function to move the turtle a given distance in a given direction
def go(x):
    t.setheading(x)
    t.forward(e_size)


# Initialize variables for tracking the current layer, the number of E shapes drawn,
# and the number of E shapes needed for the next layer
current_layer = 0
num_of_e_for_next_layer = 1
num_of_e = 0

while current_layer < num_of_layer:
    setE(queue.get()) # Draw an E shape at the next coordinate in the queue
    num_of_e += 1

    # If the number of E shapes drawn equals the number needed for the next layer,
    # update the tracking variables and adjust the size and thickness of the turtle's pen
    if(num_of_e == num_of_e_for_next_layer):
        current_layer += 1
        num_of_e_for_next_layer += 3**current_layer
        e_size /=3
        pen_size /=2
        t.pensize(pen_size)

turtle.done()
