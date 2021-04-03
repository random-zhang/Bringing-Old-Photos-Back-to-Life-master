import numpy as np
from PIL import Image
import  cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import cv2 as cv
def v():
        img_url="face.png"
        pil_img = Image.open(img_url).convert("RGB")#原生为4通道
        image = np.array(pil_img)

        print(image)
        print(1)
# src = cv.imread("face.png")
# cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
# cv.imshow("input", src)
# dst = cv.applyColorMap(src, cv.COLORMAP_COOL)
# cv.imshow("output", dst)
img = cv.imread('0001.jpg',0)
#用numpy生成卷积核
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)

cv.imshow('erosion',erosion)
cv.waitKey(0)
cv.destroyAllWindows()