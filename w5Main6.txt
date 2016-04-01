def rockScisPaper(tempA, tempB):

    if(tempA =='R'):
        if(tempB == 'R'):
            print "Draw"
        elif(tempB =='S'):
            print "A won"
        elif(tempB =='P'):
            print "A lose"
        else:
            print "You entered wrong information"

    if(tempA =='S'):
        if(tempB == 'R'):
            print "A lose"
        elif(tempB =='S'):
            print "Draw"
        elif(tempB =='P'):
            print "A Won"
        else:
            print "You entered wrong information"

    if(tempA =='P'):
        if(tempB == 'R'):
            print "A won"
        elif(tempB =='S'):
            print "A lose"
        elif(tempB =='P'):
            print "Draw"
        else:
            print "You entered wrong information"
            
tempA = raw_input("insert R or S or P of user A: ")
tempB = raw_input("insert R or S or P of user B: ")
rockScisPaper(tempA,tempB)