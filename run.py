# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-12 21:51:30
# @LastEditTime: 2020-04-13 01:01:06
# @LastEditors: Xiao Shanghua
# @Description: 
# @FilePath: \machinelearning\vision\need-for-auto-speed\run.py

from PIL import ImageGrab
from cv2 import cv2

from control.controller import controller
from percept.lane_detect_basic import perception
from percept.process import processer

import time
import numpy as np
import os
import traceback

class Pipeline:
    def __init__(self):
        self.frame_gap = 1

    def __del__(self):
        print('auto drive pipeline finished...')

    def script(self):
        for i in range(2)[::-1]:
            print(i+1)
            time.sleep(1)
        with open(os.path.join(os.sep.join(__file__.split(os.sep)[:-1]), 'data', 'script.txt'), 'r') as f:
            moves = [x.strip() for x in f.readlines() if x.strip() in ['left', 'right', 'forward', 'backward', 'stop']]
            
        previous = None
        while True:
            for m in moves:
                try:
                    current = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
                    controller.react_basic(m)
                    print('performing: %s' % m)
                    # time.sleep(self.frame_gap)
                    flow = processer.optical_flow(previous, current)
                    cv2.imshow('window', cv2.cvtColor(flow, cv2.COLOR_BGR2RGB))
                except Exception as e:
                    print(e)
                    traceback.print_exc()
                finally:
                    previous = current
                    time.sleep(0.1)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        cv2.destroyAllWindows()
                        return
        controller.react_basic('stop')

    def run(self):
        self.script()

if __name__ == '__main__':
    pipeline = Pipeline()
    pipeline.script()

