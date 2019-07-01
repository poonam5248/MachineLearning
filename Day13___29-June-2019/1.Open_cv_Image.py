# 1.

import cv2 as cv
i=cv.imread(r"F:\Machine Learning\Day13___29-June-2019\Poonam.jpg")
print(i)

cv.imshow('img',i)

k=cv.waitKey(0)

cv.destroyAllWindows()

# 2.

import cv2 as cv
i=cv.imread(r"F:\Machine Learning\Day13___29-June-2019\Poonam.jpg")
print(i[0,0,0]) # 0 row 0 column 0 layer

cv.imshow('img',i)

k=cv.waitKey(0) # 0=unconditional wait till you press any key

cv.destroyAllWindows()

# 3.

import cv2 as cv
i=cv.imread(r"F:\Machine Learning\Day13___29-June-2019\Smiley.jpg")
print(i[0,0,:],'\n')
print(i[0:3,0:3,:],"\n")
print(i[:,:,:],"\n")
print(i[0,0,0],"\n")
print(i[0,:,:],"\n")
print(i[0:5,:,:],"\n")
print(i[0,:],"\n")
print(i[0],"\n")
i[0:5,:,0]=255
i[0:5,:1]=0
i[0:5,:,2]=0

cv.imshow('img',i)

k=cv.waitKey(0)

cv.destroyAllWindows()

# 4.


import cv2 as cv
i=cv.imread(r"F:\Machine Learning\Day13___29-June-2019\Smiley.jpg")
##i=cv.resize(i,(500,500))# to resize the image
##print(i[0,0,:],'\n')
##print(i[0:3,0:3,:],"\n")
##print(i[:,:,:],"\n")
##print(i[0,0,0],"\n")
##print(i[0,:,:],"\n")
##print(i[0:5,:,:],"\n")
##print(i[0,:],"\n")
##print(i[0],"\n")
##r,c,t=i.shape
i[0:5,:,0]=255
i[0:5,:,1]=0
i[0:5,:,2]=0

i[:,0:5,0]=255
i[:,0:5,1]=0
i[:,0:5,2]=0

i[-5:,:,0]=255
i[-5:,:,1]=0
i[-5:,:,2]=0

i[:,-5:,0]=255
i[:,-5:,1]=0
i[:,-5:,2]=0

cv.imshow('img',i)

k=cv.waitKey(0)

cv.destroyAllWindows()

# 5.

import cv2 as cv
i=cv.imread(r"F:\Machine Learning\Day13___29-June-2019\Smiley.jpg")
##i=cv.resize(i,(500,500))# to resize the image
##print(i[0,0,:],'\n')
##print(i[0:3,0:3,:],"\n")
##print(i[:,:,:],"\n")
##print(i[0,0,0],"\n")
##print(i[0,:,:],"\n")
##print(i[0:5,:,:],"\n")
##print(i[0,:],"\n")
##print(i[0],"\n")
##r,c,t=i.shape
i[x:x+10,50:60,0]=255
i[0:5,:,1]=0
i[0:5,:,2]=0

i[:,0:5,0]=255
i[:,0:5,1]=0
i[:,0:5,2]=0

i[-5:,:,0]=255
i[-5:,:,1]=0
i[-5:,:,2]=0

i[:,-5:,0]=255
i[:,-5:,1]=0
i[:,-5:,2]=0

cv.imshow('img',i)

k=cv.waitKey(5)
if(k==ord('q')):
    cv.destroyAllWindows()
    break
elif(k==ord('a')):
    y=y-10
elif(k==ord('d')):
    y=y+10
elif(k==ord('w')):
    x=x-10
elif(k==ord('s')):
    x=x+10
    





