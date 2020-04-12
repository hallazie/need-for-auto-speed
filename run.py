# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-12 21:51:30
# @LastEditTime: 2020-04-12 22:27:34
# @LastEditors: Xiao Shanghua
# @Description: 
# @FilePath: \machinelearning\vision\need-for-auto-speed\run.py

from control.controller import controller
from percept.lane_detect_basic import perception

import time

class Pipeline:
    def __init__(self):
        self.frame_gap = 0.1

    def __del__(self):
        print('auto drive pipeline finished...')

    def script(self):
        with open('data/script.txt', 'r') as f:
            moves = [x.strip() for x in f.readlines() if x.strip() in ['left', 'right', 'forward', 'backward', 'stop']]
        for m in moves:
            controller.react_basic(m)
            time.sleep(self.frame_gap)

    def run(self):
        pass

if __name__ == '__main__':
    pipeline = Pipeline()
    pipeline.script()