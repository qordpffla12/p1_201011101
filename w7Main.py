def drawSquareAtSave(size,pos):
    tracks=list()
    t1.penup()
    t1.goto(pos)
    t1.pendown()
    for i in range(0,4):
        t1.fd(size)
        t1.left(90)
        tracks.append(t1.pos())
    return tracks

def drawSquareFrom(tracks):
    t1.penup()
    t1.goto(tracks[0])
    t1.pendown()
    t1.goto(tracks[1])
    t1.goto(tracks[2])
    t1.goto(tracks[3])
    t1.goto(tracks[0])

def saveTracks():
    tracks=list()
    t1.penup()
    t1.goto(-400,300)
    tracks.append(t1.pos())
    t1.pendown()
    t1.right(90)
    t1.fd(400)
    tracks.append(t1.pos())
    t1.backward(150)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(150)
    tracks.append(t1.pos())
    t1.right(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90)
    t1.right(90)
    t1.right(90)
    t1.fd(200)
    tracks.append(t1.pos())
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(100)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(200)
    tracks.append(t1.pos())
    
    return tracks

def replayTracks(tracks):
    t1.penup()
    t1.goto(tracks[0])
    t1.pendown()
    for i in range (1,11):
        t1.goto(tracks[i])

def lab7():
    drawSquareAtSave(100,(100,100))

    x1=list()
    x1.append((0,0))
    x1.append((100,0))
    x1.append((100,100))
    x1.append((0,100))

    drawSquareFrom(x1)

    wn=turtle.Screen()
    t1=turtle.Turtle()
    t1.speed(1)
    t1.pencolor("Red")
    beforeTracks=list()

    beforeTracks=saveTracks()
    replayTracks(beforeTracks)
def main():
	lab7()

if __name__=="__main__":
    main()