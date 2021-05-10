from time import time,strftime,gmtime

from tkinter import *

k=int(time())+19800 # 19800 time gap in seconds acc. to "UTC"
k=strftime('%A, %d:%B:%Y;%H:%M:%S %p',gmtime(k))

root=Tk()
root.title('Clock')
root.resizable(height=False,width=False)

def updateclock():
	k=int(time())+19800
	k=strftime('%A, %d:%B:%Y;%H:%M:%S %p',gmtime(k))
	label['text']=k.split(';')[1]
	data='\n'.join(k.split(';')[0].split(':'))
	daymonthyear_label['text']=data
	root.after(1000,updateclock)

label=Label(root,text=k.split(';')[1],font='times 20 bold')
label.pack()

data='\n'.join(k.split(';')[0].split(':'))
daymonthyear_label=Label(root,text=data,font='times 20 bold')
daymonthyear_label.pack(pady=10)

updateclock()
root.mainloop()

#Thanks For Using.