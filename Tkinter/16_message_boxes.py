#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this program, we show various
message boxes.

author: Jan Bodnar
last modified: January 2011
website: www.zetcode.com
"""

'''Dialogs in Tkinter'''

# In this part of the Tkinter tutorial, we will work with dialogs.
# Dialog windows or dialogs are an indispensable part of most modern GUI applications. 
# A dialog is defined as a conversation between two or more persons. 
# In a computer application a dialog is a window which is used to "talk" to the application. 
# A dialog is used to input data, modify data, change the application settings etc. 
# Dialogs are important means of communication between a user and a computer program.

'''Message boxes'''

# Message boxes are convenient dialogs that provide messages to the user of the application. 
# The message consists of text and image data. 
# Message boxes in Tkinter are located in the tkMessageBox module.


# We use the grid manager to set up a grid of four buttons. 
# Each of the buttons shows a different message box.
from ttk import Frame, Button, Style
from Tkinter import Tk, BOTH
import tkMessageBox as box
# We import the tkMessageBox which has the functions that show dialogs.


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Message boxes")
        self.style = Style()
        self.style.theme_use("default")        
        self.pack()
        
        error = Button(self, text="Error", command=self.onError)
        #We create an error button, which calls the onError() method. 
        #Inside the method, we show the error message dialog.
        error.grid()
        warning = Button(self, text="Warning", command=self.onWarn)
        warning.grid(row=1, column=0)
        question = Button(self, text="Question", command=self.onQuest)
        question.grid(row=0, column=1)
        inform = Button(self, text="Information", command=self.onInfo)
        inform.grid(row=1, column=1)


    # In case we pressed the error button, we show the error dialog. 
    # We use the showerror() function to show the dialog on the screen. 
    # The first parameter of this method is the title of the message box, the second parameter is the actual message.
    def onError(self):
        box.showerror("Error", "Could not open file")

    def onWarn(self):
        box.showwarning("Warning", "Deprecated function call")
        
    def onQuest(self):
        box.askquestion("Question", "Are you sure to quit?")
        
    def onInfo(self):
        box.showinfo("Information", "Download completed")
         

def main():
  
    root = Tk()
    ex = Example(root)
    root.geometry("300x150+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()  