import numpy as np
import cv2
from matplotlib import pyplot as plt

num_disparities = 48
block_size = 15

# Save out put as video
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('bm_disp.avi', fourcc, 8, (1348, 374))

for i in range(0, 602):
    img_address_1 = 'datasets/2010_03_04_drive_0032/2010_03_04_drive_0032_Images/I1_'+str(i).zfill(6)+'.png'
    img_address_2 = 'datasets/2010_03_04_drive_0032/2010_03_04_drive_0032_Images/I2_'+str(i).zfill(6)+'.png'

    imgL = cv2.imread(img_address_1, cv2.IMREAD_GRAYSCALE)
    imgR = cv2.imread(img_address_2, cv2.IMREAD_GRAYSCALE)

    stereo = cv2.StereoBM_create(numDisparities=num_disparities, blockSize=block_size)
    disparity = stereo.compute(imgL,imgR).astype(float)/16
    disparity = cv2.normalize(disparity, disparity, alpha=255, beta=0, norm_type=cv2.NORM_MINMAX)
    disparity = np.uint8(disparity)

    cv2.putText(disparity, str(i), (30,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    cv2.imshow('Disparity Image BM', disparity)

    #frame = cv2.cvtColor(disparity, cv2.COLOR_GRAY2BGR)
    #out.write(frame)

    k = cv2.waitKey(15) & 0xFF
    if k == 27:
        break

#out.release()
cv2.destroyAllWindows()