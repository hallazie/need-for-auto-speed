# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-13 00:32:55
# @LastEditTime: 2020-04-13 00:51:39
# @LastEditors: Xiao Shanghua
# @Description: 
# @FilePath: \machinelearning\vision\need-for-auto-speed\percept\process.py

from cv2 import cv2

import numpy as np

class Process:
    def __init__(self):
        pass

    @staticmethod
    def optical_flow(previous_, current_):
        previous = cv2.cvtColor(previous_, cv2.COLOR_BGR2GRAY)
        current = cv2.cvtColor(current_, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(previous, current, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        hsv = np.zeros_like(previous_)
        mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
        hsv[...,0] = ang*180/np.pi/2
        hsv[...,1] = 255
        hsv[...,2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        flow = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        return flow

    @staticmethod
    def edge_detect(image):
        return image

processer = Process()