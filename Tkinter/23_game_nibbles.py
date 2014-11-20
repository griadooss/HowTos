#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial 

This is a simple Nibbles game
clone.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2011
"""

'''Nibbles in Tkinter'''

# In this part of the Tkinter tutorial, we will create a Nibbles game clone.
# 
# Nibbles is an older classic video game. 
# It was first created in late 70s. 
# Later it was brought to PCs. 
# In this game the player controls a snake. 
# The objective is to eat as many apples as possible. 
# Each time the snake eats an apple, its body grows. 
# The snake must avoid the walls and its own body.

'''Development'''

# The size of each of the joints of a snake is 10px. 
# The snake is controlled with the cursor keys. 
# Initially, the snake has three joints. 
# The game starts immediately. 
# When the game is finished, we display "Game Over" message in the center of the window.
# 
# We use the Canvas widget to create the game. 
# The objects in the game are images. 
# We use canvas methods to create image items. 
# We use canvas methods to find items on the canvas using tags and to do collision detection.

import sys
import random
from PIL import Image, ImageTk
from Tkinter import Tk, Frame, Canvas, ALL, NW

# First we will define some constants used in our game.
# The WIDTH and HEIGHT constants determine the size of the Board. 
# The DELAY constant determines the speed of the game. 
# The DOT_SIZE is the size of the apple and the dot of the snake. 
# The ALL_DOTS constant defines the maximum number of possible dots on the Board. 
# The RAND_POS constant is used to calculate a random position of an apple.
WIDTH = 300
HEIGHT = 300
DELAY = 100
DOT_SIZE = 10
ALL_DOTS = WIDTH * HEIGHT / (DOT_SIZE * DOT_SIZE)
RAND_POS = 27

x = [0] * ALL_DOTS
y = [0] * ALL_DOTS
# These two arrays store the x and y coordinates of all possible joints of a snake.

# The initGame() method initialises variables, loads images, and starts a timeout function.

class Board(Canvas):

    def __init__(self, parent):
        Canvas.__init__(self, width=WIDTH, height=HEIGHT, 
            background="black", highlightthickness=0)
         
        self.parent = parent 
        self.initGame()
        self.pack()
                       
    
    def initGame(self):

        self.left = False
        self.right = True
        self.up = False
        self.down = False
        self.inGame = True
        self.dots = 3
        
        self.apple_x = 100
        self.apple_y = 190

        for i in range(self.dots):
            x[i] = 50 - i * 10
            y[i] = 50
        
        try:
            self.idot = Image.open("dot.png")
            self.dot = ImageTk.PhotoImage(self.idot)    
            self.ihead = Image.open("head.png")
            self.head = ImageTk.PhotoImage(self.ihead)           
            self.iapple = Image.open("apple.png")
            self.apple = ImageTk.PhotoImage(self.iapple) 

        except IOError, e:
            print e
            sys.exit(1)
        #In these lines, we load our images. 
        #There are three images in the Nibbles game: the head, the dot, and the apple.

        self.focus_get()

        self.createObjects()
        self.locateApple()
        #The createObjects() method creates items on the canvas. 
        #The locateApple() puts an apple randomly on the canvas.
        self.bind_all("<Key>", self.onKeyPressed)
        #We bind the keyboard events to the onKeyPressed() method. 
        #The game is controlled with keyboard cursor keys.
        self.after(DELAY, self.onTimer)
        

    def createObjects(self):
    
        self.create_image(self.apple_x, self.apple_y, image=self.apple,
            anchor=NW, tag="apple")
        self.create_image(50, 50, image=self.head, anchor=NW,  tag="head")
        self.create_image(30, 50, image=self.dot, anchor=NW, tag="dot")
        self.create_image(40, 50, image=self.dot, anchor=NW, tag="dot")
    #In the createObjects() method, we create game objects on the canvas. 
    #These are canvas items. 
    #They are given initial x, y coordinates. 
    #The image parameter provides the image to be displayed. 
    #The anchor parameter is set to NW; this way the coordinates of the canvas item are the top-left points of the items. 
    #This is important if we want to be able to display images next to the borders of the root window. 
    #Try to delete the anchor and see what happens. 
    #The tag parameter is used to identify items on the canvas. 
    #One tag may be used for multiple canvas items.
   
    
    #The checkApple() method checks if the snake has hit the apple object. 
    #If so, we add another snake joint and call the locateApple().
    def checkApple(self):

        apple = self.find_withtag("apple")
        head = self.find_withtag("head")
        #The find_withtag() method finds an item on the canvas using its tag. 
        #We need two items. 
        #The head of the snake and the apple. 
        #Note that even if there is only one item with a given tag, the method returns a tuple. 
        #This is a case for the apple item. 
        #And later the apple item is accessed the following way: apple[0].
        
        x1, y1, x2, y2 = self.bbox(head)
        overlap = self.find_overlapping(x1, y1, x2, y2)
        #The bbox() method returns the bounding box points of an item. 
        #The find_overlapping() method finds colliding items for the given coordinates.
            
        for ovr in overlap:
          
            if apple[0] == ovr:
                
                x, y = self.coords(apple)
                self.create_image(x, y, image=self.dot, anchor=NW, tag="dot")
                self.locateApple()
            #If the apple collides with the head, we create a new dot item at the coordinates of the apple object. 
            #We call the locateApple() method, which deletes the old apple item from the canvas and creates and 
            #randomly positions a new one.
        
    
    #In the doMove() method we have the key algorithm of the game. 
    #To understand it, look at how the snake is moving. 
    #You control the head of the snake. 
    #You can change its direction with the cursor keys. 
    #The rest of the joints move one position up the chain. 
    #The second joint moves where the first was, the third joint where the second was etc.
    def doMove(self):
      
        dots = self.find_withtag("dot")
        head = self.find_withtag("head")
                
        items = dots + head
        
        z = 0
        while z < len(items)-1:
            c1 = self.coords(items[z])
            c2 = self.coords(items[z+1])
            self.move(items[z], c2[0]-c1[0], c2[1]-c1[1])
            z += 1
        #This code moves the joints up the chain.

        if self.left:
            self.move(head, -DOT_SIZE, 0)
        #Move the head to the left.
            
        if self.right: 
            self.move(head, DOT_SIZE, 0)

        if self.up:
            self.move(head, 0, -DOT_SIZE)

        if self.down:
            self.move(head, 0, DOT_SIZE)
            
    #In the checkCollisions() method, we determine if the snake has hit itself or one of the walls.
    def checkCollisions(self):

        dots = self.find_withtag("dot")
        head = self.find_withtag("head")
        
        x1, y1, x2, y2 = self.bbox(head)
        overlap = self.find_overlapping(x1, y1, x2, y2)
        
        for dot in dots:
            for over in overlap:
                if over == dot:
                  self.inGame = False
        #We finish the game if the snake hits one of its joints with the head.
            
        if x1 < 0:
            self.inGame = False
        
        if x1 > WIDTH - DOT_SIZE:
            self.inGame = False

        if y1 < 0:
            self.inGame = False
        
        if y1 > HEIGHT - DOT_SIZE:
            self.inGame = False
        #We finish the game if the snake hits the bottom of the Board.
        
    #The locateApple() method locates a new apple randomly on the board and deletes the old one.
    def locateApple(self):
    
        apple = self.find_withtag("apple")
        self.delete(apple[0])
        #Here we find and delete the apple that was eaten by the snake.
    
        r = random.randint(0, RAND_POS)
        #We get a random number from 0 to RAND_POS - 1.
        self.apple_x = r * DOT_SIZE
        r = random.randint(0, RAND_POS)
        self.apple_y = r * DOT_SIZE
        #These lines set the x and y coordinates of the apple object.


        self.create_image(self.apple_x, self.apple_y, anchor=NW,
            image=self.apple, tag="apple")
                
    #In the onKeyPressed() method of the Board class, we determine the keys that were pressed.
    def onKeyPressed(self, e): 
    
        key = e.keysym

        if key == "Left" and not self.right: 
            self.left = True
            self.up = False
            self.down = False
        #If we hit the left cursor key, we set left variable to true. 
        #This variable is used in the doMove() method to change coordinates of the snake object. 
        #Notice also that when the snake is heading to the right, we cannot turn immediately to the left.
        

        if key == "Right" and not self.left:
            self.right = True
            self.up = False
            self.down = False
        

        if key == "Up" and not self.down:
            self.up = True
            self.right = False
            self.left = False
        

        if key == "Down" and not self.up: 
            self.down = True
            self.right = False
            self.left = False
            
            
    def onTimer(self):

        if self.inGame:
            self.checkCollisions()
            self.checkApple()
            self.doMove()
            self.after(DELAY, self.onTimer)
        else:
            self.gameOver()
    #Every DELAY ms, the onTimer() method is called. 
    #If we are in the game, we call three methods that build the logic of the game. 
    #Otherwise the game is finished. 
    #The timer is based on the after() method, which calls a method after DELAY ms only once. 
    #To repeatedly call the timer, we recursively call the onTimer() method.
            
             
    def gameOver(self):

        self.delete(ALL)
        self.create_text(self.winfo_width()/2, self.winfo_height()/2, 
            text="Game Over", fill="white")
    #If the game is over, we delete all items on the canvas. 
    #Then we draw "Game Over" in the center of the screen.


class Nibbles(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
                
        parent.title('Nibbles')
        self.board = Board(parent)
        self.pack()


def main():

    root = Tk()
    nib = Nibbles(root)
    root.mainloop()  


if __name__ == '__main__':
    main()