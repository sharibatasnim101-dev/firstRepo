stk=[]
while True:
    print("1-push")
    print("2-pop")
    print("3-display")
    ch=input("Enter choice:")
    if ch=="1":
        n=(input("Enter Element to PUSH :"))
        stk.append(n)
    elif ch=="2":
        if stk==[]:
            print("Underflow")
        else:
            p=stk.pop()
            print("Element deleted: ",p)
    elif ch=="3":
        l=len(stk)
        for i in range(l-1,-1,-1):
            print(stk[i])