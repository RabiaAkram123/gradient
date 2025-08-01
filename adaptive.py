import cv2
import numpy as np

img=cv2.imread("sudoko.png",0)

_,th1=cv2.threshold(img,150,255,cv2.THRESH_BINARY) # Simple binary thresholding
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2) # Adaptive thresholding using mean
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2) # Adaptive thresholding using Gaussian mean

cv2.imshow("image",img)
#cv2.imshow("th1",th1)
cv2.imshow("th2",th2)
cv2.imshow("th3",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
