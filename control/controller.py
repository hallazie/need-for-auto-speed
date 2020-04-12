# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-12 13:33:08
# @LastEditTime: 2020-04-12 13:42:04
# @LastEditors: Xiao Shanghua
# @Description: Controller for car
# @FilePath: \machinelearning\vision\gta5-driver\control\controller.py

import numpy as np

class Controller:
    _instance = None
    
    def __new__(cls, *args, **kws):
        if not cls._instance:
            cls._instance = super(Controller, cls).__new__(cls, *args, **kws)
        return cls._instance

    def __init__(self):
        self.hidden_state = {}

    def react(self, perception):
        '''
            current perception + hidden state -> current control stratage
        '''
        pass


if __name__ == '__main__':
    controller = Controller()