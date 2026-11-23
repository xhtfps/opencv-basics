import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 图像基础处理
img = np.zeros((256, 256, 3), np.uint8)
plt.imshow(img[:, :, ::-1])
# cv.imshow('image', img)

# print(f'{img[100, 100]}')
# print(f'img.shape:{img.shape}, img.dtype{img.dtype}, img.size:{img.size}')

# 读取图像
img = cv.imread('image/linboli.png', 1)  # 0表示灰度图，1表示彩色图
# plt.imshow(img[:, :, ::-1])
# plt.show()

# 图像分割
# b,g,r = cv.split(img)
# plt.imshow(b, cmap='gray')
# plt.show()

# 图像合并
# img2 = cv.merge((b,g,r))
# plt.imshow(img2[:, :, ::-1])
# plt.show()

# 图像颜色空间转换
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray')
plt.show()

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
plt.imshow(hsv[:, :, ::-1])
plt.show()