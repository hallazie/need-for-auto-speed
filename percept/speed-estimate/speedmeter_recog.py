# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-08 19:14:36
# @LastEditTime: 2020-04-22 01:16:10
# @LastEditors: Xiao Shanghua
# @Description: recognize speed meter on need for speed frame
# @FilePath: \machinelearning\vision\need-for-auto-speed\percept\speed-estimate\speedmeter_recog.py

import torch
import torch.nn as nn
import torch.functional as F
import os

from neural.block import Conv2DBlock, PoolingBlock

class SpeedMeterRecog(nn.Module):
    def __init__(self):
        # 256*256
        self.net = nn.Sequential(
            Conv2DBlock(3, 16, 3),
            PoolingBlock('max', 2, 2), # 128
            Conv2DBlock(16, 16, 3),
            PoolingBlock('max', 2, 2), # 64
            Conv2DBlock(16, 16, 3),
            PoolingBlock('max', 2, 2), # 32
            Conv2DBlock(16, 16, 3),
            PoolingBlock('max', 2, 2), # 16
            Conv2DBlock(16, 16, 3),
            PoolingBlock('max', 2, 2), # 8
            Conv2DBlock(16, 16, 3),
            PoolingBlock('max', 2, 2), # 4
            Conv2DBlock(16, 16, 3),
            PoolingBlock('max', 2, 2), # 2
            Conv2DBlock(16, 1, 3),
            PoolingBlock('max', 2, 2), # 1
        )

    def forward(self, x):
        return self.net(x)


class Model:
    def __init__(self, train):
        self.train = train
        self.model_path = os.path.join(os.sep.join(__file__.split(os.sep)[:-2]), 'checkpoint', 'speedmeter-recog.weight')
        self.model = SpeedMeterRecog()
        if not self.train:
            self.model.load_state_dict(torch.load(self.model_path))

    def train(self):
        pass

    def test(self):
        pass

    def predict(self):
        pass