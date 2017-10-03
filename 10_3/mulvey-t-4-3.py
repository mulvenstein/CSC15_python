#file : mulvey-t-4-3
#purpose : considers if N is divisble by 3,5 both, or none and
#determines an output based off that
# author :tom mulvey
#date : 10/3
#vers .0.1
def fizzBuzzOrNah(intToTest):
	
	fizzbuzz = ""

	if(intToTest % 3 == 0 and intToTest%5 == 0):
		fizzbuzz = "fizz buzz bro"
	elif(intToTest%3==0 and intToTest%5!=0):
		fizzbuzz = "fizz"
	elif(intToTest%5==0 and intToTest%3!=0):
		fizzbuzz = "buzz"
	else:
		fizzbuzz = intToTest	

	return fizzbuzz


def main():
	numToTest = int(input("From 1 to X, the program will test its divisibility. \n please enter X : " ))
		
	for x in range(1,numToTest +1) :
		value = fizzBuzzOrNah(x)
		print("N=",x,"\treturns ", value)

	return
#---#
main()



