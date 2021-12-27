import turtle
import random

def getRow (x):
    return x%10

def getCol (x):
    return x/10

#arrayLight = [0 for i in range(100)]
arrayLight = [0 for i in range(100)]

## Random initialisation 

for index in range(100):
    arrayLight[index] = random.randrange(0,2)
num = 100
turtleList = [turtle.Turtle() for i in range(num)]

win = turtle.Screen()
win.title ("Lights out")
win.bgcolor("black")
win.setup(width=800, height = 800)
win.tracer(0)
turtle.setworldcoordinates(-50, -50, 700, 700)

pen3 = turtle.Turtle()
pen3.speed(0)
pen3.color ("white")
pen3.penup()
pen3.hideturtle()
pen3.goto (300, 475)
    
def getNewList (x,y):
    row = y/50
    col = x/50
    print ("row: ", round(row), " col: ", round(col), " x: ", x, " y: ", y) 
    index = 10* round(row) + round(col)
    print ("index: ", index)
    turtleList[index].color("blue")
    arrayLight[index] = 1

def getNewList_2 (x,y):
    row = y/50
    col = x/50
    print ("row: ", int(row), " col: ", int(col), " x: ", x, " y: ", y) 
    index = 10* round(row) + round(col)
    print ("index: ", index)
    turtleList[index].color("green")
    arrayLight[index] = 0

def flip ( x, y):
    row = (y)/50
    col = (x)/50
    print ("row: ", round(row), " col: ", round(col), " x: ", x, " y: ", y) 
    #index = 10* int(row) + int(col)
    index = 10* round(row) + round(col)
    print ("index: ", index)
    
    if arrayLight[index] == 1:
        turtleList[index].color("green")
        arrayLight[index] = 0 
    elif arrayLight[index] == 0:
        turtleList[index].color("blue")
        arrayLight[index] = 1
    
    targetIndex = index + 1
    if ( index % 10 != 9):
        if arrayLight[targetIndex] == 1:
            turtleList[targetIndex].color("green")
            arrayLight[targetIndex] = 0 
        elif arrayLight[targetIndex] == 0:
            turtleList[targetIndex].color("blue")
            arrayLight[targetIndex] = 1
    
    targetIndex = index - 1
    if (targetIndex >= 0 ):
        if (index % 10 != 0):
            if arrayLight[targetIndex] == 1:
                turtleList[targetIndex].color("green")
                arrayLight[targetIndex] = 0 
            elif arrayLight[targetIndex] == 0:
                turtleList[targetIndex].color("blue")
                arrayLight[targetIndex] = 1
   
    targetIndex = index + 10
    
    if (targetIndex < 100):
        if arrayLight[targetIndex] == 1:
            turtleList[targetIndex].color("green")
            arrayLight[targetIndex] = 0 
        elif arrayLight[targetIndex] == 0:
            turtleList[targetIndex].color("blue")
            arrayLight[targetIndex] = 1
    
    targetIndex = index - 10
    
    if (targetIndex >= 0):
        if arrayLight[targetIndex] == 1:
            turtleList[targetIndex].color("green")
            arrayLight[targetIndex] = 0 
        elif arrayLight[targetIndex] == 0:
            turtleList[targetIndex].color("blue")
            arrayLight[targetIndex] = 1
    greenCount = 0
    blueCount = 0

    for index1 in range(100):
        if (arrayLight[index1] == 0): greenCount += 1
        elif (arrayLight[index1] == 1): blueCount += 1

    print ("Blue LED: ", blueCount, " | green LEDs: ", greenCount)
    
    pen3.clear()    
    pen3.write (" Blue LED count: {}, Green LED count: {}".format(blueCount, greenCount), align="center", font=("Courier", 20, "normal"))
    
for index in range(num):
    obj = turtleList[index]
    obj.speed(0)
    obj.shape("circle")
    
    if arrayLight[index] == 0:
        obj.color("green")
    elif arrayLight[index] == 1:
        obj.color("blue")
    
    obj.penup()
    
    row = getRow(index)
    col = getCol(index)
    
    x_coord = 50*int(row)
    y_coord = 50*int(col)
    obj.goto(x_coord, y_coord)

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color ("white")
pen2.penup()
pen2.hideturtle()
pen2.goto (350, 500)
pen2.write (" Change color of all LEDs to blue from green", align="center", font=("Courier", 20, "normal"))

win.onclick(getNewList,2)
win.onclick(getNewList_2, 3)
win.onclick(flip, 1)

maxGreenCount = 0
maxBlueCount = 0

pen4 = turtle.Turtle()
pen4.speed(0)
pen4.color ("white")
pen4.penup()
pen4.hideturtle()
#pen3.clear()
pen4.goto (650, 575)
while True:
    greenCount = 0
    blueCount = 0
    for index_2 in range(100):
        if ( arrayLight[index_2] == 0) : greenCount += 1
        elif (arrayLight[index_2] == 1): blueCount += 1
    
    maxGreenCount = max(maxGreenCount, greenCount)
    maxBlueCount = max (maxBlueCount, blueCount)
    pen4.clear()
    pen4.write(" max blue count: {}, max green count: {}".format(maxBlueCount, maxGreenCount), align="right", font = ("Courier", 20, "bold"))
    win.update()
        
