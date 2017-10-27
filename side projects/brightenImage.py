from PIL import Image

def brighten_Image(pixelList):

	pix_len = len(pixelList)
	for i in range(pix_len): #assigns each part of tuple to a variable
		current_pixel = pixelList[i] #then will brigthen each by 50
		red = current_pixel[0]
		green = current_pixel[1]
		blue = current_pixel[2]
		#this is not the best way, ex : replace  current_pixel
		#with pixList[i][0] ect
		newPixel = (red+50, green+50,  blue+50)
		pixelList[i] = newPixel #replaces current pixel with one 
								#whos R,G,B values are +50
	
	return pixelList

def main():

	myFile = "/home/h702546919/Desktop/jimmy.jpg"
	my_img_obj = Image.open(myFile)
	#my_img_obj.show()

	#grabs each pixel's tuple	
	pixelList = list(my_img_obj.getdata()) 
	
	#sends list of tuples to be brightend, gives back newPic
	newPic = brighten_Image(pixelList)
	#pushes new brighter pixels
	my_img_obj.putdata(newPic)


	#displays new pic and old one 
	#(learn how to make a canvas and print side by side ? )
	my_img_obj.show()	
	
	return

#---#
main()
