#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This program shows a simple
menu. It has one command, which
will terminate the program, when
selected. 

author: Jan Bodnar
last modified: December 2010
website: www.zetcode.com
"""

'''Menus & toolbars in Tkinter'''

# In this part of the Tkinter tutorial, we will work with menus and toolbar.
# A menubar is one of the most visible parts of the GUI application. 
# It is a group of commands located in various menus. 
# While in console applications we must remember many arcane commands, here we have most of the commands grouped into logical parts. 
# There are accepted standards that further reduce the amount of time spending to learn a new application. 
# Menus group commands that we can use in an application. 
# Toolbars provide a quick access to the most frequently used commands.

'''Simple menu'''

#The first example will show a simple menu.
#Our example will show a menu with one item. 
#By selecting the exit menu item we close the application.
from Tkinter import Tk, Frame, Menu


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Simple menu")
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        #Here we create a menubar. 
        #It is a regular Menu widget configured to be the menubar of the root window.
        
        fileMenu = Menu(menubar)
        #We create a file menu object. 
        #A menu is a popup window containing commands.
        fileMenu.add_command(label="Exit", command=self.onExit)
        #We add a command to the file menu. 
        #The command will call the onExit() method.
        menubar.add_cascade(label="File", menu=fileMenu)
        #The file menu is added to the menubar.
        

    def onExit(self):
        self.quit()


def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  