def double(x):
    return x*2
print(double(10))

double=lambda x:x*2
print(double(9))

def cube(x):
    return x*x*x
print(cube(9))

cube=lambda x:x*x*x
print(cube(6))

average=lambda x,y:(x+y)/2
print(average(9,10))

def apply(fx,value):
    return fx(value)
print(apply(cube,3))
print(apply(cube,11))
print(apply(cube,14))

appl=lambda fx,value:fx(value)
print(appl(cube,19))
print(appl(cube,18))
print(appl(cube,17))
print(appl(cube,16))