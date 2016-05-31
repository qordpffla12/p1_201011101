data=[1,2,3,4,5,6,7,8,9,10]
fout=open('outputNumber.txt', 'w')
for i in data:
    if i%2==0:
        content='\n'
    else:
        content='\t'
    toPrint="{0}{1}".format(i,content)
    fout.write(toPrint)
fout.close()