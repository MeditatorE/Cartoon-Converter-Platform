import numpy as np
import os
import cv2
import math

def cal_psnr(img1, img2):
   mse = np.mean((img1 - img2) ** 2 )
   if mse < 1.0e-10:
      return 100
   return 10 * math.log10(255.0**2/mse)


path="../photo/.DS_Store"
if os.path.exists(path):
    os.remove(path)

path="../cartoon/.DS_Store"
if os.path.exists(path):
    os.remove(path)


file_handle=open('psnr.txt',mode='w')
sum=0
j=0
for i in range(0,22):  # 遍历pathDir下的所有文件filename
        j+=1
        path1="../photo/"+str(i)+".png"
        path2="./cartoon/"+str(i)+"_Hosoda.png"
        im1=cv2.imread(path1)
        im2=cv2.imread(path2)
        psnr=cal_psnr(im1, im2)
        sum=sum+psnr
        file_handle.write(str(psnr)+"\n")

file_handle.write("\n"+"avg="+str(sum/j)+"\n")
file_handle.close()
print(sum/j)






















