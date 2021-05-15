# Importing libraries
from tkinter import Tk,END,DISABLED,NORMAL,RIGHT,BOTH,Entry,Menu,Frame,messagebox,HORIZONTAL,X
from tkinter.ttk import Scrollbar as ttk_scroll,Button as ttk_btn

root=Tk()
root.resizable(height=False,width=False) # Disable resizing of window abrubtly
root.iconbitmap('Calc_Icon.ico') # Sets Icon
root.title('Calculator') #Sets Title

# Don't touch keyboard
def keyboardused(e):
	entry_box.delete(0,END)
	entry_box['state']=DISABLED

# Create a screen
entry_box=Entry(root,font=('Agency FB',15,'bold'),justify=RIGHT)
entry_box.pack(pady=5,fill=BOTH)
entry_box['state']=DISABLED
entry_box.bind('<KeyPress>',keyboardused)

# Frame to keep buttons
button_frame=Frame(root,bd=0)
button_frame.pack(pady=5)

keys=[('ON/OFF',0,0),('C',0,1),('%',0,2),('DEL',0,3),('7',1,0),('8',1,1),('9',1,2),('÷',1,3),('4',2,0),('5',2,1),('6',2,2),('x',2,3),('1',3,0),('2',3,1),('3',3,2),('-',3,3),('0',4,0),('.',4,1),('=',4,2),('+',4,3)]

# Calculation function
def clicked(e):
	if e.widget.cget('text')=='=':
		try:
			raw_data=entry_box.get().replace('%','/100x')
			raw_data=raw_data.replace('x','*')
			raw_data=raw_data.replace('÷','/')
			data=eval(raw_data)
			entry_box.delete(0,END)
			entry_box.insert(0,f'{data}')
		except:
			entry_box.delete(0,END)
			entry_box.insert(0,'Error')

	elif e.widget.cget('text')=='C':
		entry_box.delete(0,END)

	elif e.widget.cget('text')=='ON/OFF':
		if entry_box.cget('state')=='normal':
			entry_box.delete(0,END)
			entry_box['state']=DISABLED
		else:
			entry_box['state']=NORMAL

	elif e.widget.cget('text')=='DEL':
		entry_box.delete(len(entry_box.get())-1,END)

	else:
		if entry_box.get()=='Error':
			entry_box.delete(0,END)
		curr_pressed_button=e.widget.cget('text')
		data=entry_box.get()+curr_pressed_button
		entry_box.delete(0,END)
		entry_box.insert(0,data)

# Key building area
for i in keys:
	k=ttk_btn(button_frame,text=i[0],takefocus=False)
	k.grid(row=i[1],column=i[2])
	k.bind('<ButtonRelease-1>',clicked)

# Create a scrollbar
entry_scroll=ttk_scroll(root,command=entry_box.xview,orient=HORIZONTAL)
entry_scroll.pack(fill=X)
entry_box.config(xscrollcommand=entry_scroll.set)

# Menu area
my_menu=Menu(root)
root.config(menu=my_menu)

option_menu=Menu(my_menu)

# Information popup
def showinfos():
	messagebox.showinfo('Information!','''Hello!\n\n1. Use "//" to get only the integer value while dividing.\n\tFor example: 5//2 = 2\n\n2. Use "**" to find the square,cube,... on a number.\n\tFor example:\n\t1**2 = 1\n\t2**2 = 4\n\t2**3 = 8\n\tand many more.''')

my_menu.add_command(label='Info',command=showinfos)
my_menu.add_command(label='Close',command=root.destroy)

root.mainloop()

# Thanks For Using
