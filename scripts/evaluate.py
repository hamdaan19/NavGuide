import torch
import matplotlib.pyplot as plt
from utils import *
import model
from torchvision import transforms
import matplotlib.pyplot as plt

ROOT_DIR = r'E:\Dev\DnF\NavGuide\datasets/NV_dataset'
MODEL_PATH = 'NV_model.pth.tar'
PLOT_LOSSES = False
EVAL = True
SAVE_IMG = True

if torch.cuda.is_available():
    DEVICE = 'cuda:0'
    print('Running on the GPU.')
else:
    DEVICE = 'cpu'
    print('Running on the CPU.')

def compute_accuracy(model, data):
    model.eval()
    for batch in data:
        X, Y = batch 
        X, Y = X.to(DEVICE), Y.to(DEVICE)

        pred = model(X)
        pred = torch.nn.functional.softmax(pred, dim=1)
        pred_labels = torch.argmax(pred, dim=1) 
        print(pred_labels.shape)

        if SAVE_IMG == True:
            pred_img = transforms.ToPILImage()(pred_labels.view(420, 420).byte())
            X = transforms.ToPILImage()(X.view(3, 420, 420).byte())
            plt.imshow(pred_img)
            plt.show()
            break


def eval():
    dataset = get_nv_data(ROOT_DIR)

    net = model.UNET(in_channels=3, classes=3).to(DEVICE)
    checkpoint = torch.load(MODEL_PATH)
    net.load_state_dict(checkpoint['model_state_dict'])
    print(f'{MODEL_PATH} has been loaded and initialized')
    compute_accuracy(net, dataset)

def plot_losses(path):
    checkpoint = torch.load(path)
    losses = checkpoint['loss_values']
    epoch = checkpoint['epoch']
    epoch_list = list(range(epoch)) # epoch instead of 10

    plt.plot(epoch_list, losses)
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title(f"Loss over {epoch} epoch/s")
    plt.show()

if __name__ == '__main__':
    if PLOT_LOSSES == True:
        plot_losses(MODEL_PATH)

    if EVAL == True:
        eval()