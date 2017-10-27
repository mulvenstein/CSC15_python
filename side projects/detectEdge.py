#edge detection challeng
#date 10/24
#author tom mulveyero 

from PIL import Image, ImageColor

#import PIL.Image

def getBrightness(myImage, x, y):

	pixelRGB = myImage.getpixel((x,y))
	R, G, B = pixelRGB
	brightness = sum([R,G,B])/3

	return brightness

def main():
	
	print("edge detection program!")
	#loads the image into a grid!	
	myImage = Image.open(input("Image name? ")) #should ask for img
	myGrid = myImage.load()
	
	newImage = Image.new("RGB", myImage.size,(50,50,50))
	#newImage.show()
	#newGrid = newImage.load()
	
	for x in range(myImage.height-1) : #change this to height of imge
		for y in range(myImage.width-1) : #change to width of img
			pixBright = getBrightness(myImage, y, x) #check if it is off the grid.
			if((getBrightness(myImage, y+1, x) - pixBright >= 10 ) and ( getBrightness(myImage, y, x+1) - pixBright >= 10 )):
				newImage.putpixel((y,x), ImageColor.getcolor('white' , '1'))
			else :
				newImage.putpixel((y,x), ImageColor.getcolor('black' , '1'))
	
	
	newImage.show()

	return

#--#
main()
