from PIL import Image
from numpy.lib.npyio import save
from torchvision import transforms
import matplotlib.pyplot as plt
import torch
import numpy as np
from tqdm import tqdm
import os

path = r"E:\Dev\DnF\Transformed dataset\color segmented images/"
save_path = r"E:\Dev\DnF\Transformed dataset\mask_images/"
filename_list = os.listdir(path)
num = 0

for file in tqdm(filename_list):
    img = Image.open(path + file)
    
    # plt.imshow(img)
    # plt.show()

    img = np.array(img)
    new = np.empty([420, 420])

    for i in range(420):
        for j in range(420):
            if(list(img[i][j]) == [255, 255, 255]):
                new[i][j] = 0 # unlabelled
            elif(list(img[i][j]) == [255, 0, 0]):
                new[i][j] = 1 # crosswalk
            elif(list(img[i][j]) == [0, 0, 255]):
                new[i][j] = 2 # sidewalk
            else:
                new[i][j] = 255 # ignore

    new = torch.from_numpy(new)
    new_img = transforms.ToPILImage()(new.byte())
    new_img.save(save_path + f'labelled_{str(num).zfill(2)}.png')
    num += 1
