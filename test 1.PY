fact=1
N=int(input("Enter number: "))
if N>=0:
    for i in range(1,N+1):
        fact*=i
print("Factorial: ",fact)