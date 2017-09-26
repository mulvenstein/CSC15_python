# File: mulvey-t-3-3
# Purpose : Opposite Bisect sort, find apporx cube oof a number given
#
# Author : Tom Mulvey
#
# Date: 9/26/17
# Version : 0.0.1

def main():
	print("Aprrox Cube Generator")
	
	numEntered = float(input("Enter the number you want to use : "))
	minNum = 1
	maxNum = numEntered
	
	while True:
		midPoint = (minNum + maxNum) / 2
		if abs((midPoint * midPoint * midPoint) - numEntered) < .1 :
			break
		elif abs((midPoint * midPoint * midPoint) > numEntered) :
			maxNum = midPoint
		elif abs((midPoint * midPoint * midPoint) < numEntered) :
			minNum = midPoint 
		else :
			print("is this possible? ")
	print("Cube Root is ~= : ", midPoint)
		
	return
#---#
main()
