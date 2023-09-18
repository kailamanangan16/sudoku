from tkinter import *
from functions import *

window = Tk() # makes tkinter window

ex = [
  [3,2,4,1,5,6,7,8,9],
  ['','','','','','','','',''],
  ['','','','','','','','',''],
  ['','',1,'','','','','',''],
  ['','','','','','','','',''],
  ['','','','','','','','',''],
  ['','','','','','','','',''],
  ['','','','','','','','',''],
  ['','','','','','','','',''],
  ]

probOne = Sudoku(ex)

for i in range(probOne.dim): # rows
    for j in range(probOne.dim): # columns
        sudokuGrid = Label(window, text = str(probOne.problem[i][j]), relief = GROOVE, width = 20, height = 5)
        sudokuGrid.grid(row = i, column = j)

#variables
row = IntVar()
col = IntVar()
num = IntVar()

#labels for entry
enterLabelRow = Label(window, text ="What row?")
enterLabelCol = Label(window, text = "What column?")
enterLabelNum = Label(window, text = "What number?")
statusLabel = Label(window, text = '')

#entries
enterEntryRow = Entry(window, textvariable = row)
enterEntryCol = Entry(window, textvariable = col)
enterEntryNum = Entry(window, textvariable = num)

def addNum():
    if row.get() < 0 or row.get() > probOne.dim or col.get() < 0 or col.get() > probOne.dim or num.get() < 0 or num.get() > probOne.dim:
        statusLabel = Label(window, text = "Number out of range")
        statusLabel.grid(row = probOne.dim+5, column = 0)
    elif probOne.add(row.get(), col.get(), num.get()):
        for i in range(probOne.dim): # rows
            for j in range(probOne.dim): # columns
                sudokuGrid = Label(window, text = str(probOne.problem[i][j]), relief = GROOVE, width = 20, height = 5)
                sudokuGrid.grid(row = i, column = j)
    else:
        statusLabel = Label(window, text = "Unable to add number")
        statusLabel.grid(row = probOne.dim+5, column = 0)

def clear():
    probOne.clearBoard()
    for i in range(probOne.dim): # rows
        for j in range(probOne.dim): # columns
            sudokuGrid = Label(window, text = str(probOne.problem[i][j]), relief = GROOVE, width = 20, height = 5)
            sudokuGrid.grid(row = i, column = j)
    statusLabel = Label(window, text = "Board Cleared")
    statusLabel.grid(row = probOne.dim+5, column = 0)

def checkWork():
    if probOne.gameOver():
        statusLabel = Label(window, text = "Good Job!")
        statusLabel.grid(row = probOne.dim+5, column = 0) 
    else:
        statusLabel = Label(window, text = "Not Done!")
        statusLabel.grid(row = probOne.dim+5, column = 0) 


#buttons
enterButton = Button(window, text = "Enter", command=lambda: addNum())
clearButton = Button(window, text = "Clear", command=lambda: clear())
checkButton = Button(window, text = "Check Work", command=lambda: checkWork())

#display
enterLabelRow.grid(row = probOne.dim+1, column = 0)
enterLabelCol.grid(row = probOne.dim+2, column = 0)
enterLabelNum.grid(row = probOne.dim+3, column = 0)

enterEntryRow.grid(row = probOne.dim+1, column = 1)
enterEntryCol.grid(row = probOne.dim+2, column = 1)
enterEntryNum.grid(row = probOne.dim+3, column = 1)

enterButton.grid(row = probOne.dim+4, column = 0)
clearButton.grid(row = probOne.dim+4, column = 1)
checkButton.grid(row = probOne.dim+4, column = 2)
statusLabel.grid(row = probOne.dim+5, column = 1)


window.mainloop() # runs tkinter in a loop