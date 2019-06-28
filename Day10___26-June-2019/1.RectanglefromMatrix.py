import numpy as np
def isRectangle(m):
    # finding rows and column size

    rows=len(m)
    if(rows==0):
        return False
    columns=len(m[0])

    # scanning the matrux
    for y1 in range (rows):
        for x1 in range(columns):
            #if any index found 1 the
            # try for all rectangles

            if(m[y1][x1]==1):
                for y2 in range(y1+1,rows):
                    for x2 in range(x1+1,columns):
                        if(m[y1][x2]==1 and
                           m[y2][x1]==1 and
                           m[y2][x2]==1):
                            return True
        return False
arr=np.zeros([5,6])
arr[0,0]=1
arr[0,3]=1
arr[1,0]=1
arr[1,2]=1
arr[1,5]=1
arr[3,2]=1
arr[3,5]=1
arr[4,5]=1
print(arr)
print("............")
if(isRectangle(arr)):
    print("Yes")
else:
    print("No")
                    
        
