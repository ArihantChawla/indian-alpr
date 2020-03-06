import json
import numpy as np
from PIL import Image
import os

def listJson(output_path):
	jsonlist = []
	for file in os.listdir(output_path):
		if file.endswith(".json"):
			jsonlist.append(str(output_path) + "/" + str(file))
	return jsonlist		

def openJson(json_path):
	with open(json_path, 'r') as f:
		data = json.read(f)

	return data

def extractBox(data):
	xmin = data[0]['y_min']
	xmax = data[0]['x_max']
	ymin = data[0]['y_min']
	ymax = data[0]['y_max']
	image_path = data[0]['path']
	return [path, [xmin, xmax, ymin, ymax]]

enum = 0

def crop(box,filepath):
	image_path = box[0]
	xmin = box[1][0]
	xmax = box[1][1]
	ymin = box[1][2]	
	ymax = box[1][3]

	image = Image.open(image_path)
	extension = str(image_path.split('.')[-1])
	cropped_image = im.crop((xmin,ymin,xmax,ymax))
	cropped_image.save("output/" + str(enum) + "." + extension)




class Cropper:
	def __init__(self, output_path):
		self.output_path = output_path
		
	def placeholder(self):
		list = listJson(self.output_path)
		for file in list:
			fileData = openJson(file)
			fileBox = extractBox(filedata)

