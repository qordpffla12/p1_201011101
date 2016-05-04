%matplotlib inline

import matplotlib
import matplotlib.pyplot as plt
d=dict()

def charCount(word):
    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    print d

def charGraph(word):

    plt.bar(range(len(d)), d.values(), align='center')
    plt.xticks(range(len(d)),list(d.keys()))
    plt.show()

def alphaDigit(word):
    e=dict()
    e['alpha']=0
    e['digit']=0
    for c in word:
        if c.isalpha()==True:
            e['alpha']+=1
        elif c.isdigit()==True:
            e['digit']+=1    
    print e     
    
    
    plt.bar(range(len(e)), e.values(), align='center')
    plt.xticks(range(len(e)), list(e.keys()))
    plt.show()

def charCountGraph():
    word='sangmyung university'
    charCount(word)
    charGraph(word)

def AD():
    word="7 hongji, Hongro"
    alphaDigit(word)

def objectInHome():
    myHome=set(['TV', 'phone', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'])
    frHome=set(['coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'])
    
    print "1"
    print myHome.union(frHome)
    print "2"
    print myHome-frHome
    print "3"
    print frHome-myHome
    print "4"
    print myHome.intersection(frHome)
    
    x=dict()
    for c in myHome.union(frHome):
        if c not in myHome&frHome:
            x[c]=1
        else:
            x[c]=2
            
    print "5"
    print x

def lab9():

    charCountGraph()
    AD()
    objectInHome()

def main():
    lab9()

if __name__=="__main__":
    main()