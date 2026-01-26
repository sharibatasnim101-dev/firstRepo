#to find Factorial
n=int(input("enter: "))
fact=1
if n>=1:
    for i in range(1,n+1):
        fact*=i
print(fact)