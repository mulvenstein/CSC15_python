#Interactive program to analyze a document
#Author: Thomas Mulvey
#Date : 10/24
#mulvey-t-6-1.py

def analyze(filename):
	'''takes a file name.
		opens that file name, puts all the lines into a list of strings
		after that, analyzes each word and genereates a map.'''
	
	docMap = {}
	docList = []
	sentanceList = [] #list for each line, splits word
	lineCounter = 1
	
	myFile = open(filename)
	
	for line in myFile:
		docList.append(line)
		#split line into words
		sentanceList = line.split()
		for word in sentanceList :
			if word in docMap :
				#just add a counter.
				docMap[word].append(lineCounter)
			else : #word isnt in the docmap, so add it into there
				#print(word)
				docMap.update({word : [lineCounter]})
		lineCounter += 1
	#print(docMap)
	return docMap, docList

def find(docMap, word):
	
	if word in docMap:
		print(word + " is in the document on the following lines.\n", docMap[word])
	else: #not in docMap
		print(word + " is not in the document.")
		
	return

def context(docMap, docList, word):
	
	if word in docMap:
		for lines in docMap[word] :
			print(lines, ": ", docList[lines])
	else: #not in docMap
		print(word + " is not in the document. Please try again ;)")
		
	return
	
def main():

	print("Document analysis program")
	print("*************************")
	print()
	action = input("Ready> ")
	while action != "quit":
		if action == "analyze":
			filename = input("Name of file to analyze? ")
			docMap, docList = analyze(filename)
            
		elif action == "find":
			word = input("Word to find in document? ")
			find(docMap, word)

		elif action == "context":
			word = input("Context for which word? ")
			context(docMap, docList, word)

		else:
			print("I don't understand that choice.")

		action = input("Ready>> ")

	print("Bye!")
	return

#---#
main()
