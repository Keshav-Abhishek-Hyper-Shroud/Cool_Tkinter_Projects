from tkinter import Tk, Button, Label
from pygame import screenshot

root=Tk()

def takeScreenShot():
    data = screenshot()
    data.save('OutPut.png')

my_b = Button(root,text='Take ScreenShot',font='times 20 bold',command=takeScreenShot)
my_b.pack(padx=20, pady=20)

root.mainloop()