f=open(r"F:\Machine Learning\Day4____18-June-2019\File.txt",'r')
e=''
d=f.read()
f.close()
for i in range(0,len(d)):
    if(d[i]=='e+d[i]'):
        e=d[i]
    else:
        e=e+chr(ord(d[i])+2)
print(e)

f1=open(r"F:\Machine Learning\Day4____18-June-2019\Encrypt.txt",'w')
f1.write(e)
f1.close()
