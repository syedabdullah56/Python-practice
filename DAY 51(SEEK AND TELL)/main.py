# seek
with open("myfile.txt",'r') as f:
    print(type(f))
    f.seek(10)
    data=f.read()
    print(data)
  
f=open('myfile.txt','r')
f.seek(8)
print (f.read())

# tell
print(f.tell())
data1=f.read(5)
print(data1)

# truncate
g=open('sample.txt','w')
print(g.write("MY NAME IS ABDULLAH"))
print(g.truncate(5))
g.close()