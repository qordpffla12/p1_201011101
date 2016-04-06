import random

def upDown(begin, end):
    rn = random.randrange(begin, end, 1)
    num = 0
    count = 0

    while num != rn:
        num = int(raw_input("enter num: "))
        count = count+1

        if num < rn:
            print 'up'
        elif num > rn:
            print 'down'
        else:
            print 'right', count

upDown(1,100)