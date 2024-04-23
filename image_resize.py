from PIL import Image
import customtkinter
import os
import re
from tkinter import filedialog as fd
from tkinter import END
from CTkMessagebox import CTkMessagebox
file = ""

def checkmaxsize(maxsize):
    maxsize = maxsize.lower()
    
    if 'b' in maxsize:
        pattern = re.compile(r'([1-9][0-9]*)([kmg])b$')
        matches = pattern.finditer(maxsize)
        for i in matches:
            print(i.group(2))
            if i.group(2) == 'k':
                print(int(i.group(1))*1024)
                return int(i.group(1)) * 1024
            if i.group(2) == 'm':
                return int(i.group(1)) * 1024*1024
            if i.group(2) == 'g':
                return int(i.group(1)) * 1024*1024
    elif maxsize.isdigit():
        return maxsize
    else:
        msg = CTkMessagebox(title='error' , message="Enter valid file size" ,icon="warning", option_1="OK")
        maxsize.delete(first_index=0, last_index=END)
        return 0


    
    
def resize():
    global file
    print(file)
    if len(file) != 0 :
        image = Image.open(file)
        newfilename = newfileinput.get()
        maxfilesize = maxsize.get()
        maxfilesize =  checkmaxsize(maxfilesize)
        size = os.path.getsize(file)
        print(maxfilesize)
        print(size)
        

        w = image.width
        h = image.height
        
        extension = file[file.rfind('.'):]
        pathwithoutfilename = file[:file.rfind('/')]
        newfile = pathwithoutfilename+"/"+newfilename + extension
        if maxfilesize != 0 :
            if size < int(maxfilesize):
                msg = CTkMessagebox(title='info' , message="The image is already less than"+ maxfilesize ,icon="info", option_1="OK")
                label.configure(image = placeholderimg)
                newfileinput.delete(first_index=0, last_index=END)
                maxsize.delete(first_index=0, last_index=END)
                file = ""
            else:
            
                if os.path.exists(newfile):
                    msg = CTkMessagebox(title="Warning", 
                            message="File Already exists , Do you want to replace", 
                            icon="warning", 
                            option_1="Replace", 
                            option_2="Cancel")
                    if msg.get() == "Replace":
                        while size > int(maxfilesize) and h > 150:
                            h = h-100
                            image.thumbnail((h, h))
                            image.save(newfile)
                            image = Image.open(newfile)
                            size = os.path.getsize(newfile)
                        msg = CTkMessagebox(title='info' , message=newfilename+"Resized - check the folder in which the image was initially present  " ,icon="info", option_1="OK")
                        newfileinput.delete(first_index=0, last_index=END)
                        maxsize.delete(first_index=0, last_index=END)
                        label.configure(image = placeholderimg)
                        file = ""
                    else:
                        newfileinput.delete(first_index=0, last_index=END)
                        maxsize.delete(first_index=0, last_index=END)
                else:
                    while size > int(maxfilesize) and h > 150:
                        h = h-100
                        image.thumbnail((h, h))
                        print(image.height)
                        extension = file[file.rfind('.'):]
                        pathwithoutfilename = file[:file.rfind('/')]
                        
                        print(pathwithoutfilename+"/" + newfilename +
                            extension, size, maxfilesize)
                        image.save(newfile)
                        image = Image.open(newfile)
                        size = os.path.getsize(newfile)
                        
                    msg = CTkMessagebox(title='info' , message=newfilename+" Resized - check the folder in which the image was initially present  " ,icon="info", option_1="OK")

                    label.configure(image = placeholderimg)
                    newfileinput.delete(first_index=0, last_index=END)
                    maxsize.delete(first_index=0, last_index=END)
                    file = ""
    else:
        msg = CTkMessagebox(title='info' , message="Choose a image" ,icon="info", option_1="OK")

def onpressed():
    global file
    file = fd.askopenfilename(title='Choose an image to resize')
    image = Image.open(file)
    w = image.width
    h = image.height
    ratio = h/w
    height = 180
    img = customtkinter.CTkImage(image, size=(height/ratio, height))
    label.configure(image=img)
    print(file)
    filenamelabel = customtkinter.CTkLabel(
        root, text="New File Name", bg_color='#00041A')
    filenamelabel.place(x=250, y=90)
    maxsizelabel = customtkinter.CTkLabel(
        root, text="Max File Size", bg_color="#00041A")
    maxsizelabel.place(x=250, y=130)
    newfileinput.place(x=350, y=90)
    maxsize.place(x=350, y=130)
    submitbutton = customtkinter.CTkButton(
        root, text="Resize", command=resize, height=30)

    submitbutton.place(x=300, y=200)


root = customtkinter.CTk()
root.geometry("534x330")
root.config(background='#00041A')
title = customtkinter.CTkLabel(
    root, text="Resize an image", font=('Arial', 20), bg_color='#00041A')
button = customtkinter.CTkButton(
    root, text="Select an image", command=onpressed, height=40, width=150)
title.place(x=180, y=5)
button.place(x=40, y=257)
newfileinput = customtkinter.CTkEntry(root, placeholder_text="new_file_name")
maxsize = customtkinter.CTkEntry(root, placeholder_text="max file size")
placeholder = Image.open('placeholder.jpg')
placeholderimg = customtkinter.CTkImage(placeholder, size=(150, 180))
label = customtkinter.CTkLabel(root, text="", image=placeholderimg)
label.place(x=40, y=50)
root.mainloop()
