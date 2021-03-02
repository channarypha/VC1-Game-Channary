# IMPORTS TK
import tkinter as tk
# LOAD THE LIBRARY FOR SOUND
import winsound
# IMAPORT MESSAGE
from tkinter import messagebox
# RANDOM IMPORT
import random

# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
X = -1
Y = -1

# VARIABLES
grid = [[0,0,1,1,1,4,1,2,0,5,1,1,1,1,1,1,2,0,0],
        [0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,4,1,0,0],
        [0,0,4,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1],
        [0,0,1,1,1,4,1,1,1,1,1,1,1,2,0,1,1,1,1],
        [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,4,0],
        [1,1,1,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0],
        [0,1,1,0,2,0,1,0,0,0,0,0,0,4,0,0,0,0,0],
        [3,1,4,0,1,0,1,0,0,1,1,1,1,1,0,0,0,0,0],
        [0,0,1,1,1,4,1,1,1,1,4,1,4,1,1,1,1,1,2],
        [0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0],
        [2,1,1,4,1,4,0,0,0,0,0,0,2,1,0,0,0,0,0],
        [1,1,4,0,0,1,1,2,1,0,0,0,0,1,1,4,0,0,0],
        [0,0,2,1,1,1,0,1,0,0,2,1,4,1,1,1,0,0,1],
        [0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,1,1,4,1],
        [1,4,1,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,1,1,0,0,0,0,4,1,1,0,2,1,1,0],
        [0,0,1,1,1,2,1,0,0,1,1,1,0,0,0,0,1,0,0]]

# ARRAY OF IMAGES
arrayOfImages = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "bad-angrybird.png"]

# FUNCTION TO KNOW POSITION OF PLAYER
def getIndex3():
    global X,Y
    for index in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[index][i] == 3:
                Y =index
                X = i

# FUNCTION TO DRAW
def arrayToDrawing():
    for i in range(len(grid)):
        y1 = 40 * i
        y2 = 40+ y1
        for j in range(len(grid[0])):
            x1 = j*40 + 300
            x2 = x1 + 40
            
            if grid[i][j] == 0:

                # LOAD THE IMAGE
                canvas.create_image(x1+20,y1+21, image=wall)
            else:
                # if grid[i][j] == 1:
                canvas.create_rectangle(x1, y1, x2, y2, fill = "#660066")  
                if grid[i][j] ==  3 :
                    # canvas.create_rectangle(x1, y1, x2, y2, fill = "#660066") 

                    # LOAD THE IMAGE
                    canvas.create_image(x1+20,y1+13, image=bird)
                
                elif grid[i][j] == 2 :
                    # canvas.create_rectangle(x1, y1, x2, y2, fill = "#660066")

                    # LOAD THE IMAGE
                    canvas.create_image(x1+20,y1+19, image=badbird)
                elif grid[i][j] == 5 :
                    # canvas.create_rectangle(x1, y1, x2, y2, fill = "green")

                    # LOAD THE IMAGE
                    canvas.create_image(x1+20,y1+20, image=goals)

# FUNCTION LEFT CLICK
def leftclick(event):
    global grid
    getIndex3()
    if X and grid[Y][X-1] == 1 or grid[Y][X-1] == 2 or grid[Y][X-1] == 5:
        grid[Y][X] = 1
        if grid[Y][X-1] == 2:
            grid[Y][X-1] = 3
            messagebox.showinfo("DEFEAT", "You lose !")
        if grid[Y][X-1] == 5:
            grid[Y][X-1] = 3
            messagebox.showinfo("SUCCESS", "You win !")
    # winsound.PlaySound("1918.mp3", winsound.SND_FILENAME)
    arrayToDrawing()
    print(grid)

# FUNCTION RIGHTCLICK
def rightclick(event):
    global grid
    getIndex3()
    if X<len(grid[0]) - 1 and grid[Y][X+1] == 1 or grid[Y][X+1] == 2 or grid[Y][X+1] == 5:
        grid[Y][X] = 1
        if grid[Y][X+1] == 1:
            grid[Y][X+1] = 3
        if grid[Y][X+1] == 2:
            grid[Y][X+1] = 3
            messagebox.showinfo("DEFEAT", "You lose !")
        if grid[Y][X+1] == 5:
            grid[Y][X+1] = 3
            messagebox.showinfo("SUCCESS", "You win !")
    # winsound.PlaySound("1918.mp3", winsound.SND_FILENAME)
    print(grid)
    arrayToDrawing()

# FUNCTION UPCLICK
def upclick(event):
    global grid 
    getIndex3() 
    if Y and grid[Y-1][X] == 1 or grid[Y-1][X] == 2 or grid[Y-1][X] == 5:
        grid[Y][X] = 1
        if grid[Y-1][X] == 1:
            grid[Y-1][X] = 3
        if grid[Y-1][X] == 2:
            grid[Y-1][X] = 3
            messagebox.showinfo("DEFEAT", "You lose !")
        if grid[Y-1][X] == 5:
            grid[Y-1][X] = 3
            messagebox.showinfo("SUCCESS", "You win !")
    # winsound.PlaySound("1918.mp3", winsound.SND_FILENAME)
    print(grid)
    arrayToDrawing()

# FUNCTION DOWNCLICK
def downclick(event):
    global grid
    getIndex3()
    if Y <len(grid)-1 and grid[Y+1][X] == 1 or grid[Y+1][X] == 2 or grid[Y+1][X] == 5:
        grid[Y][X] = 1
        if grid[Y+1][X] == 1:
            grid[Y+1][X] = 3
        if grid[Y+1][X] == 2:
            grid[Y+1][X] = 3
            messagebox.showinfo("DEFEAT", "You lose !")
        if grid[Y+1][X] == 5:
            grid[Y+1][X] = 3
            messagebox.showinfo("SUCCESS", "You win !")
    # winsound.PlaySound("1918.mp3", winsound.SND_FILENAME)
    print(grid)
    arrayToDrawing()

# PLAY THE SOUND 
# winsound.PlaySound("test.wav", winsound.SND_FILENAME)


root = tk.Tk()
#LEFT CLICK
root.bind ( " <Left> ", leftclick) 
#RIGHT CLICK
root.bind ( " <Right> ", rightclick) 
#UP CLICK
root.bind ( " <Up> ", upclick) 
#DOWN CLICK 
root.bind ( " <Down> ", downclick)  


# MAIN
root.geometry ( str (SCREEN_WIDTH) + "x" + str ( SCREEN_HEIGHT ) )
canvas = tk.Canvas (root)
canvas.pack(expand=True, fill="both")
# ADD THE IMAGES TO THE CANVAS
bird= tk.PhotoImage(file='cute-bird.png')
badbird= tk.PhotoImage(file=random.choice(arrayOfImages))
goals= tk.PhotoImage(file='goal.png')
wall= tk.PhotoImage(file='wall.png')
# CALL FUNCTION TO DRAW
arrayToDrawing()
# CALL ROOT
root.mainloop()

# 1.BLUE GRID
# 2.ENEMIES
# 3.CUTE BIRD OF PLAYER
# 4.FOOD OR COIN OR ANYTHING ELSE
# 5.GOAL