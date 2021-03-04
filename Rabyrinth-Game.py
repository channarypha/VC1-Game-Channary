# IMPORTS TK
import tkinter as tk
# LOAD THE LIBRARY FOR SOUND
import winsound
# IMAPORT MESSAGE
from tkinter import messagebox
# RANDOM IMPORT
import random

# CONSTANTS
SCREEN_WIDTH = 840
SCREEN_HEIGHT = 840
X = -1
Y = -1
# VARIABLE OF SCORE AND TIME LEFT
Score = 0
timeLeft = 30

# VARIABLES OF GRID (ARRAY 2D)
grid = [[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
        [7,0,0,1,1,1,4,1,2,0,5,1,1,1,1,1,1,2,0,0,7],
        [7,0,0,1,0,0,0,0,1,0,0,0,0,0,4,2,6,1,2,0,7],
        [7,0,0,4,2,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1,7],
        [7,0,0,1,1,1,4,1,1,1,1,6,1,1,2,0,1,1,1,1,7],
        [7,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,4,1,7],
        [7,2,6,1,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,7],
        [7,0,1,1,0,2,0,1,0,0,0,0,0,0,6,0,0,0,0,1,7],
        [7,3,1,4,0,1,0,1,0,0,1,1,1,1,1,0,0,0,1,1,7],
        [7,0,0,1,1,1,6,1,1,1,1,6,2,4,1,1,1,1,1,2,7],
        [7,0,0,1,0,0,1,1,1,0,0,0,0,1,1,0,0,0,1,1,7],
        [7,2,1,1,4,1,4,0,0,0,0,0,1,2,1,1,0,0,0,0,7],
        [7,1,1,6,1,2,1,1,2,1,0,1,1,0,0,1,6,0,0,0,7],
        [7,0,1,0,0,0,1,0,0,0,0,2,0,4,1,1,2,0,0,1,7],
        [7,0,1,0,0,0,1,0,0,0,0,1,1,0,0,1,1,1,4,1,7],
        [7,1,6,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,7],
        [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]]



# ARRAY OF IMAGES
arrayOfImages = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "bad-angrybird.png"]
    
# DISPLAY WIN 
def win():
    winsound .PlaySound('win.wav', winsound.SND_FILENAME)
    messagebox.showinfo("SUCCESS", "YOU WIN !")
    

# DISPLAY LOSE
def lose():
    winsound .PlaySound('gameover.wav', winsound.SND_FILENAME)
    messagebox.showinfo("DEFEAT", "YOU LOSE !")
    

# RANDOM IMAGES OF ENEMIES
# def randomEnemies():

# FUNCTION TO KNOW POSITION OF PLAYER
def getIndex3():
    global X,Y
    for index in range(len(grid)):        
        for i in range(len(grid[0])):
            if grid[index][i] == 3:
                Y = index
                X = i

# FUNCTION TO DRAW
def arrayToDrawing():
    for i in range(len(grid)):
        y1 = 40 * i + 50
        y2 = 40+ y1
        for j in range(len(grid[0])):
            x1 = j*40 #+ 300
            x2 = x1 + 40
            if grid[i][j] == 0:
                # LOAD THE IMAGE
                canvas.create_image(x1+22,y1+24, image=wall)
            elif grid[i][j] == 7 :
                canvas.create_rectangle(x1, y1, x2, y2, fill = "black")
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill = "#660066")  
                if grid[i][j] == 2 :
                    # LOAD THE IMAGE
                    canvas.create_image(x1+20,y1+19, image=badbird)
                elif grid[i][j] ==  3 :
                    # LOAD THE IMAGE
                    canvas.create_image(x1+20,y1+13, image=bird)
                elif grid[i][j] ==  4 :
                    # LOAD THE IMAGE
                    canvas.create_image(x1+20,y1+20, image=cakea)
                elif grid[i][j] == 5 :
                    # LOAD THE IMAGE
                    canvas.create_image(x1+20,y1+20, image=goals)
                elif grid[i][j] == 6 :
                    # LOAD THE IMAGE
                    canvas.create_image(x1+20,y1+13, image=cakeb)
    # SCORE TEXT
    canvas.create_text(40, 20, fill="green", font="Times 16 italic bold", text="Score: "+str(Score))
    # TIME LEFT
    canvas.create_text(200, 20, fill="green", font="Times 16 italic bold", text="Time Left: "+str(timeLeft))

    return None
                
