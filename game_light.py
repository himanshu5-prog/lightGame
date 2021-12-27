import turtle

def getRow (x):
    return x%10

def getCol (x):
    return x/10

arrayLight = [0 for i in range(100)]
num = 100
turtleList = [turtle.Turtle() for i in range(num)]

win = turtle.Screen()
win.title ("Lights out")
win.bgcolor("black")
win.setup(width=800, height = 800)
win.tracer(0)
turtle.setworldcoordinates(-20, -20, 600, 600)
#arrayLight[23] = 1
mouseClick = 0
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
pen2.goto (250, 500)
pen2.write (" Change color of all LEDs to blue from green", align="center", font=("Courier", 20, "normal"))

win.onclick(getNewList,2)
win.onclick(getNewList_2, 3)
win.onclick(flip, 1)
while True:
    win.update()
        
