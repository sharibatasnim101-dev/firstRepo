num=int(input("Enter a number (0-999): "))
if num<0 or num>999:
    print("Invalid entry. Please enter number between 0-999.")
else:
    if num<10:
        print("The number",num,"is of 1 digit.")
    else:
        if num<100:
            print("The number is of 2 digit.")
        else:
            print("the number is of 3 digit. ")
