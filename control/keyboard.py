# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-12 13:41:35
# @LastEditTime: 2020-04-12 21:53:38
# @LastEditors: Xiao Shanghua
# @Description: using code from pygta5
# @FilePath: \machinelearning\vision\need-for-auto-speed\control\keyboard.py

from control.credef import *

import time
import ctypes

SendInput = ctypes.windll.user32.SendInput
W = 0x11
A = 0x1E
S = 0x1F
D = 0x20

class Keyboard:
    _instance = None
    
    def __new__(cls, *args, **kws):
        if not cls._instance:
            cls._instance = super(Keyboard, cls).__new__(cls, *args, **kws)
        return cls._instance

    def __init__(self):
        pass

    @staticmethod
    def press(hex_key):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput( 0, hex_key, 0x0008, 0, ctypes.pointer(extra) )
        x = Input( ctypes.c_ulong(1), ii_ )
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    @staticmethod
    def release(hex_key):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput( 0, hex_key, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
        x = Input( ctypes.c_ulong(1), ii_ )
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

keyboard = Keyboard()