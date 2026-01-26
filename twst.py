try:
    filrname="gynacologist.txt"
    open("gynacologist.txt","w")
except IOError:
    print("File cannot be opened")
else:
    print("File opened properly")
finally:
    print("Yes Done!")

