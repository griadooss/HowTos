#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This program toggles the title of the
window with the Checkbutton widget

author: Jan Bodnar
last modified: December 2010
website: www.zetcode.com
"""


'''Tkinter widgets'''

#In this part of the Tkinter tutorial, we will cover some basic Tkinter widgets.
 
# Widgets are basic building blocks of a GUI application. 
# Over the years, several widgets became a standard in all toolkits on all OS platforms. 
# For example a button, a check box or a scroll bar. 
# Some of them might have a different name. 
# For instance, a check box is called a check button in Tkinter. 
# Tkinter has a small set of widgets which cover the basic programming needs. 
# More specialised components can be created as custom widgets.

'''Checkbutton'''

# The Checkbutton is a widget that has two states: on and off. 
# The on state is visualized by a check mark. 
# It is used to denote some boolean property. 
# The Checkbutton widget provides a check box with a text label.

#In our example, we place a check button on the window. 
#The check button shows or hides the title of the window.
from Tkinter import Tk, Frame, Checkbutton
from Tkinter import IntVar, BOTH


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Checkbutton")

        self.pack(fill=BOTH, expand=1)
        self.var = IntVar()
        #We create an IntVar object. 
        #It is a value holder for integer values for widgets in Tkinter.
        
        cb = Checkbutton(self, text="Show title",
            variable=self.var, command=self.onClick)
        #An instance of the Checkbutton is created. 
        #The value holder is connected to the widget via the variable parameter. 
        #When we click on the check button, the onClick() method is called. 
        #This is done with the command parameter.
        cb.select()
        #Initially, the title is shown in the titlebar. 
        #So at the start, we make it checked with the select() method.
        cb.place(x=50, y=50)


    def onClick(self):
       #Inside the onClick() method, we display or hide the title based on the value from the self.var variable.
        if self.var.get() == 1:
            self.master.title("Checkbutton")
        else:
            self.master.title("")
            


def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
 