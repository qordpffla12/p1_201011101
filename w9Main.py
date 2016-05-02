%matplotlib inline

import matplotlib
import matplotlib.pyplot as plt
word='sangmyung university'
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

def lab9():

    charCount(word)
    charGraph(word)
def main():
    lab9()

if __name__=="__main__":
    main()