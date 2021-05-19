from tkinter import *
from os import system, chdir
from tkinter import filedialog, messagebox

root=Tk()
root.title('Git File Uploader')
root.resizable(height=False,width=False)

def start():
	askgitdir=filedialog.askdirectory(title='Select Git Configured Directory')
	askfile=filedialog.askopenfilename(title='Select file to be uploaded',filetypes=[('All Files','*.*')])
	askfile=askfile.split('/')[-1]

	if askgitdir and ' ' not in askfile:
		chdir(askgitdir)
		try:
			system('git pull origin master')
			system('git status')
			system("git add {}".format(askfile))
			system("git commit -m 'test'")
			system('git push -u origin master')
			root.destroy()
		except:
			messagebox.showerror('Oops!,','Select folder not a Git Configured')
	else:
		messagebox.showerror('Oops!','Remember that filename must not contains blankspaces or tabs.')
		root.destroy()

start_button=Button(root,text='Start',font=('Agency FB',70,'bold'),fg='green',bg='#000000',command=start)
start_button.pack()

root.mainloop()