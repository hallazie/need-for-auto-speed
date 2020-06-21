# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-21 22:47:23
# @LastEditTime: 2020-04-22 01:06:58
# @LastEditors: Xiao Shanghua
# @Description: 
# @FilePath: \machinelearning\vision\need-for-auto-speed\neural\block.py

from config import logger

import torch
import torch.nn as nn
import torch.functional as F


class Conv2DBlock(nn.Module):
    def __init__(self, in_channel, out_channel, kernel_size, stride=1, padding=1, activation='relu'):
        super().__init__()
        self.conv = nn.Conv2d(in_channel, out_channel, kernel_size, stride=stride, padding=padding)
        self.bn = nn.BatchNorm2d(out_channel)
        if activation == 'sigmoid':
            self.relu = nn.Sigmoid()
        else:
            self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        x = self.relu(x)
        return x


class PoolingBlock(nn.Module):
    def __init__(self, pool_type, kernel_size, stride):
        super().__init__()
        if pool_type == 'avg':
            self.pool = nn.AvgPool2d(kernel_size=kernel_size, stride=stride)
        else:
            self.pool = nn.MaxPool2d(kernel_size=kernel_size, stride=stride)

    def forward(self, x):
        x = self.pool(x)
        return x
