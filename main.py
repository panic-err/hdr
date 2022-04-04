#!~/bin/python

import cv2 as cv
import numpy as np

#load exposures into a list

dirname = "~/Code/hdr/photometry"

img_fn = ["StLouisArchMultExpEV+1.51.JPG", "StLouisArchMultExpEV+4.09.JPG", "StLouisArchMultExpEV-1.82.JPG", "StLouisArchMultExpEV-4.72.JPG"]

print(img_fn)
for i in img_fn:
    print(dirname+"/"+i)
