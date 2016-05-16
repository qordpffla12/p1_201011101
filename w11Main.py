import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
line=turtle.Turtle()
wn.bgpic("myMaze.gif")

def keyup():
    t1.fd(50)
def keydown():
    t1.backward(50)
def keyright():
    t1.right(90)
def keyleft():
    t1.left(90)

def mousegoto(x,y):
    t1.setpos(x,y)

def isArrived(x,y):
    t1.setpos(x,y)
    if t1.xcor()>=0 and t1.xcor()<=100 and t1.ycor()==0:
        print "you arrived"
def addKeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyleft,"Left")
    wn.onkey(keyright,"Right")
    wn.onkey(wn.bye,"q")

def addMouse():
    wn.onclick(mousegoto)
    wn.onclick(isArrived)

def lab11():
    line.goto(100,0)
    t1.penup()
    t1.goto(-350, 350)
    t1.pendown()
    addKeys()
    addMouse()
    wn.listen()
    turtle.mainloop()

lab11()