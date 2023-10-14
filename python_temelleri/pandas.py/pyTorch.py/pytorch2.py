import torch
import torchvision.transforms as transforms
import torchvision
import os
import pandas as pd
from torch.utils.data import(Dataset, DataLoader)
from skimage import io

import warnings
warnings.filterwarnings("ignore")


#Veriyi Dahil Etme

class veri(Dataset):
    def __init__(self, csv_file, root_dir, transform = None):
        self.annotations = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, index):
        img_path = os.path.join(self.root_dir, self.annotations.iloc[index, 0])
        image = io.imread(img_path)
        y_label = torch.tensor(int(self.annotations.iloc[index, 1]))

        if self.transform:
            image = self.transform(image)

        return (image, y_label)


dataset = veri(csv_file=r"C:\\Users\\huawei\\OneDrive\\Masaüstü\\f111.csv",
               root_dir=r"C:\\Users\\huawei\\OneDrive\\Masaüstü\\f1_classification",
               transform = torchvision.transforms.Compose([

                transforms.Resize(size=(28,28)),
                transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))
               ]))


#veri ön işleme

train_set, test_set = torch.utils.data.random_split(dataset,[200,79])
train_loader = DataLoader(dataset=train_set,batch_size=1,shuffle = False)

        