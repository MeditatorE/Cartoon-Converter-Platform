import os
path="./photo/"
n=0

fileList=os.listdir(path)

for i in fileList:
    

    oldname=str(i)
    print(i)    

    

    newname=str(n)+'.png'
    #使用rename时候要加上路径
    os.rename(path+oldname,path+newname)
    print(oldname,'======>',newname)
    
    n+=1
