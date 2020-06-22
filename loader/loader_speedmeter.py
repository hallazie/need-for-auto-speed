# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-24 00:54:03
# @LastEditTime: 2020-05-10 18:48:49
# @LastEditors: Xiao Shanghua
# @Description:
# @FilePath: \machinelearning\vision\need-for-auto-speed\percept\speed_estimate\dataloader.py

from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from PIL import Image
from utils.common import speed_to_vec

import math
import os
import json
import random

random.seed(30)


class SpeedMeterDS(Dataset):
    '''
        input size: 64
    '''

    def __init__(self, root, height, width):
        super(SpeedMeterDS, self).__init__()
        self.root = root
        self.height = height
        self.width = width
        self.item_list = []
        self.transform = transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.456], std=[0.224])
             ])
        self._init_data()

    @staticmethod
    def _norm_box(box):
        x0, x1 = min(box[0][0], box[1][0]), max(box[0][0], box[1][0])
        y0, y1 = min(box[0][1], box[1][1]), max(box[0][1], box[1][1])
        return [[x0, y0], [x1, y1]]

    @staticmethod
    def _random_attack(img):
        w, h = img.size
        x0, x1 = random.randint(0, w//5), random.randint(0, w//5)
        y0, y1 = random.randint(0, h//5), random.randint(0, h//5)
        return img.crop((0+x0, 0+y0, w-x1, h-y1))

    def _init_data(self):
        for _, _, fs in os.walk(self.root):
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
        lbl_box = json.load(open(os.path.join(self.root, lbl_name), 'r'))['shapes'][0]
        box = self._norm_box(lbl_box['points'])
        lbl = int(lbl_box['label'])
        # lbl = math.log(int(lbl_box['label'])+1)
        vec = speed_to_vec(lbl)
        raw = Image.open(os.path.join(self.root, img_name)).crop((int(box[0][0]), int(box[0][1]), int(box[1][0]), int(box[1][1])))
        raw = self._random_attack(raw)
        img = raw.resize((self.width, self.height), Image.BICUBIC)
        return prefix, self.transform(img), vec


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
