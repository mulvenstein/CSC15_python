#mulvey-t-11-1.py Tic-Tac-Toe [Desktop]
#author: tom mulvey
#date : 11/28
#vers 0.0.1
#purpose : create a tic tac toe game vs computer,
#manipulate lists, continuously print/update,

#steps : human plays -> check win -> computer plays
# update between steps.
from random import *
import numpy as np
#a = [[1,4], [2,6], [3,9]]
#print(np.matrix(a)) it works.

def cls(): #this is realllly eh
   print("\n" * 100)
   return

def initialize_board(board) :
   #inits the board for use. empty board
   board = [['','',''],['','',''],['','','']]
   return board

def display(board):
   #displays current status of board, ran after every move
   #numpy print?
   #print("\n\n\n\n\n\n\n\n\n\n\n")
   print(" | (1,1) | (1,2) | (1,3) |\n",\
         "| (2,1) | (2,2) | (2,3) |\n",\
         "| (3,1) | (3,2) | (3,3) |\n",)

   print(np.matrix(board))
   return

def human_move(board):
   #human's turn to place his mark.
   #display grid after.
   print("Humans Turn>> Grid Location? ")
   row = int(input("row? : "))
   col = int(input("col? : "))
   check = check_grid(row, col, board)

   while check == 0:
      cls()
      display(board)
      print("invalid input. Try again.")
      row = int(input("row? : "))
      col = int(input("col? : "))
      check = check_grid(row, col, board)

   board[row-1][col-1] = 'X'
   ans, char = check_game(row, col, board, 'X')

   return board, ans, char

def computer_move(board):
   #computer's turn
   #MI..?
   print("comps move.")
   row = randint(0,3)
   col = randint(0,3)
   check = check_grid(row, col, board)
   while check == 0 :
      row = randint(0,3)
      col = randint(0,3)
      check = check_grid(row, col, board)
   board[row-1][col-1] = 'O'
   ans, char = check_game(row, col, board, 'O')
   return board, ans, char

def check_game(row, col, board, char):
   #comp win, human win, tie?
   #check all horizantals on row
   #check all verts on col
   #always check slanteds
   ans = "maybe"
   #slanteds
   if board[0][0]== char and board[1][1] == char and board[2][2] == char : #someone wons!
      return "yes", char
   elif board[0][2] == char and board[1][1] == char and board[2][0] == char : #someone wons!
      return "yes", char
   else :
       ans = "no"

   #horizontals
   if board[row-1][0] == char and board[row-1][1] == char and board[row-1][2] == char :#hoiz win
      return "yes", char
   else :
      ans = "no"

   #vertz
   if board[0][col-1] == char and board[1][col-1] == char and board[2][col-1] == char : #wons!
      return "yes", char
   else :
      ans = "no"

   return ans, char

def check_grid(row, col, board):
   #checks spot + grid if valid
   check = 2
   if 0 < row < 4 and 0 < col < 4 :
      if board[row-1][col-1] == '' :
         check = 1
      else :
         check = 0
   else :
      check = 0

   return check

def main():
   #driver function.
   board = list()
   board = initialize_board(board)
   #print(np.matrix(board))
   print("Tic Tac Toe!\n")
   while True :
      #display, human, check_valid, check_game, display, comp, check_valid, check_game
      display(board)
      board, ans, char = human_move(board)
      if ans == "yes" :
         print(char, " has won my dude!")
         break
      cls()
      display(board)

      board, ans, char = computer_move(board)
      if ans == "yes" :
         print(char, " has won my dude!")
         break
      cls()

   print("final board : \n")
   display(board)
   return

#----#
main()
