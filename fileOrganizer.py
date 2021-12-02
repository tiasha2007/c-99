import os
import shutil
from typing import Text

path=input("enter the path of the files to be sorted: ")
list_of_files=os.listdir(path)

for file in list_of_files:
    name,ext = os.path.splitext(file)
    
    # this is going to store the extension type
    ext=ext[1:]

    # if it is a directory
    if ext == '':
        continue

    #this will move the file to the directory
    #where the ext already exist
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
