my_pt={'a':(4,3),'b':(1,2),'c':(5,1)}
highest=[0,0]
init=0
for a in range(2):
    init=0
    for b in my_pt.keys():
        val=my_pt[b][a]
        if init==0:
            highest[a]=val
        init+=1
        if val>highest[a]:
            highest[a]=val
    print("Maximum Value at index(my-pt,",a,")=",highest[a])
