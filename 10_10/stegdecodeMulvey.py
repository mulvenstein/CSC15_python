#Purpose: Decode a steganographically coded image
#Author: Your Name

from PIL import Image

def hidden_num(pixelTuple): #takes pixel as a paramenter and returns 
							#the insignificant ints
	insig_num = 0
	insig_num += pixelTuple[0]%10 * 100
	insig_num += pixelTuple[1]%10 * 10
	insig_num += pixelTuple[2]%10 * 1

	return insig_num

def hidden_char(insig_num): #takes insignum as parameter, converts to asccii equiv.
	return chr(insig_num)

def decode(original_pic, N) : #takes OG pic and #of pixels(N) to 
				#sort through, decodes message in a for loop :D
	pixelList = list( original_pic.getdata() ) #puts tuples in a list
	message = "" #message is a string of all the pixels
	for i in range(0, N) :
		tempNum = hidden_num(pixelList[i])
		message = message + hidden_char(tempNum)
	
	return message


###Your functions should be written above this line
###Don't modify any of the code below

def testfunctions():
    sample = [(241, 90, 147), (111 , 51, 31) ]
    if hidden_num(sample[0]) != 107:
        print("Your 'hidden_num' function has an error.")

    if hidden_char(107) != 'k':
        print("Your 'hidden_char' function has an error.")

    class dummy:
        def getdata(self):
            return [(241, 90, 147), (111 , 51, 31) ]

    if decode(dummy(), 2) != 'ko':
        print("Your 'decode' function has an error.")

    return
    
def main():
    print("\n\nTesting your functions.\n\n")
    testfunctions()
    print("\n\nReady to decode.\n\n")
    imgfile = "pizza.png"
    N = 254 #change N to whatever the length o hidden messsage is
    thepic = Image.open(imgfile)
    print(decode(thepic, N))
    return

###
main()

