#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
ZetCode Tkinter tutorial

This program creates a quit
button. When we press the button,
the application terminates. 

author: Jan Bodnar
last modified: December 2010
website: www.zetcode.com
"""
#In this example we will create a quit button. 
#When we press this button, the application terminates.
from Tkinter import Tk, BOTH
from ttk import Frame, Button, Style
#Tkinter supports theming of widgets. Widgets that are themed can be imported from the ttk module. 
#At the time of this writing (January 6, 2011), not all widgets are themable. 
#For instance, menus or listboxes are not supported so far.

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        self.parent.title("Quit button")
        self.style = Style()
        self.style.theme_use("default")
        #We apply a theme for our widgets. 
        #Some of the supported themes are clam, default, alt or classic.
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text="Quit", command=self.quit)
        #We create an instance of the Button widget. 
        #The parent of this button is the Frame container. 
        #We provide a label for the button and a command. 
        #The command specifies a method that is called when we press the button. 
        #In our case the quit() method is called, which terminates the application.
        quitButton.place(x=50, y=50)
        #We use the place geometry manager to position the button in absolute coordinates. 
        #50x50px from the top-left corner of the window.

def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
    