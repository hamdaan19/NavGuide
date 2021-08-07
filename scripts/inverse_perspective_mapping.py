import cv2
import numpy as np
from numpy.matrixlib.defmatrix import matrix
import matplotlib.pyplot as plt 

#04
path = r"E:\Dev\DnF\Transformed dataset\dataset images\untransformed_13.jfif"

# img = plt.imread(path)
# plt.imshow(img)
# plt.show()

img = cv2.imread(path , cv2.IMREAD_COLOR)
pt1 = (171, 352)
pt2 = (446, 377)
pt3 = (8, 366)
pt4 = (301, 400)
# cv2.circle(img, pt1, 3, (0, 0, 255), -1) # 1
# cv2.circle(img, pt2, 3, (0, 255, 255), -1) # 2
# cv2.circle(img, pt3, 3, (255, 0, 255), -1) # 3
# cv2.circle(img, pt4, 3, (0, 0, 255), -1) # 4

pts1 = np.float32([pt1, pt2, pt3, pt4])
pts2 = np.float32([[100-20, 200-30], [300-20,200-30], [100-20,300-30], [300-20,300-30]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(img, matrix, (420, 420))

cv2.imshow('transformed', result)
cv2.imwrite('transformed.png', result)


cv2.imshow('frame', img)



cv2.waitKey(0)
cv2.destroyAllWindows()
