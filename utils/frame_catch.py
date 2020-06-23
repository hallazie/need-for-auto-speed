# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-21 00:49:58
# @LastEditTime: 2020-04-22 00:34:53
# @LastEditors: Xiao Shanghua
# @Description: 
# @FilePath: \machinelearning\vision\need-for-auto-speed\process\frame_catch.py

from cv2 import cv2
from PIL import ImageGrab

import numpy as np
import time
import os


class FrameCatcher:
    def __init__(self, bbox=(0, 40, 800, 640)):
        self.bbox = bbox
        self.frame_count = 0
        self.frame_click = 5
        self.frame_save_path = os.path.join(os.sep.join(__file__.split(os.sep)[:-2]), 'data', 'click-frame', 'frame-%s.jpg')

    def loop_catch(self):
        screen = np.array(ImageGrab.grab(self.bbox))
        return cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

    def click_catch(self):
        while True:
            screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
            cv2.imshow('window1', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))

            if self.frame_count % self.frame_click == 0:
                cv2.imwrite(self.frame_save_path % self.frame_count, cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
                print('frame %s save finished...' % self.frame_count)

            self.frame_count += 1

            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break


if __name__ == '__main__':
    fc = FrameCatch()
    fc.click_catch()
