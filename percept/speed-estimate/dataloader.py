# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-24 00:54:03
# @LastEditTime: 2020-04-24 01:13:51
# @LastEditors: Xiao Shanghua
# @Description: 
# @FilePath: \machinelearning\vision\need-for-auto-speed\percept\speed-estimate\dataloader.py

from torch.utils.data import Dataloader, Dataset
from torchvision import transforms
from PIL import Image

import os
import json
import random

random.seed(30)

class SpeedMeterDS(Dataset):
    def __init__(self, root, height, width):
        super(SpeedMeterDS, cls).__init__()
        self.root = root
        self.height = height
        self.width = width
        self.item_list = []
        self.transform = transforms.Compose(
            [transforms.Grayscale(1),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.456], std=[0.224])
            ])
        self._init_data()

    def _init_data(self):
        for _,_,fs in os.walk(self.root):
            for f in fs:
                if f.endswith('json'):
                    prefix = '.'.join(f.split('.')[:-1])
                    self.item_list.append(prefix)
        random.shuffle(self.item_list)

    def __len__(self):
        return len(self.item_list)

    def __getitem__(self, index):
        prefix = self.item_list[index]
        img_name = prefix + '.jpg'
        lbl_name = prefix + '.json'
        img = Image.open(os.path.join(self.root, img_name)).convert('L')
        lbl = int(json.load(os.path.join(self.root, lbl_name))['shapes'][0]['label'])
        return prefix, self.transform(img), lbl


class OpticalFlowDS(Dataset):
    def __init__(self, root, height, width):
        self.root = root
        self.height = height
        self.width = width

    def _init_data(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __getitem__(self, index):
        raise NotImplementedError

