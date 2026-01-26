s=input("Enter String:")
l=len(s)
a=0
end=l
s2=''
while a<l:
    if a==0:
        s2+=s[0].upper()
        a+=1
    elif(s[a]==''and s[a+1]!=''):
        s2+=s[a]
        s2+=s[a+1].upper()
        a+=2
    else:
        s2+=s[a]
        a+=1
    print("Original String: ",s)
    print("Capitalized string: ",s2)