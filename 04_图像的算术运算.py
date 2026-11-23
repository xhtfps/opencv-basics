import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 图像的算术运算
img1 = cv.imread('image/linboli.png', 1)
img2 = cv.imread('image/linboli.png', 1)

# 图像相加
img_add = cv.add(img1, img2)
plt.imshow(img_add[:, :, ::-1])
plt.show()

# 图像相减
img_sub = cv.subtract(img1, img2)
plt.imshow(img_sub[:, :, ::-1])
plt.show()

# 图像相乘
img_mul = cv.multiply(img1, img2)
plt.imshow(img_mul[:, :, ::-1])
plt.show()

# 图像相除
img_div = cv.divide(img1, img2)
plt.imshow(img_div[:, :, ::-1])
plt.show()
