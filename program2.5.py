str=input("Enter a String: ")
char=input("Enter a letter: ")
if char in str:
    count=0
    for a in str:
        if a!=char:
            count=count+1
        else:
            break
    print(char,"is at index",count,"in",str)
else:
    print(char,"is NOT in",str)