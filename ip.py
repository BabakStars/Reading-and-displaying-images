
import numpy as np
import cv2 as cv
img1 = cv.imread('Your path',0)
img2 = cv.imread('Your path',1)
img3 = cv.imread('Your path',-1)

#cv.IMREAD_COLOR                1
#cv.IMREAD_GRAYSCALE            0
#cv.IMREAD_IGNORE_ORIENTATION   -1

cv.imshow('IM1',img1)
cv.imshow('IM2',img2)
cv.imshow('IM3',img3)
cv.waitKey(0)
cv.destroyAllWindows()
