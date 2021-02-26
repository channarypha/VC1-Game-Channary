# IMPORTS
import tkinter as tk

# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
X = -1
Y = -1
# VARIABLES
grid = [[0,0,0,0,0,0,0,2,0,5,1,1,1,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],[0,0,1,1,1,1,1,1,1,1,1,1,1,2,0,1,1,1,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0],[0,0,1,0,2,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[3,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],[0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],[2,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,2,1,1,1,0,0,0,0,2,1,1,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0]]
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
                canvas.create_rectangle(x1, y1, x2, y2, fill = "gray")  
            elif grid[i][j] ==  3 :
                canvas.create_rectangle(x1, y1, x2, y2, fill = "black") 
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

    
    arrayToDrawing()
    print(grid)

    # call again the draw

    
def rightclick(event):
    global grid
    getIndex3()
    if X<len(grid[0]) - 1 and grid[Y][X+1] == 1:
        grid[Y][X] = 1
        grid[Y][X+1] = 3
    print(grid)
    
    arrayToDrawing()
def upclick(event):
    global grid 
    getIndex3() 
    if Y and grid[Y-1][X] == 1:
            grid[Y][X] = 1
            grid[Y-1][X] = 3
    print(grid)
    arrayToDrawing()
def downclick(event):
    global grid
    getIndex3()
    if Y <len(grid)-1 and grid[Y+1][X] == 1:
            grid[Y][X] = 1
            grid[Y+1][X] = 3
    print(grid)
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

root.geometry ( str (SCREEN_WIDTH) + "x" + str ( SCREEN_HEIGHT ) )

canvas = tk.Canvas (root)
canvas.pack(expand=True, fill="both")
arrayToDrawing()

root.mainloop()