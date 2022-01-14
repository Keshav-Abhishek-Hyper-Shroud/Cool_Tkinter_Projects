# Libraries to be imported

import os
from tkinter import *
from tkinter import filedialog
from PIL import Image

root=Tk()

root.geometry('500x500')
root.title('Image Resizer')

# Helps to choose picture/image to be resized
def browsePhoto():
    global imgLocation
    imgLocation = filedialog.askopenfilename(title='Open Image File', filetypes=[('PNG Files', '*.png'), ('JPG Files', '*.jpg'), ('JPEG Files', '*.jpeg')])

    if imgLocation:
        imgName = imgLocation.split('/')[-1]
        imageNameLabel.config(text=f'Image Name: {imgName}')

        imgWidth,imgHeight = Image.open(imgLocation).size

        imageAspectLabel.config(text=f'Width: {imgWidth}px\nHeight: {imgHeight}px\nAspect-Ratio (Width:Height) = {round(imgWidth/imgHeight,3)}')

        global ratio
        ratio = round(imgWidth/imgHeight,3)

        widthEntry.config(state=NORMAL)
        heightEntry.config(state=NORMAL)
        resizeSave.config(state=NORMAL)
        browse_photo.config(state=DISABLED)
    else:
        imageNameLabel.config(text=f'Image Name: no-file-choosen')
        imageAspectLabel.config(text=f'')
        widthEntry.config(state=DISABLED)
        heightEntry.config(state=DISABLED)
        resizeSave.config(state=DISABLED)
        browse_photo.config(state=NORMAL)

browse_photo = Button(root,text='Browse Image',font='times 20 bold',command=browsePhoto)
browse_photo.pack(pady=20)

main_frame = Frame(root)
main_frame.pack(pady=20)

imageNameLabel = Label(main_frame,text='Image Name: no-file-choosen')
imageNameLabel.pack(pady=10)

imageAspectLabel = Label(main_frame,text='')
imageAspectLabel.pack(pady=10)

userEntryLabel = Label(main_frame,text='User Entry',font='times 20 bold')
userEntryLabel.pack(pady=5)

frame_2 = Frame(main_frame)
frame_2.pack(pady=10)


widthEntryLabel = Label(frame_2,text='Width: ',font='times 15 bold')
widthEntryLabel.grid(row=0,column=0)

heightEntryLabel = Label(frame_2,text='Height: ',font='times 15 bold')
heightEntryLabel.grid(row=1,column=0)



widthEntry = Entry(frame_2,font='times 15 normal', state=DISABLED)
widthEntry.grid(row=0,column=1)

heightEntry = Entry(frame_2,font='times 15 normal', state=DISABLED)
heightEntry.grid(row=1,column=1)



onlyIntergersAllowedLabelWidth = Label(frame_2,text='(Only Intergers)',font='times 12 normal',foreground='red')
onlyIntergersAllowedLabelWidth.grid(row=0,column=2)

onlyIntergersAllowedLabelHeight = Label(frame_2,text='(Only Intergers)',font='times 12 normal',foreground='red')
onlyIntergersAllowedLabelHeight.grid(row=1,column=2)


# Controls Width
def widthControl(e):
    try:
        global ratio
        widthEntry.delete(0,END)
        width = int(ratio*int(heightEntry.get()+e.char))

        widthEntry.insert(0,str(width))
    except ValueError:
        pass

# Controls Height
def heightControl(e):
    try:
        global ratio
        heightEntry.delete(0,END)
        height =int(int(widthEntry.get()+e.char)/ratio)

        heightEntry.insert(0,str(height))
    except ValueError:
        pass

widthEntry.bind('<Key>',heightControl)
heightEntry.bind('<Key>',widthControl)

# Saves Resized Image
def saveImage():
    global imgLocation
    try:
        if int(widthEntry.get()) and int(heightEntry.get()):
            img = Image.open(imgLocation)
            imgSave = img.resize((int(widthEntry.get()),int(heightEntry.get())))
            imgSaveLoaction = filedialog.asksaveasfilename(title='Save As', filetypes=[('PNG Files', '*.png'), ('JPG Files', '*.jpg'), ('JPEG Files', '*.jpeg')],defaultextension="")
            imgSave.save(imgSaveLoaction)
            os.startfile(imgSaveLoaction)
            resetApp()
    except:
        resetApp()

resizeSave = Button(main_frame,text='Resize & Save',font='times 18 bold',command=saveImage,state=DISABLED)
resizeSave.pack(pady=10,fill=X)

# Reset App
global resetApp
def resetApp():
    imageNameLabel.config(text=f'Image Name: no-file-choosen')
    imageAspectLabel.config(text=f'')
    widthEntry.delete(0,END)
    heightEntry.delete(0,END)
    widthEntry.config(state=DISABLED)
    heightEntry.config(state=DISABLED)
    resizeSave.config(state=DISABLED)
    browse_photo.config(state=NORMAL)


resetAppButton = Button(main_frame,text='Reset',font='times 15 normal',command=resetApp,foreground='red',borderwidth=0)
resetAppButton.pack(pady=10)

root.mainloop()