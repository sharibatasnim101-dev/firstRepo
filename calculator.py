n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
sum=n1+n2
if n2>n1:
    sub=n2-n1
if n1>n2:
    sub=n1-n2
else:
    sub=0
print("Sum: ",sum)
print("Subtract: ",sub)