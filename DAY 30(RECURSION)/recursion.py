def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
print(factorial(4))
print(factorial(10))
def fabonaccino(n1):
    if (n1==0):
        return 0
    if (n1==1):
        return 1
    else:
        return fabonaccino(n1-1)+fabonaccino(n1-2)
print(fabonaccino(1))
print(fabonaccino(3))
print(fabonaccino(4))
print(fabonaccino(6))
print(fabonaccino(8))
def sumofn(n2):
    if (n2==0):
        return 0
    if (n2==1):
        return 1
    else:
        return n2+ sumofn(n2-1)
print(sumofn(10))
print(sumofn(5))
print(sumofn(4))
def sumofevenno(n3):
    if (n3==0 or n3==1):
        return 0
    if (n3%2==0):
        return n3+sumofevenno(n3-2)
    else:
        n4 = n3-1
        return n4+sumofevenno(n4-2)

print(sumofevenno(6))
print(sumofevenno(4))
print(sumofevenno(7))



    







    