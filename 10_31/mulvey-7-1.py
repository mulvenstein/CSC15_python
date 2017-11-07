#author : tom mulvey
#date : 10/31
#vers : 0.1
#purpose : given a number N, give min num of coins needed
#to make that number N

coinList = [1,5,6,9]#coins sent to the recursive algorithm.
	            #user can switch them

def rec_mincoins(change, coins, saved):#changeinputed, usable coins, and dict
	minC = change
	if change in coins :
		saved[change] = 1
		return 1
	elif change in saved :
		return saved[change]
	elif change <= 0 :
		return float("inf")
	else :
		for i in [c for c in coins if c<= change ] : #list comprehension :)
			num = 1 + rec_mincoins(change-i, coins, saved)
			if num < minC :
				minC = num
			saved.update({change:minC})
		return minC

a = rec_mincoins(89, coinList, {})
print(a)

