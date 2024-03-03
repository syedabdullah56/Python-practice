a=int(input("Enter any value between 5 to 9"))
if (a<5 or a>9):
    raise ValueError("VALUE SHOULD BE BTW 5 AND 9")
b=str(input("ENTER quit:"))
if (b!="quit"):
    raise ValueError("INVALID INPUT")