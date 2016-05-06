%matplotlib inline

import matplotlib
import matplotlib.pyplot as plt

jongro=[74425, 76326]
joonggu=[61164, 61636]
yongsan=[109688, 115744]
seongdong=[144796, 146776]
gwangjin=[174996, 181676]
dongdaemoon=[177841, 177434]
joongrang=[204630, 205980]
seongbook=[223373, 232245]
gangbook=[161055, 166130]
dobong=[171576, 176735]
nowon=[279169, 293772]
eunpyeong=[239450, 251066]
seodaemoon=[148690, 156510]
mapo=[182977, 196992]
yangcheon=[237792, 242641]
gangseo=[283869, 296762]
guro=[209344, 210282]
geumcheon=[118965, 114441]
yeongdeungpo=[186503, 186856]
dongjak=[195734, 203014]
gwanak=[254381, 249472]
seocho=[212401, 229111]
gangnam=[271654, 295354]
songpa=[319197, 335045]
gangdong=[229829, 231671]

def caculatePop():
    total=[jongro,joonggu,yongsan,seongdong,gwangjin,dongdaemoon,joongrang,seongbook,gangbook,dobong,nowon,eunpyeong,seodaemoon,mapo,yangcheon,gangseo,guro,geumcheon,yeongdeungpo,dongjak,gwanak,seocho,gangnam,songpa,gangdong]
    guTotal=[]
    maleSum=0
    femaleSum=0
    maleAverage=0
    femaleAverage=0
    
    for i in range (0,len(total)):
        maleSum+=total[i][0]
        femaleSum+=total[i][1]
        guTotal.append(total[i][0]+total[i][1])
    maleAverage=maleSum/25
    femaleAverage=femaleSum/25

    dictGuTotal=({'jongro':guTotal[0],'joonggu':guTotal[1],'yongsan':guTotal[2],'seongdong':guTotal[3],'gwangjin':guTotal[4],'dongdaemoon':guTotal[5],'joongrang':guTotal[6],'seongbook':guTotal[7],'gangbook':guTotal[8],'dobong':guTotal[9],'nowon':guTotal[10],'eunpyeong':guTotal[11],'seodaemoon':guTotal[12],'mapo':guTotal[13],'yangcheon':guTotal[14],'gangseo':guTotal[15],'guro':guTotal[16],'geumcheon':guTotal[17],'yeongdeungpo':guTotal[18],'dongjak':guTotal[19],'gwanak':guTotal[20],'seocho':guTotal[21],'gangnam':guTotal[22],'songpa':guTotal[23],'gangdong':guTotal[24],})

    print maleSum
    print femaleSum
    print maleAverage
    print femaleAverage
    print guTotal

    plt.bar(range(len(dictGuTotal)), dictGuTotal.values() ,align='center')
    #plt.xticks(range(len(dictGuTotal)),list(dictGuTotal.keys()))
    plt.show()

def lab10():
    caculatePop()

def main():
    lab10()

if __name__="__main__":
    main()