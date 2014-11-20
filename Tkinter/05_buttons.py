#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
ZetCode Tkinter tutorial

In this script, we use pack manager
to position two buttons in the
bottom right corner of the window. 

author: Jan Bodnar
last modified: December 2010
website: www.zetcode.com
"""

#We will have two frames. 
#There is the base frame and an additional frame, which will expand in both directions and 
#push the two buttons to the bottom of the base frame. 
#The buttons are placed in a horizontal box and placed to the right of this box.
from Tkinter import Tk, RIGHT, BOTH, RAISED
from ttk import Frame, Button, Style


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Buttons")
        self.style = Style()
        self.style.theme_use("default")
        
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=1)
        #We create another Frame widget. 
        #This widget takes the bulk of the area. 
        #We change the border of the frame so that the frame is visible. 
        #By default it is flat.
        
        self.pack(fill=BOTH, expand=1)
        
        closeButton = Button(self, text="Close")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        #A closeButton is created. 
        #It is put into a horizontal box. 
        #The side parameter will create a horizontal box layout, in which the button is placed to the right of the box. 
        #The padx and the pady parameters will put some space between the widgets. 
        #The padx puts some space between the button widgets and between the closeButton and the right border of the root window. 
        #The pady puts some space between the button widgets and the borders of the frame and the root window.
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)
        #The okButton is placed next to the closeButton with 5px space between them.
              

def main():
  
    root = Tk()
    root.geometry("300x200+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  