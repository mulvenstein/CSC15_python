#file : mulvey-t-4-4
#purpose : generates private key for python
# author :tom mulvey
#date : 10/3
#vers .0.1

import os

def genPrivate():
	N = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 2**3 - 1
	P = 0
	for x in range(0, 255+1):
		P += (ord(os.urandom(1))%2)*(2**x)
	ans = (P %(N-1)) + 1
	return ans

def main():
	keyGen = genPrivate()
	print("Key generated : ", keyGen)
	return
#---#
main()




