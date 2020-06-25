# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-08 19:14:36
# @LastEditTime: 2020-04-22 01:16:10
# @LastEditors: Xiao Shanghua
# @Description: recognize speed meter on need for speed frame
# @FilePath: \machinelearning\vision\need-for-auto-speed\percept\speed_estimate\speedmeter_estimate.py
import os
import random

import torch
import torch.nn as nn
import logging
import math

from torch.utils.data import DataLoader
from torch.optim import Adam
from torch.autograd import Variable
from torchvision.transforms import transforms
from PIL import Image

from neural.block import Conv2DBlock, PoolingBlock
from loader.loader_speedmeter import SpeedMeterDS
from config import logger
from utils.common import time_monitor, vec_to_speed


class SpeedMeterModel(nn.Module):
    def __init__(self):
        # 256*256
        super().__init__()
        self.net = nn.Sequential(
            Conv2DBlock(3, 16, 3),
            PoolingBlock('max', 2, 2),  # 32
            Conv2DBlock(16, 16, 3),
            PoolingBlock('max', 2, 2),  # 16
            Conv2DBlock(16, 16, 3),
            PoolingBlock('max', 2, 2),  # 8
            Conv2DBlock(16, 16, 3),
            PoolingBlock('max', 2, 2),  # 4
            Conv2DBlock(16, 16, 3),
            PoolingBlock('max', 2, 2),  # 2
            Conv2DBlock(16, 16, 3),
            PoolingBlock('max', 2, 2),  # 1
            Conv2DBlock(16, 24, 3, activation='sigmoid'),
        )

    def forward(self, x):
        return self.net(x).squeeze()


class SpeedMeterInference:
    def __init__(self, is_train=False):
        self.is_train = is_train
        self.epoch = 5000
        self.lr = 1e-3
        self.batch_size = 128
        self.width = 64
        self.height = 64
        self.model_path = '/'.join(__file__.split('/')[:-3] + ['data', 'model', 'speed_estimate-speedmeter.weight'])
        self.data_path = '/'.join(__file__.split('/')[:-3] + ['data', 'click-frame-speedmeter'])
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize(mean=[0.456], std=[0.224])])
        if not self.is_train:
            self._init_model()

    def _init_model(self):
        if not hasattr(self, 'model') or type(self.model) is SpeedMeterModel:
            self.model = torch.load(self.model_path).to(self.device).eval()

    @staticmethod
    def _exp(n):
        return int((math.e**n)-1)

    def train(self):
        logger.info('using device: %s' % str(self.device))
        model = SpeedMeterModel().to(self.device)
        dataset = SpeedMeterDS(self.data_path, height=self.width, width=self.height)
        logger.info('dataset init finished with size: %s' % len(dataset))
        loader = DataLoader(dataset, batch_size=self.batch_size, shuffle=True)
        optimizer = Adam(model.parameters(), lr=self.lr)
        loss_func = nn.BCELoss()

        for e in range(self.epoch):
            model.train()
            for i, (_, data, label) in enumerate(loader):
                try:
                    data = data.to(self.device)
                    label = label.to(self.device).type(torch.float)
                    out = model(data)
                    loss = loss_func(out, label)
                    logger.info('epoch %s, batch %s, MAELoss = %s (label: %s, predict: %s)' % (e, i, loss.data.item(), [vec_to_speed(list(x)) for x in label.data.cpu().numpy()[:4]], [vec_to_speed(list(x)) for x in out.data.cpu().numpy()[:4]]))
                    loss.backward()
                    optimizer.step()
                    optimizer.zero_grad()
                except Exception as err:
                    logger.error(err)
            if e % 10 == 0 and e > 0:
                torch.save(model, self.model_path)

    @time_monitor
    def _inference_single(self, img):
        return self.model(img).data.cpu().numpy()

    def test(self):
        self._init_model()
        f_list = []
        for _, _, fs in os.walk('../../data/click-frame-speedmeter'):
            for f in fs:
                if f.endswith('jpg'):
                    f_list.append(f.split('.')[0]+'.jpg')
        random.shuffle(f_list)
        for f in f_list[:100]:
            img = Image.open('../../data/click-frame-speedmeter/%s' % f)
            w, h = img.size
            meter = img.crop((w-120, h-80, w, h)).resize((self.width, self.height), Image.BICUBIC)
            vec = self.predict(meter)
            speed = vec_to_speed(vec)
            logger.info('predicted speed: %s' % speed)
            meter.save('../../data/output/%s-%s.jpg' % (f.split('.')[0], speed))

    def predict(self, img):
        img = self.transform(img).to(self.device)
        img = torch.unsqueeze(img, dim=0)
        out = self._inference_single(img)
        return out


if __name__ == '__main__':
    logger.setLevel(logging.INFO)
    speed_meter_inf = SpeedMeterInference(False)
    # speed_meter_inf.train()
    speed_meter_inf.test()
