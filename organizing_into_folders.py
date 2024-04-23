import os
from os.path import isfile 
# path = "C:\Users\nikhi\Downloads"

path = r"C:\Users\nikhi\Downloads"
os.chdir(path)
folders = ['pdf' , 'ppt' , 'images' , 'photoshop' , 'ZIP' , 'word_excel' , 'random']
pdf_path = os.path.join(path , folders[0])
ppt_path = os.path.join(path , folders[1])
images_path = os.path.join(path , folders[2])
photoshop_path = os.path.join(path , folders[3])
ZIP_path = os.path.join(path , folders[4])
word_excel_path = os.path.join(path , folders[5])
random_path = os.path.join(path , folders[6])



files = os.listdir()
files = [f for f in files if isfile(os.path.join(path , f))]

#? make a directory of ur choice if already present this is not needed 
if not(os.path.exists(pdf_path)):
    os.mkdir(pdf_path)
if not(os.path.exists(images_path)):
    os.mkdir(images_path)
if not(os.path.exists(photoshop_path)):
    os.mkdir(photoshop_path)
if not(os.path.exists(ZIP_path)):
    os.mkdir(ZIP_path)
if not(os.path.exists(word_excel_path)):
    os.mkdir(word_excel_path)
if not(os.path.exists(random_path)):
    os.mkdir(random_path)




for i in files:
    index_of_extension = i.rfind('.')
    file_extension = i[index_of_extension:]
    if file_extension.lower() == ".pdf":
        orginal_path = os.path.join(path , i)
        new_path = os.path.join(pdf_path , i)
        os.rename(orginal_path , new_path)
    elif file_extension.lower() == ".pptx" or file_extension.lower() == 'ppt':
        orginal_path = os.path.join(path , i)
        new_path = os.path.join(ppt_path , i)
        os.rename(orginal_path , new_path)
    elif file_extension.lower() == ".jpg" or file_extension.lower() == ".png" or file_extension.lower() == ".jpeg" or file_extension.lower() == ".jfif"  or file_extension.lower() == ".gif":
        orginal_path = os.path.join(path , i)
        new_path = os.path.join(images_path , i)
        os.rename(orginal_path , new_path)
    elif file_extension.lower() == ".psd":
        orginal_path = os.path.join(path , i)
        new_path = os.path.join(photoshop_path , i)
        os.rename(orginal_path , new_path)
    elif file_extension.lower() == ".zip":
        orginal_path = os.path.join(path , i)
        new_path = os.path.join(ZIP_path , i)
        os.rename(orginal_path , new_path)
    elif file_extension.lower() == ".xlsx" or file_extension.lower() == '.docx' or file_extension.lower() == '.csv':
        orginal_path = os.path.join(path , i)
        new_path = os.path.join(word_excel_path , i)
        os.rename(orginal_path , new_path)
    else:
        orginal_path = os.path.join(path , i)
        new_path = os.path.join(random_path , i)
        os.rename(orginal_path , new_path)

#  removing duplicates 

print("Done")