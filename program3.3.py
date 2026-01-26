def arCalc(x,y):
    return x+y,x-y,x*y,x/y,x%y
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
add,sub,mult,div,mod=arCalc(num1,num2)
print("Sum of given numbers:",add)
print("Difference of the numbers:",sub)
print("Product of the numbers:",mult)
print("Division of the numbers:",div)
print("Modulo of the given numbers:",mod)