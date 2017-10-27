#magic square
#lab 4 10/30
import time # for sleep function
import os #cls function
import numpy as np #orinting at end
def checkMove (x,y,size) : #should really just send a list of x and y coords
					  #but just using x and y helps me visualize
	if ( x >= 0 ) :
		if ( y <= size-1 ) :
			case = 1 #x and y valid
		else :
			case = 2 #x valid
	else :
		if ( y <= size-1 ) :
			case = 3 #y valid
		else :
			case = 4 #neither valid

	#uses case to determine where to move
	if case == 1 :
		x = x
		y = y
	elif case == 2 :
		x = x
		y = 0
	elif case == 3 :
		x = size-1
		y = y
	else :
		x = size-1
		y = 0
	
	return (x,y)

def is_Filled(x,y,matrix) :
	if matrix[x][y] == None :
		x = x
		y = y 
	else :
		x = x + 1
		y = y
	return (x,y)

def main () :
	print("magic sqaure program\n")
	size = int(input("size o magic square ? : "))

	matrix = [] #declares the 2d arr/ list for magic swaure
	
	for i in range(size): #nested for loop to fill
		matrix.append([]) #matrix with null/none
		for j in range (size): #prorgram will replace None
			matrix[i].append(None) #with appropiate num
	'''
	program should put None in matrix mid point in row 0
	then go through the checks.
		check if space exists first
			ifit does, check if its filled
				if filled, move south
				if not, fill
			if it doesnt exsists
				move either to left col / bot row / both
					then print
	
	should utilize a for loop going from 1->size**2
	in there, check all the conditions.
	'''
	midpoint = size // 2 
	matrix[0][midpoint]=1 #places one in the first row and middle.
	lastPos = [ 0, midpoint ]
	run = 2 #program starts to run at 2 since 1 is predetermined
 
	for run in range(run,(size**2)+1): #for loop going from 2->size**2
		newPos = [ lastPos[0]-1, lastPos[1]+1 ]
		x = newPos[0] # x and y are the coords
		y = newPos[1] # of the possible  new coord
		x,y = checkMove(x,y,size)
		if matrix[x][y] == None : #if spot is not occupied print
			matrix[x][y] = run
			lastPos = [ x,y ]
		else :  #if occupied, move over then print
			if x == size-1 and y == 0 : #condition if number is in top
										#right corner and bot left is filled
				matrix[x-1][y+(size-1)]= run
				lastPos = [ x-1,y+size-1 ]
			else : #prints below if top right spot is occupied.
				matrix[x+size-1][y-1] = run
				lastPos = [ x+size-1,y-1  ]
		
		#print("{:3}".format(val), end=" ", flush=True)
		print(np.matrix(matrix))
		print("\n")
		time.sleep(.2)
		os.system("cls")
		
	return
#---#
main()
