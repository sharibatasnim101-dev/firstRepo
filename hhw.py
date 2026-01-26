"""value=30
for res in range(0,value):
    if res%4==0:
       print(res*4)
    elif res%5==0:
       print(res+3)
    else:
        print(res+10)"""

"""def fun(s, ch):
  n=len(s)
  m=""
  for i in range(0,n):
    if (s[i].islower()):
      m=m+s[i-1]
    elif (s[i].isdigit()):
      m=m+ch
    elif(s[i].isupper()):
      m=m+s[i].lower()
    else:
      m=m+s[i-1]
      print(m)
fun('Mind100@Work!','*')"""

"""def change_list(ar,c):
 for i in range(1,c):
   ar[i-1]+=ar[i]
def main():
 L=[3,4,5]
 L1=[10,20,30,40]
 L2=[900,1200]
 change_list(L,3)
 change_list(L1,4)
 change_list(L2,2)
 for i in range(0,3):
   print(L[i],end='#')
 print()
 for i in range(0,4):
   print(L1[i],end='@')
 print()
 for i in range(0,2):
   print(L2[i],end='$') 
main()"""


import random
PICKER = random.randint(0, 3)
COLOR = ["BLUE", "PINK", "GREEN", "RED"]
for I in COLOR :
 for J in range (1, PICKER):
   print (I, end = " ")
print ()