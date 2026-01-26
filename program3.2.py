def interest(p,rate=0.08,time=3):
    return p*rate*time
#main
p=float(input("Enter principal amount: "))
print("Simple interest with default ROI nad time values is: ")
si1=interest(800,time=5)
print("Rs.",si1)
roi=float(input("Enter rate of interest(ROI): "))
TIME=int(input("Enter time in years: "))
print("Simplr interest with provided ROI and Time values is: ")
si2=interest(p,TIME,roi/100)
print("Rs.",si2)