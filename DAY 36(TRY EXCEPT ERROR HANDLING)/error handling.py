a=int(input("Enter any integer:"))
try:
    print(f"MULTIPLICATION TABLE OF{a}is:")
    for i in range(1,11):
        print(f"{int(a)}x{i}={int(a)*i}")
except:
    print("INVALID INPUT")
b=str(input("Enter your name"))
try:
    print(f"My name is {b}")
except:
    print("INVALID INPUT")
d=int(input("ENTER INTEGER BETWEEN 0 TO 2"))
try:
    c=[1,2,3]
    print(c[d])
except:
    print("INVALID INTEGER")
