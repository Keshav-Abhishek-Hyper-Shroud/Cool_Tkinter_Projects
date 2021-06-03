# Importing Libraries
from tkinter import Tk, Label
from tkinter import messagebox, filedialog
from tkinter.ttk import Button as ttk_btn, Style
import threading

# Creating MainWindow
root=Tk()
root.title('Microsoft & Adobe - Utils')
root.resizable(height=False, width=False)

# Providing Title
main_title=Label(root,text='Microsoft & Adobe - Utils',font='times 25 bold')
main_title.pack(pady=10)

# Styling ttk Buttons
s=Style()
s.configure('W.TButton',font=('Times New Roman',15,'bold'),foreground='red')

# Asks when exiting
def surexit():
	response=messagebox.askyesno('Sure!!','You want to Exit ?')
	if response==1:
		root.destroy()

# Docx to PDF
def docxtopdf():
	filename=filedialog.askopenfilename(title='Select a Docx File',filetypes=[('Docx File','*.docx')])
	if filename!='':
		docx_pdf['text']='Converting...'
		import win32com.client
		word_pdf_mech=win32com.client.Dispatch('Word.Application')
		pdf_file=word_pdf_mech.Documents.Open(filename.replace('/','\\'))
		outputfilename=filename.replace('.docx','_converted.pdf')
		outputfilename=outputfilename.replace('/','\\')
		pdf_file.SaveAs(outputfilename,17) # Refer to "https://docs.microsoft.com/en-us/office/vba/api/word.wdsaveformat" to know about use of 17 in this line.
		messagebox.showinfo('Done!','Docx to PDF converted successfully.')
		docx_pdf['text']='Docx to PDF'

# PDF to Docx
def pdftodocx():
	filename=filedialog.askopenfilename(title='Select a PDF File',filetypes=[('PDF File','*.pdf')])
	if filename!='':
		pdf_docx['text']='Converting...'
		from pdf2docx import parse
		parse(filename,filename.replace('.pdf','_converted.docx'))
		messagebox.showinfo('Done!','PDF to Docx converted successfully.')
		pdf_docx['text']='PDF to Docx'

# Working Buttons
docx_pdf=ttk_btn(root,text='Docx to PDF',style='W.TButton',command=lambda:threading.Thread(target=docxtopdf()).start,takefocus=False)
docx_pdf.pack(pady=5)

pdf_docx=ttk_btn(root,text='PDF to Docx',style='W.TButton',command=lambda:threading.Thread(target=pdftodocx()).start,takefocus=False)
pdf_docx.pack(pady=5)

root.protocol('WM_DELETE_WINDOW',surexit)
root.mainloop()
# Thanks For Using