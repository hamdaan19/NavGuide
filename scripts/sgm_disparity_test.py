import numpy as np
import cv2
from matplotlib import pyplot as plt

block_size = 9
min_disparity = 0
max_disparity = 128
num_disparity = max_disparity - min_disparity
uniqueness_ratio = 1
speckle_window_size = 200
speckle_range = 3
disp12_max_diff = 0

#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('axe1.avi', fourcc, 8, (1348, 374))

for i in range(0, 602):
    img_add_1 = 'datasets/2010_03_04_drive_0032/2010_03_04_drive_0032_Images/I1_'+str(i).zfill(6)+'.png'
    img_add_2 = 'datasets/2010_03_04_drive_0032/2010_03_04_drive_0032_Images/I2_'+str(i).zfill(6)+'.png'

    imgL = cv2.imread(img_add_1, 0)
    imgR = cv2.imread(img_add_2, 0)

    stereo = cv2.StereoSGBM_create(
        minDisparity=min_disparity,
        numDisparities=num_disparity,
        blockSize=block_size,
        uniquenessRatio=uniqueness_ratio,
        speckleWindowSize=speckle_window_size,
        speckleRange=speckle_range,
        disp12MaxDiff=disp12_max_diff,
        P1=16 * 1 * block_size * block_size,
        P2=64 * 1 * block_size * block_size,
    )

    disparity_SGBM = stereo.compute(imgL, imgR)
    disparity_SGBM = cv2.normalize(disparity_SGBM, disparity_SGBM, alpha=255, beta=0, norm_type=cv2.NORM_MINMAX)
    disparity_SGBM = np.uint8(disparity_SGBM)

    cv2.putText(disparity_SGBM, str(i), (30,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow('Disparity Image', disparity_SGBM)
    #frame = cv2.cvtColor(disparity_SGBM, cv2.COLOR_GRAY2BGR)
    #out.write(frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

print(type(disparity_SGBM))
#out.release()
cv2.destroyAllWindows()