#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
ZetCode Tkinter tutorial

In this script, we use the Label
widget to show an image.

author: Jan Bodnar
last modified: December 2010
website: www.zetcode.com
"""
'''Label'''
#The Label widget is used to display text or images. No user interaction is available.
#               sudo apt-get install python-imaging-tk
#In order to run this example, we must install python-imaging-tk module.


#Our example shows an image on the window.
from PIL import Image, ImageTk
#By default, the Label widget can display only a limited set of image types. 
#To display a JPG image, we must use the PIL, Python Imaging Library module.
from Tkinter import Tk, Frame, Label


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Label")

        self.img = Image.open("tatras.jpg")
        tatras = ImageTk.PhotoImage(self.img)
        #We create an image from the image file in the current working directory. 
        #Later we create a photo image from the image.
        label = Label(self, image=tatras)
        #The photoimage is given to the image parameter of the label widget.

        label.image = tatras
        #In order not to be garbage collected, the image reference must be stored.
        label.pack()

        self.pack()
        
    def setGeometry(self):
      
        w, h = self.img.size
        self.parent.geometry(("%dx%d+300+300") % (w, h))
        #We make the size of the window to exactly fit the image size.
        

def main():
  
    root = Tk()
    ex = Example(root)
    ex.setGeometry()
    root.mainloop()  


if __name__ == '__main__':
    main()  