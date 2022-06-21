from flask import request
from PIL import Image
import cv2
import numpy as np

def upload_image():
	file = request.files['file']
	Image.open(file).save('static/images/test.png')

def save_result_img(A,pos,db):
	if db == 'orl':
		if pos == None:
			empty = np.zeros(shape=(112,92))
			cv2.imwrite('static/images/result.png',empty)
		else:
			cv2.imwrite('static/images/result.png',A[:,int(pos)].reshape(112,92))

def get_test_img(db):
	if db == 'orl':
		return np.array(cv2.imread('static/images/test.png',0)).reshape(10304,)