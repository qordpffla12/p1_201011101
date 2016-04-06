def getMultiplesOf3_5(begin,end):
   sum = 0
   for i in range(begin, end):
       if i%3 ==0 or i%5 == 0:
       sum = sum+i
   return sum

def getYoonnyeon(year):
    year =int(raw_input("insert year: "))
    if (year%4 == 0) and (year%100 !=0 or year%400==0):
        res = 'Yoonnyeon'
    else:
        res = 'not Yoonnyeon'
    return res

def lab6():
	getMultiplesOf3_5(1,1000)
	getYoonnyeon(2011)
def main():
	lab6()

if __name__=="__main__":
    main()
