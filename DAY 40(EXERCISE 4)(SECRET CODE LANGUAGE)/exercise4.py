a=input("What you want to convert: \n SECRET CODE TO NORMAL(SCN) OR NORMAL TO SECRET CODE(NSC) \n ENTER SCN OR NSC:")
if (a=="SCN" or a=="scn"):
    b=input("ENTER ANY SECRET CODE YOU WANT TO CONVERT IN NORMAL LANGUAGE:")
    if (len(b)==2):
        f=b[::-1]
        print(f)
    else:    
        c=b[3:-3]
        d=c[::-1]
        print(d)
if (a=="NSC" or a=="nsc"):
    d=input("ENTER ANY NORMAL LANGUAGE YOU WANT TO CONVERT IN SECRET CODE: ")
    if (len(d)==2):
        g=d[::-1]
        print(g)
    else:
        e=(f"ijk{d[::-1]}kij")
    print(e)
       


 