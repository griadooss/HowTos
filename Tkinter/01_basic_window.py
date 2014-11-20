#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
ZetCode Tkinter tutorial

This script shows a simple window
on the screen.

author: Jan Bodnar
last modified: January 2011
website: www.zetcode.com
"""

#While this code is very small, the application window can do quite a lot. 
#It can be resized, maximized, minimized. 
#All the complexity that comes with it has been hidden from the application programmer.
from Tkinter import Tk, Frame, BOTH
#Here we import Tk and Frame classes. 
#The first class is used to create a root window. 
#The latter is a container for other widgets.
class Example(Frame):
        
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        #Our example class inherits from the Frame container widget. 
        #In the __init__() constructor method we call the constructor of our inherited class. 
        #The background parameter specifies the background color of the Frame widget.
        
        self.parent = parent
        #We save a reference to the parent widget. The parent widget is the Tk root window in our case.'''
        self.initUI()
        #We delegate the creation of the user interface to the initUI() method.
        
        
    def initUI(self):
        self.parent.title("Simple")
        #We set the title of the window using the title() method.
        self.pack(fill=BOTH, expand=1)
        #The pack() method is one of the three geometry managers in Tkinter. 
        #It organizes widgets into horizontal and vertical boxes. 
        #Here we put the Frame widget, accessed via the self attribute to the Tk root window. 
        #It is expanded in both directions. In other words, it takes the whole client space of the root window.

    
def main():
    root = Tk()
    #The root window is created. 
    #The root window is a main application window in our programs. 
    #It has a title bar and borders. 
    #These are provided by the window manager. 
    #It must be created before any other widgets.
    root.geometry("250x150+300+300")
    #The geometry() method sets a size for the window and positions it on the screen. 
    #The first two parameters are width and height of the window. 
    #The last two parameters are x and y screen coordinates.
    app = Example(root)
    #Here we create the instance of the application class.
    root.mainloop()
    #Finally, we enter the mainloop. 
    #The event handling starts from this point. 
    #The mainloop receives events from the window system and dispatches them to the application widgets. 
    #It is terminated when we click on the close button of the titlebar or call the quit() method.    
if __name__ == '__main__':
    main()
    
    
    