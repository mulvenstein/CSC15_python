#mulvey-t-11-1.py Tic-Tac-Toe [Desktop]
#author: tom mulvey
#date : 11/28
#vers 0.0.1
#purpose : create a tic tac toe game vs computer,
#          and make a semi smart AI

'''there is some really janky code, especially with the computer "ai" 
   I made it so the computer was beatable, I could add forking to make it impossible
   or change prioty of mid control. 
   
   Classes were kind of useless, but if i wanted to expand to human vs human they wouuld be useful. 
   Since it is only one instance of human vs comp every time they are not utilized well, but it was good practice
   with classes beause we have not had a dedicated lab for it yet. 
   
   TODO: Rename variables, clean up the spilt spaghetti code, never look at computer moves again...'''


from random import *

class ttt_board(): #let's make some OOP :D

   def __init__(self) : 
      self.board = {1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:'', 9:''}
      self.row_list = [ [1,2,3], [4,5,6], [7,8,9] ]
      self.col_list = [ [1,4,7], [2,5,8], [3,6,9] ]
      self.slant_list = [ [1,5,9], [3,5,7] ]
      #the row, col, and slant list are used when checking if someone has won. Will only check the 3 spots in the specif row col or slant
      self.row_list_iterator = 0
      self.col_list_iterator = 0
   
   def reset(self): #resets game.
      self.board = {1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:'', 9:''}
   
   def check_spot(self, position) : #checks to see if desired spot is available.
      if self.board[position] != '' :
         return True
   
   def is_board_full(self) : 
      empty = ''
      return not any(spot == empty for spot in self.board.values()) #if +1 spot is not empty, returns false, otherwise true

   def checK_game_over(self, position): #check slanted victroies always.
       #first find the row and col position is in
      self.row_list_iterator = 0
      self.col_list_iterator = 0
      while True : #find row.
         if position in self.row_list[self.row_list_iterator]:
            break
         else:
            self.row_list_iterator += 1

      while True : #find col.
         if position in self.col_list[self.col_list_iterator]:
            break
         else:
            self.col_list_iterator += 1
   
      #the iterators for row and col are the col and row the num is in. If pos
      #is 4 or 6 do not check the slants. else see if the values of the keys
      #in the row and col ar all the same and make sure they are all not empty.
      #if they are all 'c' the comp wins. if all 'h' then human wins!
      
      rl = self.row_list[self.row_list_iterator]
      cl = self.col_list[self.col_list_iterator]
      sl1 = self.slant_list[0]
      sl2 = self.slant_list[1]
      
      if (self.board[rl[0]] == self.board[rl[1]] == self.board[rl[2]]) and self.board[rl[0]] != '': #all chars in row are same and not empty
         #if all board[i] for i in rowlist[iter] == board[pos]
         if self.board[rl[0]] == 'c' :
            return "computer"
         else :
            return "human"
      elif (self.board[cl[0]] == self.board[cl[1]] == self.board[cl[2]]) and self.board[cl[0]] != '': #all chars in col are same + not empty
         if self.board[cl[0]] == 'c' :
            return "computer"
         else :
            return "human"
      elif (self.board[sl1[0]] == self.board[sl1[1]] == self.board[sl1[2]]) and self.board[sl1[0]] != '':  #checks first slant
         if self.board[sl1[0]] == 'c' :
            return "computer"
         else :
            return "human"
      elif (self.board[sl2[0]] == self.board[sl2[1]] == self.board[sl2[2]]) and self.board[sl2[0]] != '': #checks second slant
         if self.board[sl2[0]] == 'c' :
            return "computer"
         else :
            return "human"
      else : #no one has wonnnered
         return "continue"
         #THIS IS SOME REAL SPAGHETTI CODE> SHOULD FIND BETTER WAY TO CHECK!!!!!!!!
   def print_board(self):
      print("\nGame Board :")
      print("|", end='')
      for i in range(1,4) :
         if self.board[i] == '':
            print(" ", i, "|", end='')
         else:
            print(" ", self.board[i],   "|", end='')
      print("\n---------------")

      print("|", end='')
      for i in range(4,7) :
         if self.board[i] == '':
            print(" ", i, "|", end='')
         else:
            print(" ", self.board[i], "|", end='')
      print("\n----------------")

      print("|", end='')
      for i in range(7,10) :
         if self.board[i] == '':
            print(" ", i, "|", end='')
         else:
            print(" ", self.board[i], "|", end='')
      print("\n")
      return

#-----class is done, add to anothe file then import???--------#

#now that i think of it my classes have no actual use....
#it is too late so I am going to contiue anyways....
#woops...

def cls():
   print("\n" * 100) #lol this is high level programming
   return

def human_turn(game_on):
   position = int(input("Hello Human. Would Spot would you like ? : "))
   while game_on.check_spot(position) == True or (position < 0 or position > 10): #runs if the spot is occupied
      position = int(input("Try another spot, human. : "))
   game_on.board[position] = 'h'
   return position

def computer_turn(board):
   # position = randint(1,9)
   # while game_on.check_spot(position) == True :
   #    position = randint(1,9)
   # game_on.board[position] = 'c'
   # return position
   # used to test if game worked ^

   # win if u have 2 in a row
   # bock if opponent hsa 2 in a row
   # fork - create an oprotunity where u can win in 2 way
   # block opponent fork
   #  opt 1 : create 2 in a row to force opp into defending
   #  opt 2 : if ther is a config where human can fork, block it
   # center 
   # if op is in op corner, take that corner
   # play empty corner
   # play empty side
   #alter these priorities to change difficulty level??
   
   def can_win(board, sign, i):
      test = ttt_board()
      for x in board :
         if x in test.board :
            test.board[x] = board[x]
      test.board[i] = sign
      return test.checK_game_over(i)
   #coomp win ?
   for  i in [1,2,3,4,5,6,7,8,9]:
      if board[i] == '':
         call = can_win(board, 'c', i)
         if call == "computer":
            return i
   #player win
   for  i in [1,2,3,4,5,6,7,8,9]:
      if board[i] == '':
         call = can_win(board, 'h', i)
         print(board, call)
         if call == "human":
            return i
   #take corner
   for i in [1,3,7,9]:
      if board[i] == '' :
         return i
   #center
   if board[5] == '' :
      return 5
   
   #side play
   for i in [2,4,6,8]:
      if board[i] == '' :
         return i
   
   #need to add fork, brute force ? prob best. research minimax more

def driver(): #driver function
   print("welcome to tic tac toe\n")
   game_on = ttt_board() 

   while True : #run turn base fun
      #show screen -> human plays -> check spot, game status -> cls -> computer goes -> check spot/game status -> cls
      game_on.print_board()
      position = human_turn(game_on)
      status = game_on.checK_game_over(position)
      if status != "continue" :
         break
      cont = game_on.is_board_full()
      if cont:
         status =" tie "
         break
      cls()
      bored = game_on.board
      position = computer_turn(bored)
      game_on.board[position] = 'c'
      status = game_on.checK_game_over(position)
      if status != "continue" :
         break
      cont = game_on.is_board_full()
      if cont:
         status =" tie "
         break
      cls()

   cls()
   game_on.print_board()
   if status == "human" :
      print("human wonnered")
   elif status == " tie ":
      print("tis a tie")
   else :
      print("computer wonnered")

   return
#-----#
driver()
