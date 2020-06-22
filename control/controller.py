# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-12 13:33:08
# @LastEditTime: 2020-04-12 21:53:08
# @LastEditors: Xiao Shanghua
# @Description: Controller for car
# @FilePath: \machinelearning\vision\need-for-auto-speed\control\controller.py

from control.keyboard import *
from items import HiddenState

import numpy as np


class Controller:
    _instance = None
    
    def __new__(cls, *args, **kws):
        if not cls._instance:
            cls._instance = super(Controller, cls).__new__(cls, *args, **kws)
        return cls._instance

    def __init__(self):
        self.hidden_state = HiddenState()
        self.history = []

    def react(self, perception):
        """
        实时策略，由perception和hidden state共同决定使用下面哪些操作，暂时用if-else
        TODO 使用策略配置文件简化
        :param perception:
        :return:
        """
        pass

    @staticmethod
    def react_basic(direct):
        """
        最简单的控制，验证按键反馈的
        :param direct:
        :return:
        """
        if direct == 'left':
            keyboard.release(D)
            keyboard.release(S)
            keyboard.press(W)
            keyboard.press(A)
        elif direct == 'right':
            keyboard.release(A)
            keyboard.release(S)
            keyboard.press(W)
            keyboard.press(D)
        elif direct == 'forward':
            keyboard.release(A)
            keyboard.release(D)
            keyboard.release(S)
            keyboard.press(W)
        elif direct == 'backward':
            keyboard.release(A)
            keyboard.release(D)
            keyboard.release(W)
            keyboard.press(S)
        elif direct == 'stop':
            keyboard.release(W)
            keyboard.release(S)
            keyboard.release(A)
            keyboard.release(D)

    @staticmethod
    def slow_down(vol):
        """
        减速，根据vol值决定减速程度
        :param vol: uint
        :return:
        """
        pass

    @staticmethod
    def speed_up(vol):
        """
        加速，根据vol值决定加速程度
        :param vol: uint
        :return:
        """
        pass

    @staticmethod
    def hard_brake():
        """
        急刹车，正面刹死
        :return:
        """

    @staticmethod
    def drift_brake():
        """
        漂移时的轻点刹车，估计做不出来
        :return:
        """
        pass

    def speed_limit(self, limit):
        """
        定速巡航
        :param limit: 定速值，KMpH
        :return:
        """
        if self.hidden_state.speed > limit:
            self.slow_down(self.hidden_state.speed-limit)
        elif self.hidden_state.speed < limit:
            self.speed_limit(limit-self.hidden_state.speed)
