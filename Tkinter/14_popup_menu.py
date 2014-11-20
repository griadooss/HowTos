#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this program, we create
a popup menu. 

author: Jan Bodnar
last modified: December 2010
website: www.zetcode.com
"""

'''Popup menu'''

# In the next example, we create a popup menu. 
# Popup menu is also called a context menu. 
# It can be shown anywhere on the client area of a window.

# In our example, we create a popup menu with two commands.
from Tkinter import Tk, Frame, Menu


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Popup menu")
        self.menu = Menu(self.parent, tearoff=0)
        #A context menu is a regular Menu widget. 
        #The tearoff feature is turned off. 
        #Now it is not possible to separate the menu into a new toplevel window.
        self.menu.add_command(label="Beep", command=self.bell())
        self.menu.add_command(label="Exit", command=self.onExit)

        self.parent.bind("<Button-3>", self.showMenu)
        #We bind the <Button-3> event to the showMenu() method. 
        #The event is generated when we right click on the client area of the window.
        self.pack()
        
    #The showMenu() method shows the context menu. 
    #The popup menu is shown at the x and y coordinates of the mouse click.    
    def showMenu(self, e):
        self.menu.post(e.x_root, e.y_root)
       

    def onExit(self):
        self.quit()


def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
