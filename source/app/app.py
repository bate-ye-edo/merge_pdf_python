#Created by Bate Ye
#GNU GENERAL PUBLIC LICENSE
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mbox
from merge import mergePDF

class AppendGUI:
    def __init__(self):
        self.filenames=[]
        self.root = Tk()
        self.root.title("Append PDF")
        self.root.geometry('600x200')
        self.root.resizable(True,True)
        self.f = Frame()
        self.f.pack()

        self.labeltext = ""
        self.names = Label(self.f,text=self.labeltext)
        self.names.grid(row=1,column=2)


        self.outputFileEntry = Button(self.f,cursor='hand1',text="Merge PDFs",command=lambda:self.saveButtonClicked(),width=20)
        self.outputFileEntry.grid(row=2,column=2,columnspan=2)

        self.outputRow = 1

        self.openButton = Button(self.f,cursor='hand1',text="openFile",command=lambda:self.openButtonClicked(),width=20)
        self.openButton.grid(row=0,column=2,columnspan=2)

        self.root.mainloop()
    def openButtonClicked(self):
        self.root.filename = filedialog.askopenfilename(initialdir="/",title="Select PDFs",filetypes=[("PDF files","*.pdf")])
        if self.root.filename != "":
            self.filenames.append(self.root.filename)
        self.labeltext = self.labeltext+self.root.filename+"\n"
        self.names.config(text=self.labeltext)

    def saveButtonClicked(self):
        if self.labeltext != "":
            self.root.filename = filedialog.asksaveasfilename(initialdir='/',title='Save Merged PDF',filetypes=[('PDF files','*.pdf')])
            outputFileName = self.root.filename
            if outputFileName.find('.pdf') == False:
                outputFileName = outputFileName+'.pdf'
            boleano = mergePDF(self.filenames,outputFileName)
            if boleano== True:
                mbox.showinfo("Success!","PDFs Merged!")
                self.labeltext = ""
                self.names.config(text=self.labeltext)
        else:
            mbox.showwarning("Warning!","No PDFs to merge")



if __name__=='__main__':
    app = AppendGUI()
