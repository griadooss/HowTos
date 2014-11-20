#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this program, we use the
tkFileDialog to select a file from
a filesystem.

author: Jan Bodar
last modified: January 2011
website: www.zetcode.com
"""

'''File dialog'''

# In our code example, we use the tkFileDialog dialog to select a file and display its contents in a Text widget.
from Tkinter import Frame, Tk, BOTH, Text, Menu, END
import tkFileDialog 
# tkFileDialog dialog allows a user to select a file from the filesystem.
class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("File dialog")
        self.pack(fill=BOTH, expand=1)
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)        
        
        self.txt = Text(self)
        #This is the Text widget in which we will show the contents of a selected file.
        self.txt.pack(fill=BOTH, expand=1)


    def onOpen(self):
      
        ftypes = [('Python files', '*.py'), ('All files', '*')]
        #These are file filters. 
        #The first shows only Python files, the other shows all files.
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
        #The dialog is created and shown on the screen. We get the return value, which is the name of the selected file.
        
        if fl != '':
            text = self.readFile(fl)
            #We read the contents of the file.
            self.txt.insert(END, text)
            #The text is inserted into the Text widget.

    def readFile(self, filename):

        f = open(filename, "r")
        text = f.read()
        return text
         

def main():
  
    root = Tk()
    ex = Example(root)
    root.geometry("300x250+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()  