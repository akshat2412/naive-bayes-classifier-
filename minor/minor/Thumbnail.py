from wand.image import Image  
from wand.display import display  
from wand.color import Color

def createAndStoreThumbnail(**kwargs):

	# fileDirectory = "/home/akshat/Desktop/"  
	# inFileName="test_doc_2.pdf"  
	# outFileName="myOutputfile.jpg"  
	imageFromPdf = Image(filename=kwargs["fileLocation"]+kwargs["fileName"])  
	# pages = len(imageFromPdf.sequence)  
	# print(pages)  

	# creates an empty Image.
	image = Image(  
	width=imageFromPdf.width,  
	height=imageFromPdf.height  
	)  

	# resize the empty image
	image.sample(470,330)

	#superimpose on the empty image the argument given, at the position specified
	image.composite(
		imageFromPdf.sequence[0], top=0, left=0
	)
	image.background_color = Color("white")
	image.alpha_channel = 'remove'
	# for i in range(pages):  
	# 	image.composite(  
	#  		imageFromPdf.sequence[i],  
	#  		top=imageFromPdf.height * i,  
	#  		left=0  
	# 	)  

	image.format="jpg"  
	image.save(filename=kwargs["imageLocation"]+kwargs["imageName"]+".jpg")
	return kwargs["imageName"]+".jpg" 
	# display(image)  