import os
import shutil

fromdir="C:/Users/ayush/Downloads"
todir="C:/Users/ayush/OneDrive/Desktop/p102"

listoffiles=os.listdir(fromdir)
#print(listoffiles)

for filename in listoffiles:
    name,ext=os.path.splitext(filename)
    #print(name)
    #print(ext)
    if(ext==''):
        continue
    if(ext in ['.txt','.doc','.docx','.pdf']):
        path1=fromdir+'/'+filename
        path2=todir+'/'+"docfiles"
        path3=todir+'/'+"docfiles"+'/'+filename
        if(os.path.exists(path2)):
            print("The file is being moved.")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("The file is being moved.")
            shutil.move(path1,path3)