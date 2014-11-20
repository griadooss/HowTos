#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we show how to
use the Scale widget.

author: Jan Bodnar
last modified: December 2010
website: www.zetcode.com
"""

'''Scale'''

# Scale is a widget that lets the user graphically select a value by sliding a knob within a bounded interval. 
# Our example will show a selected number in a label widget.

# We have two widgets in the below script: a scale and a label. 
# A value from the scale widget is shown in the label widget.
from ttk import Frame, Label, Scale, Style
from Tkinter import Tk, BOTH, IntVar


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Scale")
        self.style = Style()
        self.style.theme_use("default")        
        
        self.pack(fill=BOTH, expand=1)

        scale = Scale(self, from_=0, to=100, 
            command=self.onScale)
        #Scale widget is created. 
        #We provide the lower and upper bounds. 
        #The from is a regular Python keyword that is why there is an underscore after the first parameter. 
        #When we move the knob of the scale, the onScale() method is called.
        scale.place(x=20, y=20)

        self.var = IntVar()
        self.label = Label(self, text=0, textvariable=self.var)
        #An integer value holder and label widget are created. 
        #Value from the holder is shown in the label widget.
        self.label.place(x=130, y=70)

    #The onScale() method receives a currently selected value from the scale widget as a parameter. 
    #The value is first converted to a float and then to integer. 
    #Finally, the value is set to the value holder of the label widget.
    def onScale(self, val):
     
        v = int(float(val))
        self.var.set(v)
         

def main():
  
    root = Tk()
    ex = Example(root)
    root.geometry("300x150+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()  