# FUNCTION LEFT CLICK
def leftclick(event):
    global grid, Score, timeLeft, ScoreOfCoins
    getIndex3()
    if X and grid[Y][X-1] == 1 or grid[Y][X-1] == 2 or grid[Y][X-1] == 5 or grid[Y][X-1] == 4 or grid[Y][X-1] == 6:
        grid[Y][X] = 1
        if grid[Y][X-1] == 2:
            lose()
            grid[Y][X-1] = 3
            
        if grid[Y][X-1] == 5:
            win()
            grid[Y][X-1] = 3
            
        if grid[Y][X-1] == 4 or grid[Y][X-1] == 6 or grid[Y][X-1] == 1:
            if grid[Y][X-1] == 4 or grid[Y][X-1] == 6 :
                winsound .PlaySound('eat.wav', winsound.SND_FILENAME)
                Score += 10
            grid[Y][X-1] = 3
    timeLeft -= 1
    arrayToDrawing()

# FUNCTION RIGHTCLICK
def rightclick(event):
    global grid, Score, timeLeft
    getIndex3()
    if X<len(grid[0]) - 1 and grid[Y][X+1] == 1 or grid[Y][X+1] == 2 or grid[Y][X+1] == 5 or grid[Y][X+1] == 4 or grid[Y][X+1] == 6:
        grid[Y][X] = 1
        if grid[Y][X+1] == 2:
            lose()
            grid[Y][X+1] = 3
            
        if grid[Y][X+1] == 5:
            win()
            grid[Y][X+1] = 3
            
        if grid[Y][X+1] == 4 or grid[Y][X+1] == 6 or grid[Y][X+1] == 1:
            if grid[Y][X+1] == 4 or grid[Y][X+1] == 6 :
                winsound .PlaySound('eat.wav', winsound.SND_FILENAME)
                Score += 10
            grid[Y][X+1] = 3
    timeLeft -= 1
    arrayToDrawing()

# FUNCTION UPCLICK
def upclick(event):
    global grid, Score, timeLeft
    getIndex3() 
    if Y and grid[Y-1][X] == 1 or grid[Y-1][X] == 2 or grid[Y-1][X] == 5 or grid[Y-1][X] == 4 or grid[Y-1][X] == 6:
        grid[Y][X] = 1
        if grid[Y-1][X] == 2:
            lose()
            grid[Y-1][X] = 3
            
        if grid[Y-1][X] == 5:
            win()
            grid[Y-1][X] = 3
            
        if grid[Y-1][X] == 4 or grid[Y-1][X] == 6 or grid[Y-1][X] == 1:
            if grid[Y-1][X] == 4 or grid[Y-1][X] == 6 :
                winsound .PlaySound('eat.wav', winsound.SND_FILENAME)
                Score += 10
            grid[Y-1][X] = 3
    timeLeft -= 1
    arrayToDrawing()

# FUNCTION DOWNCLICK
def downclick(event):
    global grid, Score, timeLeft
    getIndex3()
    if Y <len(grid)-1 and grid[Y+1][X] == 1 or grid[Y+1][X] == 2 or grid[Y+1][X] == 5 or grid[Y+1][X] == 4 or grid[Y+1][X] == 6:
        grid[Y][X] = 1
        if grid[Y+1][X] == 2:
            lose()
            grid[Y+1][X] = 3
            
        if grid[Y+1][X] == 5:
            win()
            grid[Y+1][X] = 3
            
        if grid[Y+1][X] == 4 or grid[Y+1][X] == 6 or grid[Y+1][X] == 1:
            if grid[Y+1][X] == 4 or grid[Y+1][X] == 6 :
                winsound .PlaySound('eat.wav', winsound.SND_FILENAME)
                Score += 10
            grid[Y+1][X] = 3
    timeLeft -= 1
    arrayToDrawing()

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
# TITTLE
root.title('CHANNARY - PHA - GAMMER')
# CANVAS
canvas = tk.Canvas (root)
canvas.pack(expand=True, fill="both")
# ADD THE IMAGES TO THE CANVAS
bird= tk.PhotoImage(file='cute-bird.png')
badbird= tk.PhotoImage(file=random.choice(arrayOfImages))
goals= tk.PhotoImage(file='goal.png')
wall= tk.PhotoImage(file='wall.png')
cakea= tk.PhotoImage(file='a.png')
cakeb= tk.PhotoImage(file='b.png')
# CALL FUNCTION TO DRAW
arrayToDrawing()
# CALL ROOT
root.mainloop()

# 1.BLUE GRID
# 2.ENEMIES
# 3.CUTE BIRD OF PLAYER
# 4.FOOD OR COIN OR ANYTHING ELSE
# 5.GOAL
# 6.CAKE
# BLACK WALL