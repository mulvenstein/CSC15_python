#file : mulvey-t-4-2
#purpose : considers if n and N+@ are prine
# author :tom mulvey
#date : 10/3
#vers .0.1
def is_prime(N):
	''''isprime is true
		when n and n+2
		are prime'''
	d=2
	while d<N and N%d != 0 :
		d += 1
	
	if d == N :
		return True
	else:
		return False

def main():
	numInput = int(input("Etner the first num : "))
	num2 = numInput + 2
	
	if( is_prime(numInput) and is_prime(num2)):
		print(numInput, "and", num2, "are prime twins")
	else :
		print(numInput, "and", num2, "are not twins")
	return
#---#
main()



