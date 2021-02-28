# IMPORTS
import tkinter as tk
# Load the library for sounds 
import winsound
from tkinter import messagebox

# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
X = -1
Y = -1

# VARIABLES
grid = [[0,0,0,0,0,0,0,2,0,5,1,1,1,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,2,0,1,1,1,0],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0],
        [0,0,1,0,2,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
        [3,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],
        [2,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,2,1,1,1,0,0,0,0,2,1,1,1,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0]]


# FUNCTION
def getIndex3():
    global X,Y
    for index in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[index][i] == 3:
                Y =index
                X = i


def arrayToDrawing():
    for i in range(len(grid)):
        y1 = 40 * i
        y2 = 40+ y1
        for j in range(len(grid[0])):
            x1 = j*40
            x2 = x1 + 40
            if grid[i][j] == 1:
                canvas.create_rectangle(x1, y1, x2, y2, fill = "pink")  
            elif grid[i][j] ==  3 :
                # canvas.create_rectangle(x1, y1, x2, y2, fill = "black") 
                canvas.create_image(x1+20,y1+25, image=Robot)
               
            elif grid[i][j] == 2 :
                canvas.create_rectangle(x1, y1, x2, y2, fill = "red")
            elif grid[i][j] == 5 :
                canvas.create_rectangle(x1, y1, x2, y2, fill = "green")

# draw a line with white and black squares using the global array
def leftclick(event):
    global grid
    getIndex3()
    if X and grid[Y][X-1] == 1:
        grid[Y][X] = 1
        grid[Y][X-1] = 3
    elif X and grid[Y][X-1] == 2:
        messagebox.showinfo("DEFEAT", "You lose !")
    elif X and grid[Y][X-1] == 5:
        messagebox.showinfo("SUCCESS", "You win !")
    # winsound.PlaySound("1918.mp3", winsound.SND_FILENAME)
    arrayToDrawing()
    print(grid)

    # call again the draw

    
def rightclick(event):
    global grid
    getIndex3()
    if X<len(grid[0]) - 1 and grid[Y][X+1] == 1:
        grid[Y][X] = 1
        grid[Y][X+1] = 3
    elif X<len(grid[0]) - 1 and grid[Y][X+1] == 2:
        messagebox.showinfo("DEFEAT", "You lose !")
    elif X<len(grid[0]) - 1 and grid[Y][X+1] == 5:
        messagebox.showinfo("SUCCESS", "You win !")
    # winsound.PlaySound("1918.mp3", winsound.SND_FILENAME)
    print(grid)
    arrayToDrawing()
def upclick(event):
    global grid 
    getIndex3() 
    if Y and grid[Y-1][X] == 1:
            grid[Y][X] = 1
            grid[Y-1][X] = 3
    elif Y and grid[Y-1][X] == 2:
        messagebox.showinfo("DEFEAT", "You lose !")
    elif Y and grid[Y-1][X] == 5:
        messagebox.showinfo("SUCCESS", "You win !")
    # winsound.PlaySound("1918.mp3", winsound.SND_FILENAME)
    print(grid)
    arrayToDrawing()
def downclick(event):
    global grid
    getIndex3()
    if Y <len(grid)-1 and grid[Y+1][X] == 1:
        grid[Y][X] = 1
        grid[Y+1][X] = 3
    elif Y <len(grid)-1 and grid[Y+1][X] == 2:
        messagebox.showinfo("DEFEAT", "You lose !")
    elif Y <len(grid)-1 and grid[Y+1][X] == 5:
        messagebox.showinfo("SUCCESS", "You win !")
    # winsound.PlaySound("1918.mp3", winsound.SND_FILENAME)
    print(grid)
    arrayToDrawing()

# Play the sound 
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


# main
root.geometry ( str (SCREEN_WIDTH) + "x" + str ( SCREEN_HEIGHT ) )
canvas = tk.Canvas (root)
canvas.pack(expand=True, fill="both")
# images
Robot= tk.PhotoImage(file='image\\robot.png')

arrayToDrawing()

root.mainloop()