allData=[["English","Math"], [100,200], [200,200], [100,300]]
data=allData[1:]
engSum=0
engAverage=0
mathSum=0
mathAverage=0
for i in range(0,len(data)):
    engSum += data[i][0]
    mathSum += data[i][1]
engAverage= engSum/3
mathAverage= mathSum/3
print "Sum of English:",engSum,"Average of English:",engAverage
print "Sum of math:",mathSum,"Average of math:",mathAverage
