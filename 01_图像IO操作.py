import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
img = cv.imread('image/linboli.png', 0)  # 0表示灰度图，1表示彩色图

# 显示图像
# 1. cv
# cv.imshow('linboli', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# 2. plt
plt.imshow(img, cmap = 'gray')
plt.show()

# 保存图像
cv.imwrite('image/linboli_copy.jdp', img)