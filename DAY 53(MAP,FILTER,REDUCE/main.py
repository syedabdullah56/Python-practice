# without map
def cube(x):
    return x*x*x

l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
newl=[]
for item in l:
    newl.append(cube(item))
print(newl)

# with map function
newlist=list(map(cube,l))
print(newlist)

# filter function
def filterfunction(a):
    return a>4
newlist1=list(filter(filterfunction,l))
print(newlist1)

# reduce
from functools import reduce
numbers=[1,2,3,4,5,6,7,8,9]
sum=reduce(lambda x,y:x+y,numbers)
print(sum)