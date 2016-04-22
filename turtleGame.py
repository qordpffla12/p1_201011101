import turtle
import random

#게임공간 세팅
wn=turtle.Screen()
wn.bgcolor("pink")
stadium=turtle.Turtle()
stadium.speed(10)
stadium.penup()
stadium.setpos(-300,-300)
stadium.pendown()
stadium.pensize(2)
for side in range(4):
    stadium.forward(600)
    stadium.left(90)
stadium.hideturtle()

#사용자 세팅
player=turtle.Turtle()
player.penup()
player.setpos(0,-290)
player.shape("circle")

#장애물 세팅
maxObstacles = random.randint(10,20)
obstacles =list()

#획득할 먹이의 모양과 나타날 위치를 랜덤으로 지정
for i in range(maxObstacles):
    obstacles.append(turtle.Turtle())
    obstacles[i].color("blue")
    obstacles[i].shape("circle")
    obstacles[i].penup()
    obstacles[i].speed(0)
    obstacles[i].setposition(random.randint(-300,300), random.randint(300,300))

speed=30

def pressLeft():
    player.setheading(180)
def pressRight():
    player.setheading(360)
def upSpeed():
    global speed
    speed+=10
def downSpeed():
    global speed
    speed-=10

#키보드 입력 세팅
turtle.listen()
turtle.onkey(pressLeft,"Left")
turtle.onkey(pressRight,"Right")
turtle.onkey(upSpeed, "Up")
turtle.onkey(downSpeed, "Down")
    


while obstacles[i].ycor() > -280:
    player.forward(speed)
    player.speed(3)
    
    #장애물이 하늘에서 내려오기
    for i in range(maxObstacles):
        obstacles[i].setheading(270)
        obstacles[i].forward(speed)
        obstacles[i].speed(3)
        
    #player가 벽에 부딪히면 뒤를 돌아보게 설정
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)
