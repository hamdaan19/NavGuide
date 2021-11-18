import os
import torch
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from torchvision import transforms

class NVDataset():
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.X_dir = root_dir+'/true_images/'
        self.Y_dir = root_dir+'/labelled_images/'
        self.images = os.listdir(self.X_dir)
        self.labels = os.listdir(self.Y_dir)

    def __len__(self):
        return len(self.images)

    def __getitem__(self, index):
        X = Image.open(self.X_dir+self.images[index])
        # plt.imshow(X)
        # plt.show()
        X = transforms.ToTensor()(X)
        # X = np.array(X)
        # X = torch.from_numpy(X).view(3, 420, 420)
        #X = X.type(torch.FloatTensor)

        Y = Image.open(self.Y_dir+self.labels[index])
        Y = np.array(Y)
        Y = torch.from_numpy(Y)
        Y = Y.type(torch.LongTensor)

        return X, Y

def get_nv_data(root_dir, batch_size=1, transforms=None):
    data = NVDataset(root_dir=root_dir)
    dataset = torch.utils.data.DataLoader(data, batch_size=batch_size, shuffle=True)
    return dataset



sample = get_nv_data(r'E:\Dev\DnF\NavGuide\datasets\NV_dataset')
for i in sample:
    X, y = i
    print(X.type(), y.type())
    break