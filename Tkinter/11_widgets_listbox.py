#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we show how to
use the Listbox widget.

author: Jan Bodar
last modified: December 2010
website: www.zetcode.com
"""

'''Listbox'''

#Listbox is a widget that displays a list of objects. 
#It allows the user to select one or more items.

#In our example, we show a list of actresses in the Listbox. 
#The currently selected actress is displayed in a label widget.
from ttk import Frame, Label, Style
from Tkinter import Tk, BOTH, Listbox, StringVar, END


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Listbox") 
        
        self.pack(fill=BOTH, expand=1)

        acts = ['Scarlett Johansson', 'Rachel Weiss', 
            'Natalie Portman', 'Jessica Alba']
        #This is a list of actresses to be shown in the listbox.

        lb = Listbox(self)
        for i in acts:
            lb.insert(END, i)
        #We create an instance of the Listbox and insert all the items from the above mentioned list.
            
        lb.bind("<<ListboxSelect>>", self.onSelect)
        #When we select an item in the listbox, the <<ListboxSelect>> event is generated. 
        #We bind the onSelect() method to this event.
        
        lb.place(x=20, y=20)

        self.var = StringVar()
        self.label = Label(self, text=0, textvariable=self.var)
        #A label and its value holder is created. 
        #In this label we will display the currently selected item.
        self.label.place(x=20, y=210)

    def onSelect(self, val):
      
        sender = val.widget
        #We get the sender of the event. 
        #It is our listbox widget.
        idx = sender.curselection()
        #We find out the index of the selected item using the curselection() method.
        value = sender.get(idx)
        #The actual value is retrieved with the get() method, which takes the index of the item.
        self.var.set(value)
        #Finally, the label is updated.
         

def main():
  
    root = Tk()
    ex = Example(root)
    root.geometry("300x250+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()  