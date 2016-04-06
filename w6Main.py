def getMultiplesOf3_5(begin,end):
   sum = 0
   for i in range(begin, end):
       if i%3 ==0 or i%5 == 0:
       sum = sum+i
   return sum

def lab6():
	getMultiplesOf3_5(1,1000)

def main():
	lab6()

if __name__=="__main__":
    main()
