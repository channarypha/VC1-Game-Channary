# IMPORTS
import tkinter as tk

# CONSTANTS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1500
X = -1
Y = -1
# VARIABLES
grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

indexOfone = 0
# FUNCTION
def getIndex1():
    global X,Y
    for index in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[index][i] == 1:
                indexOfone = i
                Y =index
                X = i


def arrayToDrawing():
    for i in range(len(grid)):
        y1 = 50 * i
        y2 = 50+ y1
        for j in range(len(grid[0])):
            x1 = j*50
            x2 = x1 + 50
            if grid[i][j] == 0:
                color = "pink"
            else:
                color = "black"
            canvas.create_oval(x1, y1, x2, y2, fill=color)

# draw a line with white and black squares using the global array
def leftclick(event):
    global grid
    getIndex1()
    if X :
        grid[Y][X] = 0
        grid[Y][X-1] = 1

    
    arrayToDrawing()
    print(grid)

    # call again the draw

    
def rightclick(event):
    global grid
    getIndex1()
    if X<len(grid[0])-1:
        grid[Y][X] = 0
        grid[Y][X+1] = 1
    print(grid)
    
    arrayToDrawing()
def upclick(event):
    global grid 
    getIndex1() 
    if Y :
            grid[Y][X] = 0
            grid[Y-1][X] = 1
    print(grid)
    arrayToDrawing()
def downclick(event):
    global grid
    getIndex1()
    if Y <len(grid)-1:
            grid[Y][X] = 0
            grid[Y+1][X] = 1
    print(grid)
    arrayToDrawing()
root = tk.Tk()
root.bind("<Left>", leftclick) #LEFT CLICK
root.bind("<Right>", rightclick)  #RIGHT CLICK
root.bind("<Up>", upclick)  #UP CLICK
root.bind("<Down>", downclick)  #DOWN CLICK
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))

canvas = tk.Canvas(root)
canvas.pack(expand=True, fill="both")
arrayToDrawing()

root.mainloop()