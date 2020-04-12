# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-12 21:50:39
# @LastEditTime: 2020-04-12 21:55:41
# @LastEditors: Xiao Shanghua
# @Description: 
# @FilePath: \machinelearning\vision\need-for-auto-speed\percept\lane_detect_basic.py

class Perception:
    _instance = None

    def __new__(cls, *args, **kws):
        if not cls._instance:
            cls._instance = super(Perception, cls).__new__(cls, *args, **kws)
        return cls

    def __init__(self):
        pass


perception = Perception()

if __name__ == '__main__':
    pass

