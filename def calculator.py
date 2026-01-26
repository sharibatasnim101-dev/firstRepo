def calc(x,y):
    sum=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return sum,sub,mul,div
n1=int(input("Enter 1st Number: "))
n2=int(input("Enter 2nd Number: "))
sum,sub,mul,div=calc(n1,n2)
print("Sum",sum)
print("Subraction:",sub)
print("Multiplication: ",mul)
print("Division: ",div)