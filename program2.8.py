alist=[15,61,13,27,3,53,2]
print("Original list is: ",alist)
n=len(alist)
for i in range(n):
    for j in range(0,n-i-1):
        if alist[j]>alist[j+1]:
            alist[j],alist[j+1]=alist[j+1],alist[j]
print("List after sorting: ",alist)
