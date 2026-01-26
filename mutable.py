def myFunction(mylist):
    print("List received:",mylist)
    mylist.append(8)
    mylist.extend([5,8,7,3])
    return
list1=[1,7]
myFunction(list1)
print("List after function call: ",list1)