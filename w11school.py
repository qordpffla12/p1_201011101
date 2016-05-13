list=[[13.1, 37.1, 39.6, 8.7, 1.5],
      [10.6, 34.6, 39.5, 13.4, 1.9],
      [27.1, 40.0, 28.5, 2.9, 1.5],
      [16.2, 37.8, 38.4, 6.8, 0.8],
      [11.4, 29.8, 39.0, 14.8, 4.9],
      [12.2, 26.5, 42.0, 14.9, 4.4],
      [13.5, 29.7, 43.4, 11.1, 2.4],
      [13.7, 37.6, 43.4, 4.1, 1.2]]
goodList=[]
x=0
for i in range(0,8):
    for j in range(0,2):
        x+=list[i][j]
    goodList.append(x/2)
    x=0

badList=[]
for i in range(0,8):
    for j in range(3,5):
        x+=list[i][j]
    badList.append(x/2)
    x=0
print "교육내용에 대한 만족도 평균:", goodList[0], "       불만족도 평균:", badList[0]
print "교육방법에 대한 만족도 평균:", goodList[1], "       불만족도 평균:", badList[1]
print "교우관계에 대한 만족도 평균:", goodList[2], "      불만족도 평균:", badList[2]
print "교사와의 관계에 대한 만족도 평균:", goodList[3], "  불만족도 평균:", badList[3]
print "시설 및 설비 대한 만족도 평균:", goodList[4], "     불만족도 평균:", badList[4]
print "학교 주변 환경 대한 만족도 평균:", goodList[5], "  불만족도 평균:", badList[5]
print "전공 대한 만족도 평균:", goodList[6], "             불만족도 평균:", badList[6]
print "학교생활에 대한 만족도 평균:", goodList[7], "      불만족도 평균:", badList[7]