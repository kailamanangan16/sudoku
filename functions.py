from tkinter import *

class Sudoku:
  def __init__(self, problem):
    self.problem = problem #the actual board
    self.problemOg = problem #the actual board
    self.dim = len(problem[0]) #dimensions of the sudoku board
    self.permNum = []
    for i in range(self.dim):
      for n in range(self.dim):
        if self.problem[i][n] != '':
          self.permNum.append((i,n))
    
  def clearBoard(self):
    for i in range(self.dim):
      for j in range(self.dim):
        if (i,j) not in self.permNum:
          self.problem[i][j] = ''

  def checkAdd(self, x, y):
    nums = [] #adds a number to check
    
    for i in range(self.dim): #go through row
      if self.problem[i][x] not in nums:
        if self.problem[i][x] == '':
          pass
        else:
          nums.append(self.problem[i][x])
      else:
        return False
        
    nums = []
    for i in range(self.dim): #go through column
      if self.problem[y][i] not in nums:
        if self.problem[y][i] == '':
          pass
        else:
          nums.append(self.problem[y][i])
      else:
        return False
    return True
    
  def add(self, row, col, num):
    if self.problem[row-1][col-1] == '': #if 0
      self.problem[row-1][col-1] = num #add num in
      if self.checkAdd(col-1, row-1) == False: #change back if invalid
        self.problem[row-1][col-1] = ''
        return False
      else: #otherwise, you can add it in
        self.problem[row-1][col-1] = num
        return True
    else:
        return "You cannot add that number"
    
  def gameOver(self):
    #goes through every row
    for i in range(self.dim):
      for n in range(self.dim):
        if self.problem[i][n] == '':
          return False
    return True

'''
while probOne.gameOver() == False:
  probOne.printBoard()
  #probOne.printPerm()
  choice = probOne.prompt()
  while choice < 1 or choice > 2:
    choice = int(input("Please input a valid number: "))
  if choice == 1:
    probOne.add()
  else:
    probOne.remove()

probOne.printBoard()
print("You win!!")
'''