# x=4
# print(x)
# def hello():
#     print("hello my friend")
#     print(f"global x is {x}")
# hello()

# def hello():
#     x=4
#     print("hello my friend")
#     print(f"global x is {x}")
# hello()
# print(x)throws error bc x is local variable


def hello():
    global x
    x=4
    print("hello my friend")
    print(f"global x is {x}")
hello()
print(x) 
# not throws error