import os
import tensorflow as tf




path="../photo/.DS_Store"
if os.path.exists(path):
    os.remove(path)

path="../cartoon/.DS_Store"
if os.path.exists(path):
    os.remove(path)

file_handle=open('ssim.txt',mode='w')
sum=0
j=0
for i in range(0,22):  # 遍历pathDir下的所有文件filename
    j+=1
    path1="../photo/"+str(i)+".png"
    path2="./cartoon/"+str(i)+"_Paprika.png"
    # Read images from file.
    im1 = tf.image.decode_png(tf.io.read_file(path1))
    im2 = tf.image.decode_png(tf.io.read_file(path2))
    # Compute SSIM over tf.uint8 Tensors.
    ssim = tf.image.ssim(im1, im2, max_val=255)
    sum=sum+ssim
    file_handle.write(str(ssim)+"\n")

file_handle.write("\n"+"avg="+str(sum/j)+"\n")
file_handle.close()
print(sum/j)