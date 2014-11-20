#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script we create a submenu
a separator and keyboard shortcuts to menus.

author: Jan Bodnar
last modified: December 2010
website: www.zetcode.com
"""

'''Submenu'''
#A submenu is a menu plugged into another menu object. 
#In the example, we have three options in a submenu of a file menu. 
#We create a separator and keyboard shortcuts.

from Tkinter import Tk, Frame, Menu

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Submenu")
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        
        fileMenu = Menu(menubar)       
        
        submenu = Menu(fileMenu)
        submenu.add_command(label="New feed")
        submenu.add_command(label="Bookmarks")
        submenu.add_command(label="Mail")
        #We have a submenu with three commands. The submenu is a regular menu.
        fileMenu.add_cascade(label='Import', menu=submenu, underline=0)
        #By adding the menu to the fileMenu and not to the menubar, we create a submenu. 
        #The underline parameter creates a keyboard shortcut. 
        #We provide a character position, which should be underlined. 
        #In our case it is the first. Positions start from zero. 
        #When we click on the File menu, a popup window is shown. 
        #The Import menu has one character underlined. 
        #We can select it either with the mouse pointer, or with the Alt+I shortcut.


        
        fileMenu.add_separator()
        #A separator is a horizontal line that visually separates the menu commands. 
        #This way we can group items into some logical places.
        
        fileMenu.add_command(label="Exit", underline=0, command=self.onExit)
        menubar.add_cascade(label="File", underline=0, menu=fileMenu)        
                

    def onExit(self):
        self.quit()


def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  