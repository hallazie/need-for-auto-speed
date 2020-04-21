# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-08 19:14:36
# @LastEditTime: 2020-04-09 10:44:00
# @LastEditors: Xiao Shanghua
# @Description: recognize speed meter on need for speed frame
# @FilePath: 

import torch
import torch.nn as nn
import torch.functional as F

from neural.block import Conv2DBlock

class SpeedMeterRecog(nn.Module):
    def __init__(self):
        self.net = nn.Sequential(

        )

    def forward(self, x):
        return x