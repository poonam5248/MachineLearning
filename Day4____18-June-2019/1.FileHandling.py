f=open(r"F:\Machine Learning\Day4____18-June-2019\File.txt",'r')
e=''
d=f.read()
for i in range(0,len(d)):
    if(d[i]==''):
        e=e+d[i]
    else:
        e=e+chr(ord(d[i])+2)
print(e)


    
