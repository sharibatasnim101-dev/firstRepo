info={
    'Riya':'CS',
    'Mark':'Eco',
    'preet':'Eng',
    'kamal':'EVS'
    }
inp=input("Enter value to be searched: ")
for a in info:
        if info[a].upper()==inp.upper():
            print("The key of the given value is",a)
            break
else:
    print("Given value doesn't exist in dictionary")