# Bethany Fannin
# CSC-131-007
# Nov 10, 2020
# Lab 20
#
# Purpose: To practice programming with objects using Python's turtle modules
#
# Variables: 
# =======================

import turtle
import math

# function definitions goes here

def drawX(Xturtle, window):
    '''
    Draws an 'X' shape across the window, using
    the user input to determine window size.
    '''
    width = window.window_width()
    height = window.window_height()

    Xturtle.penup()
    Xturtle.setposition(-width/2, height/2)
    Xturtle.pendown()
    Xturtle.setposition(width/2, -height/2)
    Xturtle.penup()
    Xturtle.setposition(width/2, height/2)
    Xturtle.pendown()
    Xturtle.setposition(-width/2, -height/2)

def drawW(Wturtle, window):
    '''
    Draw the shape of a 'W' in the
    middle of the window determined by
    the user's input
    '''
    width = window.window_width()
    height = window.window_height()

    Wturtle.penup()
    Wturtle.setposition(-100,50)
    Wturtle.pendown()
    Wturtle.right(45)
    Wturtle.forward(100)
    Wturtle.left(90)
    Wturtle.forward(100)
    Wturtle.left(270)
    Wturtle.forward(100)
    Wturtle.left(90)
    Wturtle.forward(100)

def drawCircle(circle, center, radius):
    '''
    Draw the specified circle within the turtle
    window specified by the user input.
    '''
    distance = 2.0* math.pi * radius / 120

    circle.penup()
    circle.setposition(center[0], center[1])
    for i in range(0,120):
        circle.pendown()
        circle.forward(distance)
        circle.left(3)

def movingTurtle(mTurtle, window):
    '''
    Create turtle that is the shape of an actual
    turtle, then have it move from the bottom of screen
    to the top, getting smaller as it moves along its path
    '''

    height = window.window_height()

    bottom = -height // 2
    top = height // 2
    size = 15

    mTurtle.shape("turtle")
    mTurtle.shapesize(size)
    mTurtle.setheading(90) # turtle faces upward direction
    mTurtle.penup()
    mTurtle.sety(bottom)
    

    
    for i in range(bottom + 1, top):
        mTurtle.sety(i)
        if size >= 1:
            size -= size*.005
            mTurtle.shapesize(size)
        else:
            size = 1
            mTurtle.shapesize(size)

        
    
    

def main():
    # set window size
    width = int(input('Enter the width of the screen: '))
    height = int(input('Enter the height of the screen: '))
    turtle.setup(width,height)
    print('='*50)
    #========================================================
    # get reference to turtle window
    window = turtle.Screen()
    # set window title bar
    window.title('Lab20 - Turtle Object')
    #========================================================
    # Draw X
    Xturtle = turtle.Turtle()
    # function call
    try:
        drawX(Xturtle, window)
    except:
        print('drawX is not either defined or there is a',
              'problem with the function')
    print('='*50)
    #========================================================
    # Draw W
    Wturtle = turtle.Turtle()
    # function call
    try:
        drawW(Wturtle, window)
    except:
        print('drawW is not either defined or there is a',
              'problem with the function')
    print('='*50)
    #========================================================
    # Draw circle
    # Test the function with differen values for center and radius
    circle = turtle.Turtle()
    center = [[0,0], [100, 0], [100, 100]]
    radius = [100, 50, 200]
    # function call
    for i in range(len(center)):
        try:
            drawCircle(circle, center[i], radius[i])
        except:
            print('drawCircle is not either defined or there is a',
                  'problem with the function')

    print('='*50)
    #========================================================    
    # Moving turtle
    mTurtle = turtle.Turtle()
    # function call
    try:
        movingTurtle(mTurtle,window)
    except:
        print('movingTurtle is not either defined or there is a',
              'problem with the function')
    #========================================================

main()
