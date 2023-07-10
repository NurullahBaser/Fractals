import turtle
import random

#
# SETTINGS 
#
fibo_count = 12 #number of fibonacci (it is recommended to 12)
multiplication_coefficient = 5 #fibonacci numbers are multiplied by this number because they are not of sufficient size.
pen_color = "black" #you can set the color to string color or hexadecimal colors.(For example "black" or "#33cc8c")
isRandomColor = True # if you want each fibo to be drawn in a random color, you can do it true
speed = 10 #speed of pen (>10 is max speed if you want)

#TRY f_c = 12 & m_c = 5 (best) , f_c = 13 m_c = 3 , f_c = 14 & m_c = 2 , f_c = 15 , m_c = 1.3

fibo = [1,1] #The list of the fibonacci nums

for i in range(2,fibo_count): # calculate all fibonacci nums
    fibo.append(fibo[i-2]+fibo[i-1])
fibo.reverse()


window = turtle.Screen() # Creat window for setup width and height
window.setup(width=1400, height=900)
window.tracer()

t = turtle.Turtle() #Creat turtle
t.speed(speed)
t.penup()
t.pencolor(pen_color)
t.pensize(3)

text = turtle.Turtle() #Creat turtle for texting
text.speed(100)
text.penup()
text.pencolor(pen_color)
text.pensize(3)
text.hideturtle()

def getRandomColorCode(): #creates random color codes for example #34ca8f
    return "#"+''.join([random.choice("0123456789abcdef") for i in range(6)])

def checkColor(): #checks the isRandomColor and sets new color for turtle and text
    if isRandomColor:
        pen_color = getRandomColorCode()
    t.pencolor(pen_color)
    text.pencolor(pen_color)

def drawRadius(len,angle,pos): #draw radius of circle 
    t.setheading(angle)
    t.forward(len)
    t.setheading(angle-90)
    t.forward(len)
    t.penup()
    t.goto(pos)
   

def draw(len,angle): #draws the quarter circle and write its lenght
    checkColor()
    t.setheading(angle)
    t.pendown()
    t.circle(len,-45)
    text.goto(t.pos())
    text.write(f"{int(len//multiplication_coefficient) }",align="center", font=("Courier",15,"bold"))
    t.circle(len,-45)
    drawRadius(len,angle,t.pos())


angle = -90
t.goto(-fibo[0]/2*multiplication_coefficient-fibo[1]/2*multiplication_coefficient,-fibo[0]/2*multiplication_coefficient) # to center the screen

for i in fibo:
    draw(i*multiplication_coefficient,angle)
    angle-=90

t.hideturtle()
turtle.done()