#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This program draws three
rectangles filled with different
colors.

author: Jan Bodar
last modified: January 2011
website: www.zetcode.com
"""

'''Drawing in Tkinter'''
# In this part of the Tkinter tutorial we will do some drawing. 
# Drawing in Tkinter is done on the Canvas widget. 
# Canvas is a high-level facility for doing graphics in Tkinter.
# It can be used to create charts, custom widgets, or create games.

'''Colours'''
# A colour is an object representing a combination of Red, Green, and Blue (RGB) intensity values.

# In the code example, we draw three rectangles and fill them with different colour values.
from Tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Colors")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        #We create the Canvas widget.
        canvas.create_rectangle(30, 10, 120, 80, 
            outline="#fb0", fill="#fb0")
        canvas.create_rectangle(150, 10, 240, 80, 
            outline="#f50", fill="#f50")
        canvas.create_rectangle(270, 10, 370, 80, 
            outline="#05f", fill="#05f")
        #The create_rectangle() creates a rectangle item on the canvas. 
        #The first four parameters are the x and y coordinates of the two bounding points. 
        #The top-left and the bottom-right. 
        #With the outline parameter we control the colour of the outline of the rectangle. 
        #Likewise, the fill parameter provides a colour for the inside of the rectangle.
        canvas.pack(fill=BOTH, expand=1)


def main():
  
    root = Tk()
    ex = Example(root)
    root.geometry("400x100+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()  