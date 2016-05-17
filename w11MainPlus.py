import turtle
import math

wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()
#wn.bgpic("myMaze.gif")

line=[(200,0),(300,200)]
coord=[(0,200),(100,300)]
radius=50
circlePos=(200,200)

def drawLine():
    t2.penup()
    t2.goto(200,0)
    t2.pendown()
    t2.fd(100)
    t2.hideturtle()

def drawRectangle():
    t3.penup()
    t3.goto(0,200)
    t3.pendown()
    for i in range(0,4):
        t3.fd(100)
        t3.left(90)
    t3.hideturtle()
    
def drawCircle():
    t4.penup()
    t4.goto(circlePos)
    t4.pendown()
    t4.circle(radius)
    t4.hideturtle()

def keyup():
    pt=t1.pos()
    t1.fd(50)
    if isInRectangle(pt, coord)or isInCircle(pt, radius, circlePos) or isOnLine(pt,line):
        t1.write("You arrived")
def keydown():
    pt=t1.pos()
    t1.backward(50)
    if isInRectangle(pt, coord)or isInCircle(pt, radius, circlePos) or isOnLine(pt,line):
        t1.write("You arrived")
def keyright():
    t1.right(90)
def keyleft():
    t1.left(90)

def mousegoto(x,y):
    t1.setpos(x,y)
    pt=t1.pos()
    if isInRectangle(pt, coord)or isInCircle(pt, radius, circlePos) or isOnLine(pt,line):
        t1.write("You arrived")

def isInRectangle(curpos,coord):
    xs=coord[0][0]
    xe=coord[1][0]
    ys=coord[0][1]
    ye=coord[1][1]
    if xs < xe and ys < ye:
        return xs <= curpos[0] <= xe and ys <= curpos[1] <= ye
    elif xs > xe and ys < ye:
        return xe <= curpos[0] <= xs and ye <= curpos[1] <= ys
    elif xs < xe and ys > ye:
        return xs <= curpos[0] <= xe and ys <= curpos[1] <= ys
    else:
        return xe <= curpos[0] <= xs and ys <= curpos[1] <= ye
    
def isInCircle(curpos, radius, pos):
    if curpos[1]<= pos[1]:
        dist = math.sqrt(math.pow(curpos[0]-pos[0], 2) + math.pow(curpos[1]-pos[1], 2))
    else:
        dist = math.sqrt(math.pow(curpos[0]-pos[0], 2) + math.pow(pos[1]-curpos[1], 2))
    if (dist<=radius):
        return True
    else:
        return False

def isOnLine(curpos,line):
    xs=line[0][0]
    xe=line[1][0]
    ys=line[0][1]
    ye=line[1][1]
    if xs < xe and ys < ye:
        return xs <= curpos[0] <= xe and ys <= curpos[1] <= ye
    elif xs > xe and ys < ye:
        return xe <= curpos[0] <= xs and ye <= curpos[1] <= ys
    elif xs < xe and ys > ye:
        return xs <= curpos[0] <= xe and ys <= curpos[1] <= ys
    else:
        return xe <= curpos[0] <= xs and ys <= curpos[1] <= ye
    
def addKeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyleft,"Left")
    wn.onkey(keyright,"Right")
    wn.onkey(wn.bye,"q")

def addMouse():
    wn.onclick(mousegoto)

def lab11():
    drawLine()
    drawRectangle()
    drawCircle()
    addKeys()
    addMouse()
    wn.listen()
    turtle.mainloop()

def main():
     lab11()

if __name__=="__main__":
     main()