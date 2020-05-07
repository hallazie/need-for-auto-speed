# coding:utf-8

from cv2 import cv2 as cv2
from torch.utils.data import Dataset

import os

class BaseDataset(Dataset):
    '''
        image data iter, label based transfer
    '''
    def __init__(self, input_shape, target_shape, input_folder, target_folder, input_transform=None, target_transform=None, input_postfix='jpg', target_postfix=None, target_reader=None, **kw_arg):
        super(BaseDataset, self).__init__()
        self.input_shape = input_shape
        self.target_shape = target_shape
        self.input_folder = input_folder
        self.target_folder = target_folder
        self.input_transform = input_transform
        self.target_transform = target_transform
        self.input_postfix = input_postfix
        self.target_postfix = target_postfix
        self.target_reader = target_reader
        self.input_list = []
        self.kw_arg = kw_arg
        for f in os.listdir(self.input_folder):
            if f.endswith(self.input_postfix):
                self.input_list.append(f)

    def __len__(self):
        return len(self.input_list)

    def __getitem__(self, idx):
        prefix = '.'.join(self.input_list[idx].split('.')[:-1])
        input_path = os.path.join(self.input_folder, prefix+'.'+self.input_postfix)
        target_path = os.path.join(self.target_folder, prefix+'.'+self.target_postfix)
        inp = cv2.imread(input_path)
        inp = cv2.resize(inp, self.input_shape)
        if 'input_color' in self.kw_arg and self.kw_arg['input_color'] == 'gray':
            inp = cv2.cvtColor(inp, cv2.COLOR_BGR2GRAY)
        if self.target_reader is not None:
            tar = self.target_reader(target_path)
        else:
            tar = cv2.imread(target_path)
            tar = cv2.resize(tar, self.target_shape)
            if 'target_color' in self.kw_arg and self.kw_arg['target_color'] == 'gray':
                tar = cv2.cvtColor(tar, cv2.COLOR_BGR2GRAY)
        return prefix, inp, tar