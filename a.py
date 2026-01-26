def interest(X,Y,Z):
    return X*Y*Z
P=float(input("Enter Principal Amount: "))
R=float(input("Enter Rate of Interest(ROI): "))
T=int(input("Enter Time in years: "))
si=interest(P,R,T)
print("Simple Interest: Rs.",si)