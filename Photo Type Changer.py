import os
from PIL import Image as Img # pip install pillow
from tkinter import *
from tkinter import filedialog, messagebox, ttk
import threading

root=Tk()
root.title("Photo_Type_Changer")
root.geometry('300x220')
root.minsize(300, 220)
root.maxsize(300, 220)

options=['PNG', 'JPEG', 'JPG', 'ICO'] # Image Types Supported by the Software

def Convert(e):
	if my_combo.get()=='PNG':

		my_combo.set('PNG')

		part_1=os.path.splitext(a)[0]+'_converted'

		file=Img.open(a)
		file_1=file.convert('RGB')
		file_1.save(part_1+'.png')
		messagebox.showinfo('Convert Done', 'File converted to PNG')
		my_combo.destroy()

	elif my_combo.get()=='JPG':

		my_combo.set('JPG')

		part_1=os.path.splitext(a)[0]+'_converted'

		file=Img.open(a)
		file_1=file.convert('RGB')
		file_1.save(part_1+'.jpg')
		messagebox.showinfo('Convert Done', 'File converted to JPG')
		my_combo.destroy()

	elif my_combo.get()=='JPEG':

		my_combo.set('JPEG')

		part_1=os.path.splitext(a)[0]+'_converted'

		file=Img.open(a)
		file_1=file.convert('RGB')
		file_1.save(part_1+'.jpeg')
		messagebox.showinfo('Convert Done', 'File converted to JPEG')
		my_combo.destroy()

	elif my_combo.get()=='ICO':

		my_combo.set('ICO')

		part_1=os.path.splitext(a)[0]+'_converted'

		file=Img.open(a)
		file_1=file.convert('RGB')
		file_1.save(part_1+'.ico')
		messagebox.showinfo('Convert Done', 'File converted to ICO')
		my_combo.destroy()


def main_menu():

	global a, my_combo

	a=filedialog.askopenfilename(title='Open Image File', filetypes=[('PNG Files', '*.png'), ('JPG Files', '*.jpg'), ('ICON Files', '*.ico'), ('JPEG Files', '*.jpeg')])

	my_combo=ttk.Combobox(root, value=options, font=('Agency FB', 15, 'bold'))
	my_combo.pack(pady=20)
	my_combo.set('OPTIONS')
	my_combo.bind('<<ComboboxSelected>>', Convert)

browse_image=Button(root, text='Browse Image', font=('Agency FB', 20, 'bold', 'italic'), borderwidth=0, bg='grey', command=main_menu)
browse_image.pack(pady=20)

root.mainloop()
