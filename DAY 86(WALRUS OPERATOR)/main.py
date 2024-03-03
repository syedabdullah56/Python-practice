happy=True
print(happy:=False)
no=[1,2,3,4,5,6,7,8]
# while (n:=len(no))>0:
#     print(no.pop())

while (n:=len(no))>2:
    print(no.pop())

foods=list()
while (n:=input("What food do you like to enter in list:?")) !="quit":
    foods.append(n)
    print(foods)
