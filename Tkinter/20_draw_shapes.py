#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we draw basic 
shapes on the canvas.

author: Jan Bodar
last modified: January 2011
website: www.zetcode.com
"""

'''Shapes'''

# We can draw various shapes on the Canvas. 
# The following code example will show some of them.

# We draw five different shapes on the window: 
#        a circle, 
#        an ellipse, 
#        a rectangle, 
#        an arc, 
#        and a polygon. 
# Outlines are drawn in red and insides in green. 
# The width of the outline is 2px.
from Tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Shapes")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_oval(10, 10, 80, 80, outline="red", 
            fill="green", width=2)
        #Here the create_oval() method is used to create a circle item. 
        #The first four parameters are the bounding box coordinates of the circle. 
        #In other words, they are x and y coordinates of the top-left and bottom-right points of the box, 
        #in which the circle is drawn.
        canvas.create_oval(110, 10, 210, 80, outline="#f11", 
            fill="#1f1", width=2)
        canvas.create_rectangle(230, 10, 290, 60, 
            outline="#f11", fill="#1f1", width=2)
        #We create a rectangle item. 
        #The coordinates are again the bounding box of the rectangle to be drawn.
        canvas.create_arc(30, 200, 90, 100, start=0, 
            extent=210, outline="#f11", fill="#1f1", width=2)
        #This code line creates an arc. 
        #An arc is a part of the circumference of the circle. 
        #We provide the bounding box. 
        #The start parameter is the start angle of the arc. 
        #The extent is the angle size.
            
        points = [150, 100, 200, 120, 240, 180, 210, 
            200, 150, 150, 100, 200]
        canvas.create_polygon(points, outline='red', 
            fill='green', width=2)
        #A polygon is created. 
        #It is a shape with multiple corners. 
        #To create a polygon in Tkinter, we provide the list of polygon coordinates to the create_polygon() method.
        
        canvas.pack(fill=BOTH, expand=1)


def main():
  
    root = Tk()
    ex = Example(root)
    root.geometry("330x220+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()  ()  