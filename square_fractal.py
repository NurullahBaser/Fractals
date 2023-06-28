import turtle
import math
import random

#
# SETTINGS 
#
square_size = 750 #square size (it is recommended to 750)
number_of_operations = 15 #number of square
pen_color = "black" #you can set the color to string color or hexadecimal colors.(For example "black" or "#33cc8c")
isRandomColor = True # if you want each square to be drawn in a random color, you can do it true
pen_size = 3 #thickness of pen
speed = 100 #speed of pen (max==100)

#You can examine different images by changing the pen thickness and the number of operations

t = turtle.Turtle() #Creat turtle
t.speed(speed)
t.penup()
t.pencolor(pen_color)
t.pensize(pen_size)


hex_string = "0123456789abcdef"
def getRandomColorCode(): #creates random color codes
    return "#"+''.join([random.choice(hex_string) for i in range(6)])

def drawRectangle(coordinates,square_size,heading): #Draw a square with given parameters.
    if isRandomColor:
        t.pencolor(getRandomColorCode())
    t.goto(coordinates)
    t.pendown()
    for i in range(0,4):
        drawEdge(square_size,heading+i*90)
    t.penup()

def drawEdge(square_size,heading): #Draw a square edge
    t.setheading(heading)
    t.forward(square_size)


angle = 180 # first angle
coordinates = (square_size/2,square_size/2) #first coordinate

for i in range(0,number_of_operations):
    drawRectangle(coordinates,square_size,angle) #draw square
    #set new coordinate and new angle from current angle
    if(angle == 180):
        coordinates = (0,square_size/2)
        angle = 225
    else:
        coordinates = (square_size*math.sqrt(2)/4,square_size*math.sqrt(2)/4)
        angle = 180
    square_size *= math.sqrt(2)/2 # set the next square size


t.hideturtle()
turtle.done()