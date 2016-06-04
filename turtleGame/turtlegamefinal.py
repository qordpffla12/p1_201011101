import turtle
import random
import math
import time

#플레이어의 이름과 Goal의 갯수 입력받기
name = raw_input("Enter your name: ")
maxGoals = int(raw_input("Enter number of goals: "))

#화면 구성
wn=turtle.Screen()
wn.bgcolor("gray")
wn.tracer(1)

#게임을 진행할 공간 생성
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

#플레이어 생성
player=turtle.Turtle()
player.color("blue")
player.penup()
player.speed(0)

#Goal 생성
goals=[]
for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].penup()
    goals[count].speed(10)
    goals[count].setposition(random.randint(-270,270),random.randint(-270,270))
    if count%2==0:
        goals[count].color("red")
    else:
        goals[count].color("blue")
    goals[count].pendown()
    goals[count].circle(10)
    goals[count].hideturtle()

speed=1
score=0
goalcount=0

#필요함수 구현
def pressLeft():
    player.left(30)
def pressRight():
    player.right(30)
def upSpeed():
    global speed
    speed+=1
def downSpeed():
    global speed
    speed-=1

#플레이어가 장애물을 먹었는가에 대한 함수 구현
def isEaten(t1,t2):
    d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d <10:
        return True
    else:
        return False
    
#키보드 입력 세팅
turtle.listen()
turtle.onkey(pressLeft,"Left")
turtle.onkey(pressRight,"Right")
turtle.onkey(upSpeed, "Up")
turtle.onkey(downSpeed, "Down")
turtle.onkey(wn.bye, "q")

#게임 진행
while True:
    player.forward(speed)
    
    #player가 벽에 부딪히면 뒤를 돌아보게 설정
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)
    
    #player의 화살표 색상 변경 및 score 설정
    for count in range(maxGoals):
        if isEaten(player, goals[count]):
            goals[count].penup()
            goals[count].home()
            goals[count].clear()
            if player.color()!=goals[count].color():
                player.color(goals[count].color()[0])
                score+=2
                goalcount +=1
            else:
                score+=1
                goalcount +=1
            
    #게임 종료 설정(파일 저장 및 screen 종료)
    if goalcount==maxGoals:
        timeEdited=time.strftime('%y-%m-%d %H:%M:%S')
        toPrint="[{0}---{1}:{2}]\n".format(timeEdited,name,score)
        fout=open('ranking.txt','a')
        fout.write(toPrint)
        fout.close()
        wn.bye()