import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 创建空白图像
img = np.zeros((512, 512, 3), np.uint8)

# 绘制线段
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# 绘制矩形
cv.rectangle(img, (100, 100), (400, 400), (0, 255, 0), 3)

# 绘制圆形
cv.circle(img, (256, 256), 60, (0, 0, 255), -1)

# 绘制文字
cv.putText(img, 'Hello, OpenCV!', (100, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# 显示图像
cv.imshow('image', img)
cv.waitKey(0)