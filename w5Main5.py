markTemp = raw_input("insert marks (0~100): ")
marks = float(markTemp)

def computeGrade(marks):
    if(90<=marks and marks<=100):
        grade = 'A'
    elif(80<=marks and marks<90):
        grade = 'B'
    elif(70<=marks and marks<80):
        grade = 'C'
    elif(60<=marks and marks<70):
        grade = 'D'
    else:
        grade = 'F'
    return grade

computeGrade(marks)