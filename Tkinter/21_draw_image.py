#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we draw an image
on the canvas.

author: Jan Bodar
last modified: December 2010
website: www.zetcode.com
"""

'''Drawing image'''

# In the following example we will create an image item on the canvas.

# We display an image on the canvas.
from Tkinter import Tk, Canvas, Frame, BOTH, NW
import Image 
import ImageTk

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("High Tatras")        
        self.pack(fill=BOTH, expand=1)
        
        self.img = Image.open("tatras.jpg")
        self.tatras = ImageTk.PhotoImage(self.img)
        #Tkinter does not support JPG images internally. 
        #As a workaround, we use the Image and ImageTk modules.

        canvas = Canvas(self, width=self.img.size[0]+20, 
           height=self.img.size[1]+20)
        #We create the Canvas widget. 
        #It takes the size of the image into account. 
        #It is 20 px wider and 20 px higher than the actual image size.


        canvas.create_image(10, 10, anchor=NW, image=self.tatras)
        #We use the create_image() method to create an image item on the canvas. 
        #To show the whole image, it is anchored to the north and to the west. 
        #The image parameter provides the photo image to display.


        canvas.pack(fill=BOTH, expand=1)


def main():
  
    root = Tk()
    ex = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
