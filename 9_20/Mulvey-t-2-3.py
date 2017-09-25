#File: mulvey-t-2.2.py

#purpose---------
#User enters 3 numbers, program returns the median value

#Author : TOm Mulvey
#date: 9/20, version 0.0.1

def main():
	print("Welcome to the median finder program!\n")
	
	num = [0,0,0]
	
	for x in range(3) :
		num[x] = float(input("Enter num (can have decimals): "))
		print("\n")
	

	if num[0] < num[1] or num[0]==num[1]:
		if num[1] < num[2] or num[1] == num[2] :#123
			print(num[1])
		elif num[1] > num[2] and num[2] > num[0] :#132
			print(num[2])
		else :
			print(num[0]) #231
	elif num[1] < num[0] :
		if num[1] < num[2] and num[0] < num[2] : #213
			print(num[0])
		elif num[0] > num[2] and num[1] > num[2] : #23
			print(num[1])
		else :
			print(num[2])
	return

#--#
main()

