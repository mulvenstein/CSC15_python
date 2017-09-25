#File: mulvey-t-2.2.py

#purpose---------
#User enters a word, program calculates the plural version of it

#Author : TOm Mulvey
#date: 9/20, version 0.0.1

def main():
	print("Welcome to the extreme plurifier program\n")
	
	#--declarations--
	wordWanted = "\0"
	
	#--assignments--
	wordWanted = input("What word would you like to plurify? : ")
	
	#--checks-- program assumes they end with lowerase letter
	if (wordWanted.endswith("s") or wordWanted.endswith("sh") or wordWanted.endswith("x") or wordWanted.endswith("ch") or wordWanted.endswith("z") ) :
		wordWanted = wordWanted + 'es' 
		print(wordWanted)
	elif (wordWanted.endswith("ay") or wordWanted.endswith("ey") or wordWanted.endswith("iy") or wordWanted.endswith("oy") or wordWanted.endswith("uy") ) :
		wordWanted = wordWanted + 's'
		print(wordWanted)
	elif wordWanted.endswith("y") :
		wordWanted = wordWanted[:len(wordWanted)-1] + "ies"
		print(wordWanted)
	elif (wordWanted.endswith("ao") or wordWanted.endswith("eo") or wordWanted.endswith("io") or wordWanted.endswith("oo") or wordWanted.endswith("u") ) :
		wordWanted = wordWanted + 's'
		print(wordWanted)
	elif wordWanted.endswith("o") : 
		wordWanted = wordWanted + 'es' 
		print(wordWanted)
	elif wordWanted.endswith("fe") :
		wordWanted = wordWanted[:len(wordWanted)-2] + "ves"
		print(wordWanted)
	elif wordWanted.endswith("f") :
		wordWanted = wordWanted[:len(wordWanted)-1] + "ves"
		print(wordWanted)
	else :
		wordWanted = wordWanted + 's'
	
	#should really combine some of the casses woops
	
	return

#--#
main()

#wordWanted = wordWanted[:len(wordWanted)] + "es"