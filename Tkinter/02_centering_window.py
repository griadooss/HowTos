#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This script centers a small
window on the screen. 

author: Jan Bodnar
last modified: January 2011
website: www.zetcode.com
"""

#This script centers a window on the screen.
from Tkinter import Tk, Frame, BOTH

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        self.parent.title("Centered window")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

    def centerWindow(self):
        #We need to have the size of the window and the size of the screen to position the window in the center of the monitor screen.
        w = 290
        h = 150
        #These are the width and height values of the application window.
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        #We determine the width and height of the screen.
        x = (sw - w)/2
        y = (sh - h)/2
        #We calculate the required x and y coordinates.
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
        #Finally, the geometry() method is used to place the window in the center of the screen.

def main():
  
    root = Tk()
    ex = Example(root)
    root.mainloop()  

    
if __name__ == '__main__':
    main()


