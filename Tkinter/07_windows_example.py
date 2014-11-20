#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
ZetCode Tkinter tutorial

In this script, we use the grid
manager to create a more complicated
layout.

author: Jan Bodnar
last modified: December 2010
website: www.zetcode.com
"""

#In this example, we will use a Label widget, a Text widget and four buttons.
from Tkinter import Tk, Text, BOTH, W, N, E, S
from ttk import Frame, Button, Label, Style


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Windows")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)
        #We define some spaces among widgets in the grid. 
        #The largest space is put between the Text widget and the buttons.
        
        lbl = Label(self, text="Windows")
        lbl.grid(sticky=W, pady=4, padx=5)
        #The label widget is created and put into the grid. 
        #If no column and row is specified, then the first column or row is assumed. 
        #The label sticks to west and it has some padding around its text.
        
        area = Text(self)
        area.grid(row=1, column=0, columnspan=2, rowspan=4, 
            padx=5, sticky=E+W+S+N)
        #The Text widget is created and starts from the second row, first column. 
        #It spans 2 columns and 4 rows. 
        #There is 4px space between the widget and the left border of the root window. 
        #Finally, it sticks to all the four sides. 
        #So when the window is resized, the Text widget grows in all directions.
        
        abtn = Button(self, text="Activate")
        abtn.grid(row=1, column=3)

        cbtn = Button(self, text="Close")
        cbtn.grid(row=2, column=3, pady=4)
        
        hbtn = Button(self, text="Help")
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text="OK")
        obtn.grid(row=5, column=3)        
              

def main():
  
    root = Tk()
    root.geometry("350x300+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  