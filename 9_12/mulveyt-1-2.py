#File: mulvey-1.1.py
#Purpose: User inputs how many Bitcoin blocks they have mined, and their electricity usage, and the program
#		  computes how much profit is made per month
#Author: Thomas Mulvey
#Date: 9/12/2017
#Version: 1.01

def main():
	print("Welcome to the Bitcoin Mining Proit Program")
	print('\n')
	
	#--variables
	
	# blocksMined the number of blocks you have mined
	#khwUsed  #electricity used for the month
	#profit  #profit calculated
	bool = False 
	#--declarations--
	
	#while True:
	#	blocksMined = int(input("How many blocks have you mined this month? >>" )
	#	if blocksMined > 0:
	#		break
	#	else:	
	#		print("try again bud")
		#todo, invalid syntax in if statement
		
		
	blocksMined = int(input("How many blocks have you mined this month? >> " ))
	khwUsed = float(input("How much electricity have you consumed this month? >> "))
	
	#--calculations
	
	profit = (blocksMined * 52900) - (.12 * khwUsed) - 100
	
	print("Profit : $",profit)
	return
#---#
main()