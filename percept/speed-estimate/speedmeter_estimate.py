# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-08 19:14:36
# @LastEditTime: 2020-04-22 01:16:10
# @LastEditors: Xiao Shanghua
# @Description: recognize speed meter on need for speed frame
# @FilePath: \machinelearning\vision\need-for-auto-speed\percept\speed-estimate\speedmeter_estimate.py

import torch
import torch.nn as nn
import os
import logging

from torch.utils.data import DataLoader
from torch.optim import Adam
from torch.autograd import Variable

from neural.block import Conv2DBlock, PoolingBlock
from loader.loader_speedmeter import SpeedMeterDS
from config import logger


class SpeedMeterModel(nn.Module):
    def __init__(self):
        # 256*256
        super().__init__()
        self.net = nn.Sequential(
            Conv2DBlock(3, 16, 3),
            PoolingBlock('max', 2, 2),  # 128
            Conv2DBlock(16, 16, 3),
            PoolingBlock('max', 2, 2),  # 64
            Conv2DBlock(16, 16, 3),
            PoolingBlock('max', 2, 2),  # 32
            Conv2DBlock(16, 16, 3),
            PoolingBlock('max', 2, 2),  # 16
            Conv2DBlock(16, 16, 3),
            PoolingBlock('max', 2, 2),  # 8
            Conv2DBlock(16, 16, 3),
            PoolingBlock('max', 2, 2),  # 4
            Conv2DBlock(16, 1, 3),
            PoolingBlock('max', 4, 4),  # 1
        )

    def forward(self, x):
        return self.net(x).squeeze()


class SpeedMeterInference:
    def __init__(self):
        self.epoch = 500
        self.lr = 1e-1
        self.model_path = '/'.join(__file__.split('/')[:-3] + ['data', 'model', 'speed-estimate-speedmeter.weight'])
        self.data_path = '/'.join(__file__.split('/')[:-3] + ['data', 'click-frame-speedmeter'])

    def train(self):
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        logger.info('using device: %s' % str(device))
        model = SpeedMeterModel().to(device)
        dataset = SpeedMeterDS(self.data_path, height=256, width=256)
        loader = DataLoader(dataset, batch_size=4, shuffle=True)
        optimizer = Adam(model.parameters(), lr=self.lr)
        loss_func = nn.MSELoss()

        for e in range(self.epoch):
            model.train()
            for i, (_, data, label) in enumerate(loader):
                data = data.to(device)
                label = label.to(device).type(torch.float)
                out = model(data)
                loss = loss_func(out, label)
                logger.info('epoch %s, batch %s, MAELoss = %s (label: %s, predict: %s)' % (e, i, loss.data.item(), label.data.cpu().numpy(), out.data.cpu().numpy()))
                loss.backward()
                optimizer.step()
                optimizer.zero_grad()
            if e % 10 == 0 and e > 0:
                torch.save(model, self.model_path)

    def test(self):
        pass

    def predict(self):
        pass


if __name__ == '__main__':
    logger.setLevel(logging.INFO)
    speed_meter_inf = SpeedMeterInference()
    speed_meter_inf.train()
