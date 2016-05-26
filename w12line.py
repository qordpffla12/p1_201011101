import time

timeEdited=time.strftime('%Y-%m-%d %H:%M:%S')
editor="jsl"
edited="[{0} edited {1}]".format(editor,timeEdited)

fin=open('output.txt','r')
fout=open('outputUpper.txt','w')

for words in fin:
    toPrint=words
    if words.count('line')>=1:
        toPrint="{0}{1}".format(edited,words.replace('line','LINE'))
    fout.write(toPrint)

fin.close()
fout.close()