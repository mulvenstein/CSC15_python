# File: mulvey-t-3-2
# Purpose : Show a credit card repayment per month given the balance, annual int rate, and monthly repayment amount
#
# Author : Tom Mulvey
#
# Date: 9/26/17
# Version : 0.0.1

def main():
	print("Credit Card Repayment Calculator")
	
	balance = float(input("What is the starting balance ? : "))
	annualRate = float(input("What is the annual rate on the card ? : "))
	monthlyPay = float(input("What is the monthly payment ? : "))	
	
	print("\n Month \t Int. \t Print.  Bal.")
	for monthNum in range(1,12+1):
		#print("test #", monthNum) #tested to see if for loop executed properly.
		intRate = ((annualRate / 100) / 12) * balance #calculates interest rate
		balance = balance - monthlyPay + intRate
		prin = monthlyPay - intRate
		print(monthNum, "\t", round(intRate,2), "\t", round(prin,2), "\t", round(balance,2))
	return
#---#
main()
