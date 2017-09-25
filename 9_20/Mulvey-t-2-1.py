#File: mulvey-t-2.1.py

#purpose---------
#Word game, a user buys vowels and consonants
#First vowel is free, each additional is $1
#First two cons. are free, each additional are $2 each

#Author : TOm Mulvey
#date: 9/20, version 0.0.1

def main():
	print("Welcome to the Word Game")
	
	#--declarations--
	playerMoney = 0
	vowelsWanted = 0
	consWanted = 0
	moneyCheck = 0 #theoretical money needed to allow word
	
	#--assignments--
	playerMoney = float(input("How much moola you got? $"))
	vowelsWanted = int(input("How many vowels do you want? : "))
	consWanted = int(input("How many consonants bro? : "))
	
	#--operations--
	
	if(vowelsWanted < 0 or consWanted < 0) :
		print("invalid input :( ")	#checks for valid input
	else :
		if vowelsWanted > 1 :
			if consWanted > 2 :
				moneyCheck = ((vowelsWanted-1) + (consWanted-2)*2) #1$ for every extra vowel and 2 for every extra cons > 2
			else :
				moneyCheck = (vowelsWanted-1) #1 or 0 cons are free!
		else :
			if consWanted > 2 :
				moneyCheck = (consWanted-2)*2 #only pay for cons
			else :
				moneyCheck = 0; #free !!!!
				
	#--- final check ---#
	if(moneyCheck == playerMoney or moneyCheck < playerMoney) : #can change if moneyCheck >= ,  dont know why i did this
		print("\nAllowed")
	else :
		print("\nInsufficient Funds")
		
	return

#--#
main()