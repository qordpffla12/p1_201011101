try:
    fin1=open('python.txt','a')
    fin2=open('outputNumbe.txt','r')
    for line in fin2:
        fin1.write(line)
    fin1.close()
    fin2.close()
except Exception as e:
    print e