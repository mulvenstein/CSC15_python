from PIL import Image

def hide_num(pixel, X): #adds the insig num to the pixel's tuple
		ch = str(X)
		p0 = str(pixel[0])
		p1 = str(pixel[1])
		p2 = str(pixel[2])
		
		if X >= 100 :
			Red = int( p0[0:len(p0)-1] + ch[0] )
			Green = int( p1[0:len(p1)-1] + ch[1] )
			Blue = int( p2[0:len(p2)-1] + ch[2] )
		else :
			Red = int( p0[0:len(p0)-1] + "0" )
			Green = int( p1[0:len(p1)-1] + ch[0] )
			Blue = int( p2[0:len(p2)-1] + ch[1] )
		pixel = (Red, Green, Blue)
		return pixel

def hide_char(C): #converts char ascii to hex #
	return ord(C)
	
def encode(original_pic, message):
	N = len(message)
	pixelList = list( original_pic.getdata() ) #puts tuples in a list
	newPixel = ()
	for i in range(0, N) : 
		char = hide_char(message[i])
		print(char)
		newPixel = hide_num(pixelList[i], char)
		pixelList[i] = newPixel 
	
	
	original_pic.putdata(pixelList)
	return original_pic

###Your functions should be written above this line
###Don't modify any of the code below
def main():
	
	thepic = Image.open(input("Image file name: "))
	message = input("Message to hide? ")
	newpic = encode(thepic, message)
	newpic.save("encoded.png")
	print("N =", len(message))
	print("Saved in encoded.png")
	return

###
main()
