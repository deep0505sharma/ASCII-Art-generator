#Method 1

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageFont

from PIL import ImageFilter
#opening the image using pillow library
img = Image.open('deepak.jpg')
#inverting the image
img = ImageOps.invert(img)
#here I applied Gaussian blur filter which is a low pass filter hence all high frequency details got segregated
blur_filter = ImageFilter.GaussianBlur(radius=7)
blur_img = img.filter(blur_filter)

#again inverting the image to show the details of the image only
inv_img = ImageOps.invert(blur_img)
#blending the invert image with the real image with 50%  opacity
blend = Image.blend(inv_img, img, 0.5)
blend.save('fileinput.jpg')

import numpy as np
import cv2 as cv


fileOut = 'bar.jpg'
imgPil = Image.open('fileinput.jpg') 
imgCV = np.asarray(imgPil, np.uint8)
hsv = cv.cvtColor(imgCV, cv.COLOR_RGB2HSV)
h,s,v = cv.split(hsv)
ceil = np.percentile(v,8) # 92% of pixels will be white
floor = np.percentile(v,92) # 8% of pixels will be black
a = 255/(ceil-floor)
b = floor*255/(floor-ceil)
v = np.maximum(0,np.minimum(255,v*a+b)).astype(np.uint8)
hsv = cv.merge((h,s,v))
rgb = cv.cvtColor(hsv, cv.COLOR_HSV2RGB)
gray = cv.cvtColor(rgb, cv.COLOR_RGB2GRAY)
imgPil = Image.fromarray(gray)
imgPil.save(fileOut)



#Method 2
import cv2
img = cv2.imread("deepak.jpg")
grey_filter = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_filter)
blur =  cv2.GaussianBlur(invert, (41,41), 0)
invertedblur = cv2.bitwise_not(blur)

sketch_filter = cv2.divide(grey_filter,invertedblur, scale = 256.0)
cv2.imwrite("sketchoutput.jpg",sketch_filter)