def separate():
    f=open("Admission.txt","r+")
    l=f.readlines()
    for i in l:
        if 'Science' in i:
            fs=open("Science.txt","a+")
            fs.write(i)
            fs.close()
    f.close()
separate()