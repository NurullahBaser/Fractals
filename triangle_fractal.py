import turtle
import random

# A CODE THAT GENERATES TRIANGEL FRACTAL (SIERPINSKI TRIANGE)  (it takes a while)

#
# SETTINGS 
#
dot_size = 5 #dot size (it is recommended to try 2 and 5.)
triangle_size = 300 #triangle size (it is recommended to 300)
number_of_operations = 50000 #you can increase it to see a clearer image


vertex = [] #The list of the vertex coordinates

t = turtle.Turtle()
t.speed(100)
t.penup()

for i in [90,210,330]: #Creat the vertex points of the triangle
    t.goto(0,0)
    t.setheading(i)
    t.forward(triangle_size)
    t.dot(dot_size)
    vertex.append(t.position())

#Creat first dot into middle of triangle 
#(it doesn't matter if it's in the middle or not. It is enough to be inside the triangle)
coordinates = (0,0)
t.goto(coordinates) 
t.dot(dot_size)



for i in range(1, number_of_operations):
    selected_vertex = random.randint(0, 2) # Select a random vertex index (0, 1, or 2)
    
    # Calculate the midpoint coordinates by averaging the current coordinates with the selected vertex's coordinates
    coordinates = (
        (coordinates[0] + vertex[selected_vertex][0]) / 2,
        (coordinates[1] + vertex[selected_vertex][1]) / 2
    )
    t.goto(coordinates)
    t.dot(dot_size)


turtle.done()