# without enumerate function
marks=[12,34,5,99,94,81,79]
index=0
for mark in marks:
    print(mark)
    if (index==3):
        print("ABDULLAH AWESOME")
    index+=1

# with enumerate function
marks=[12,34,5,99,94,81,79]
for index,mark in enumerate(marks):
    print(mark)
    if (index==3):
        print("ABDULLAH AWESOME")

fruits=['mango','banana','apple','pineapple']
for index,fruit in enumerate(fruits):
    print(index,fruit)   

fruits=['mango','banana','apple','pineapple']
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)   