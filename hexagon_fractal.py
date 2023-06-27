import turtle
import random

#
# SETTINGS 
#
dot_size = 5 #dot size (it is recommended to try 2 and 5.)
hexagon_size = 400 #hexagon size (it is recommended to 400)
number_of_operations = 50000 #you can increase it to see a clearer image
pen_color = "black" #you can set the color to string color or hexadecimal colors.(For example "black" or "#33cc8c")

vertex = [] #The list of the vertex coordinates

t = turtle.Turtle() #Creat turtle
t.speed(100)
t.penup()
t.pencolor(pen_color)

t.goto(0,0) #Set turtle to first vertex
t.setheading(60)
t.forward(hexagon_size)

t.pendown()
for i in range(0,6): #Draw the hexagon and creat the vertex points
    t.setheading(180+i*60)
    t.forward(hexagon_size)
    vertex.append(t.position())
t.penup()

#Creat first dot into middle of hexagon
#(it doesn't matter if it's in the middle or not. It is enough to be inside the hexagon)
coordinates = (0,0)
t.goto(coordinates)
t.dot(dot_size)

for i in range(1, number_of_operations):
    selected_vertex = random.randint(0, 5) # Select a random vertex index
    
    # Calculate the new coordinates. New coordinates 2 times closer the vertex than current coordinates.
    coordinates = (
        (coordinates[0] + vertex[selected_vertex][0]*2) / 3,
        (coordinates[1] + vertex[selected_vertex][1]*2) / 3
    )
    t.goto(coordinates)
    t.dot(dot_size)

turtle.done()