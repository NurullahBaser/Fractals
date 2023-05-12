import turtle
import random

# A CODE THAT GENERATES SNOWFLAKES (it takes a whiles)

#
# SETTINGS
#
dot_size = 5 # dot size (it is recommended to try 2 and 5.)
pentagon_size = 300 # pentagon size (it is recommended to 300)
number_of_operations = 50000 # you can increase it to see a clearer image

vertex = [] # The list of the vertex coordinates

t = turtle.Turtle()
t.speed(100)
t.penup()

for i in range(0,5): # Creat the vertex points of the pentagon
    t.goto(0,0)
    t.setheading(90+72*i)
    t.forward(pentagon_size)
    t.dot(dot_size)
    vertex.append(t.position())


# Creating first dot inside of the pentagon
coordinates = ((vertex[0][0] + vertex[3][0])/2 , (vertex[0][1] + vertex[3][1])/2)
t.goto(coordinates) 
t.dot(dot_size)


# Select a random vertex index between 0 and 4
selected_vertex = random.randint(0, 4)
current = selected_vertex


for i in range(1, number_of_operations):
    # Make sure the newly selected vertex is different from the current vertex
    while selected_vertex == current:
        selected_vertex = random.randint(0, 4)
    current = selected_vertex
    
    # Calculate the midpoint coordinates by averaging the current coordinates with the selected vertex's coordinates
    coordinates = (
        (coordinates[0] + vertex[selected_vertex][0]) / 2,
        (coordinates[1] + vertex[selected_vertex][1]) / 2
    )
    t.goto(coordinates)
    t.dot(dot_size)


turtle.done()