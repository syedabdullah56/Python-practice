f=open("myfile.txt",'r')
while True:
    line=f.readline()
    print(line)
    if not line:
        print(line,type(line))
        break
        print(line)
g=open("myfile2.txt",'w')
lines=['line 1 \n','line 2 \n ','line 3 \n' ]
g.writelines(lines)
g.close()