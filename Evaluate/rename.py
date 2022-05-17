import os
path="./photo/"
n=0

fileList=os.listdir(path)

path1 = "./photo/.DS_Store"
if os.path.exists(path1):
    os.remove(path1)


for i in fileList:
    

    oldname=str(i)
    print(i)    

    

    newname=str(n)+'.png'
    #使用rename时候要加上路径
    os.rename(path+oldname,path+newname)
    print(oldname,'======>',newname)
    
    n+=1
