#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we draw text
on the window.

author: Jan Bodar
last modified: December 2010
website: www.zetcode.com
"""

'''Drawing text'''

# In the last example, we are going to draw text on the window.

# We draw a lyrics of a song on the window.
from Tkinter import Tk, Canvas, Frame, BOTH, W


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Lyrics")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_text(20, 30, anchor=W, font="Purisa",
            text="Most relationships seem so transitory")
        canvas.create_text(20, 60, anchor=W, font="Purisa",
            text="They're good but not the permanent one")
        canvas.create_text(20, 130, anchor=W, font="Purisa",
            text="Who doesn't long for someone to hold")
        canvas.create_text(20, 160, anchor=W, font="Purisa",
            text="Who knows how to love without being told")                   
        canvas.create_text(20, 190, anchor=W, font="Purisa",
            text="Somebody tell me why I'm on my own")            
        canvas.create_text(20, 220, anchor=W, font="Purisa",
            text="If there's a soulmate for everyone")
        #The first two parameters are the x and y coordinates of the center point of the text. 
        #If we anchor the text item to the west, the text starts from this position. 
        #The font parameter provides the font of the text and the text parameter is the text to be displayed.
        canvas.pack(fill=BOTH, expand=1)


def main():
  
    root = Tk()
    ex = Example(root)
    root.geometry("420x250+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()  