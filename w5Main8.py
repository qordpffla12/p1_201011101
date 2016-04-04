def getBMI(hei,wei):
    hei = float(raw_input("Insert your height: "))
    wei = float(raw_input("Insert your weight: "))
    bmi = wei/(hei/100*hei/100)
    
    if bmi<18.5:
        res = 'under average'
    elif bmi>=18.5 and bmi <24.9:
        res = 'average'
    elif bmi>=24.9 and bmi <29.9:
        res = 'over average'
    else:
        res = 'biman'
    return res, round(bmi, 2)


def main():
	getBMI(hei,wei)


if __name__=="__main__":
    main()