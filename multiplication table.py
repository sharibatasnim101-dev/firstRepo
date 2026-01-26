# Multiplication Table
n=int(input("enter a number: "))
print("The multiplication table of ",n,"is:")
for i in range (1,11):
    a=n*i
    print(n,"x",i,"=",a)