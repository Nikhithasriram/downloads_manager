import os
# from os.path import isfile 
import re

path = r"C:\Users\nikhi\Downloads"
os.chdir(path)

for root,dir,files in os.walk(path):
    # print(files)
    # print("-----------------------------------------------")
    dup  = []
    dup_files = []
    # print(files)
    for i in files:
        index = i.rfind(".")
        text = i[:index]
        if text[-1] == ')' and text[-3] == '(':
            old_text = text
            text = text[:-4]
            containsbrackets = True
        # print(text[-4:])
        elif text[-7:].lower() == ' - copy':
            text = text[:-7]
            containscopy = True
        # print(text)
        if text in dup:
            otherfile = dup_files[dup.index(text)]
            otherfilesize = os.path.getsize(os.path.join(root , otherfile))
            thisfilesize = os.path.getsize(os.path.join(root , i))
            if otherfilesize == thisfilesize:
                os.chdir(root)
                print("removing this file---------------------------------------" , i)
                os.remove(i)
        else:
            dup.append(text)
            dup_files.append(i)

# print(dup)
# for removing the extra (1) thing in the files
for root,dir,files in os.walk(path):
    for i in files:
        index = i.rfind(".")
        text = i[:index]
        extension = i[index:]
        if len(text) > 3:
            x = re.finditer(r'\(\d+\)$' , text)
            for i in x:
                # print(i.start())
            # if text[-3] == '(' and text[-1] == ')':
                
                orginalpath = os.path.join(root, text+extension)
                text = text[:i.start()]
                finalpath = os.path.join(root,text+extension)
                os.chdir(root)
                # print(os.getcwd())
                os.replace(orginalpath , finalpath)