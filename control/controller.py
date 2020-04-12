# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-12 13:33:08
# @LastEditTime: 2020-04-12 21:53:08
# @LastEditors: Xiao Shanghua
# @Description: Controller for car
# @FilePath: \machinelearning\vision\need-for-auto-speed\control\controller.py

from control.keyboard import *

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

    def react_basic(self, direct):
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

controller = Controller()

if __name__ == '__main__':
    pass