# coding:utf-8

import torch
import torch.nn as nn
import torch.functional as F

class Conv2DBlock(nn.Module):
    def __init__(self, 
        in_channel, 
        out_channel, 
        kernel_size,
        stride = 1,
        padding = 0,
        dilation = 0,
        ):
        self.conv = nn.Conv2d(in_channel, out_channel, kernel_size, stride=stride, padding=padding, dilation=dilation)
        self.bn = nn.BatchNorm2d(out_channel)
        self.relu = nn.ReLU(inplace=True)
    
    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        x = self.relu(x)
        return x