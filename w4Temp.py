fc = raw_input("F or C?: ")
temp = raw_input("Insert temperature: ")

if(fc =='F'):
    print ((float(temp)-32)/1.8)
    
elif(fc=='C'):
    print (float(temp)*1.8+32)
    
else:
    print('You entered wrong temperature')