import json
import numpy as np
from PIL import Image
import os


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


def crop(box):
	image_path = box[0]
	xmin = box[1][0]
	xmax = box[1][1]
	ymin = box[1][2]	
	ymax = box[1][3]

	image = Image.open(image_path)
	cropped_image = im.crop((xmin,ymin,xmax,ymax))
	cropped_image.save("output/")



class Cropper:
	def __init__(self, output_path):
		self.output_path = output_path
		
	def 	