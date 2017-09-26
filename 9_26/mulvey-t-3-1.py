# File: mulvey-t-3-1
# Purpose : Calculates the total number of bitcoins a miner earn 
# if they got 1,2,4, etc blocks per month
#
# Author : Tom Mulvey
#
# Date: 9/26/17
# Version : 0.0.1

def main():
	print("Bitcoin Miner Program")
	
	numOfMonths = int(input("How many months did you mine bitcoins ? "))
	totalBlocks = 0 # sum of blocks per month
	blockPerMonth = 0 # num oif blocks per month, 2^x	

	print("Month   Earn   Total")
	for x in range (1, numOfMonths+1):
		# print("test", x) used to see if loop was executed properly
		blockPerMonth = 2**(x-1)
		totalBlocks += blockPerMonth
		print(x, "\t", blockPerMonth, "\t", totalBlocks)
	
	 #need to switch x to an appropiate var name, and find out how to use setW
	return
#---#
main()
