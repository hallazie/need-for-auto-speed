# --*-- coding:utf-8 --*--
# @author: Xiao Shanghua
# @contact: hallazie@outlook.com
# @file: items.py
# @time: 2020/6/23 1:29
# @desc:


class Obstacle:
    """
    障碍物类别
    """
    def __init__(self, typ_=None, distance=None, direction=None):
        self.type = typ_
        self.distance = distance
        self.direction = direction


class HiddenState:
    """
    车辆当前状态
    """
    def __init__(self):
        self.speed = 0                  # KM/H 速度
        self.global_direction = 0       # 0~360
        self.relative_direction = 0     # 与当前设定道路方向得相对方向，和lane offset差不多？
        self.lane_offset = 0            # 还没想好
        self.is_blocked = False         # 前方是否无法通行
        self.obstacle_list = []             # obs list

