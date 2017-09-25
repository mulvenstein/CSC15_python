#File: mulvey-1.1.py
#Purpose: User inputs the fixed $ per year he recieves, and in return the program prints
#		  the value using the given formula 
#		  PV = (amount per year) / ((1 + rate) ** N) where n = years
#Author: Thomas Mulvey
#Date: 9/12/2017
#Version: 1.01

def main():
	
	cashPerYear = float(input("What is the fixed $ value per year you will recieve? >> " )) #
	interestRate = float(input("What is the current interest rate ? >> "))
	
	print('\n')
	
	total = 0
	
	for years in range(5) : #years = years 1-5 or winnings
		moneyTotal = (cashPerYear)/((1 + interestRate) ** (years + 1)) #years +1 is so it starts at 1 and not 0
		print("year ", years+1, " $", moneyTotal, '\n')
		total = total + moneyTotal #
	print("total money earned : $", "{0:.2f}".format(total))
	return
#--#
main()