from tkinter import *
from tkinter import messagebox,ttk
from PIL import ImageGrab
import os
import random
import time

curr_dir=os.getcwd()
root_dir=''
colon_index=curr_dir.index(':')

for i in range(0,colon_index+1):
    root_dir+=curr_dir[i]

if 'Screenshot Using Python' not in os.listdir(root_dir+'/'):
    os.makedirs(f'{root_dir}/Screenshot Using Python')

def main():
    root=Tk()
    root.title('Take Screenshot')
    root.resizable(width=False,height=False)

    def takeit():
        if var.get():
            messagebox.showinfo('Screenshot','Screenshot will be taken as you press OK.')
            ext=extentions[var.get()-1]
            root.destroy()
            time.sleep(1)
            image = ImageGrab.grab()
            filename=''
            for i in range(16):
                num=random.randint(65,90)
                filename+=chr(num)
            filename=f'{root_dir}/Screenshot Using Python/'+filename+ext
            image.save(filename)
            os.startfile(filename)
            main()
        else:
            messagebox.showwarning('Alert!','Photo type not choosen,\nchoose atleast one.')
    
    my_button=Button(root,text='Take ScreenShot',font='times 20 bold',bd=1,bg='lightpink',command=takeit)
    my_button.pack()

    var=IntVar()
    extentions=['.png','.jpg','.jpeg','.ico','.pdf']
    imagename_type=[('PNG',1),('JPG',2),('JPEG',3),('ICON',4)]

    radio_label=Label(root)
    radio_label.pack()

    for i in imagename_type:
        my_radio=ttk.Radiobutton(radio_label,text=i[0],variable=var,value=i[1],takefocus=False)
        my_radio.grid(row=0,column=imagename_type.index(i))
    
    def runagain():
        root.destroy()
        main()

    Button(root,text='Restart',font='times 15 bold',fg='green',bd=0,command=runagain).pack()
    Button(root,text='X',font='times 12 bold',fg='red',bd=0,command=root.destroy).pack()

    root.mainloop()
    
main()