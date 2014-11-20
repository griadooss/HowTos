#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we lay out images
using absolute positioning.

author: Jan Bodnar
last modified: December 2010
website: www.zetcode.com
"""

'''Layout management in Tkinter:'''
#In this part of the Tkinter programming tutorial, we will introduce layout managers.
#When we design the GUI of our application, we decide what widgets we will use and how 
#we will organise those widgets in the application. 
#To organise our widgets, we use specialised non visible objects called layout managers.
#
#There are two kinds of widgets: containers and their children. 
#The containers group their children into suitable layouts.
# 
# Tkinter has three built-in layout managers. The pack, grid, and place managers. 
# The pack geometry manager organises widgets in horizontal and vertical boxes. 
# The grid geometry managers places widgets in a two dimensional grid. 
# Finally, the place geometry manager places widgets on their containers using absolute positioning.
# 
'''Absolute positioning:'''
# In most cases, programmers should use layout managers. 
# There are a few situations, where we can use absolute positioning. 
# In absolute positioning, the programmer specifies the position and the size of each widget in pixels. 
# The size and the position of a widget do not change if you resize a window. 
# Applications look different on various platforms, and what looks OK on Linux, might not look OK on Mac OS. 
# Changing fonts in your application might spoil the layout. 
# If you translate your application into another language, you must redo your layout.



#In this example, we place three images using absolute positioning. We will use the place geometry manager.
from PIL import Image, ImageTk
#We will use Image and ImageTk from the Python Imaging Library (PIL) module. [Install 'python-imaging-tk' from repositories]
from Tkinter import Tk, Label, BOTH
from ttk import Frame, Style

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)
        
        style = Style()
        style.configure("TFrame", background="#333")        
        
        bard = Image.open("bardejov.jpg")
        bardejov = ImageTk.PhotoImage(bard)
        #We create an image object and a photo image object from an image in the current working directory.
        label1 = Label(self, image=bardejov)
        #We create a Label with an image. Labels can contain text or images.
        label1.image = bardejov
        #We must keep the reference to the image to prevent image from being garbage collected.
        label1.place(x=20, y=20)
        #The label is placed on the frame at x=20, y=20 coordinates.
        
        rot = Image.open("rotunda.jpg")
        rotunda = ImageTk.PhotoImage(rot)
        label2 = Label(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=40, y=160)        
        
        minc = Image.open("mincol.jpg")
        mincol = ImageTk.PhotoImage(minc)
        label3 = Label(self, image=mincol)
        label3.image = mincol
        label3.place(x=170, y=50)        
              

def main():
  
    root = Tk()
    root.geometry("300x280+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  