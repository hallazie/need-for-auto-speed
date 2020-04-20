# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-13 00:32:55
# @LastEditTime: 2020-04-21 02:03:20
# @LastEditors: Xiao Shanghua
# @Description: 
# @FilePath: \machinelearning\vision\need-for-auto-speed\percept\process.py

from cv2 import cv2

import matplotlib.pyplot as plt
import numpy as np
import os

class Process:
    def __init__(self):
        pass

    def _init_test(self):
        self.img1 = cv2.imread(os.path.join(os.sep.join(__file__.split(os.sep)[:-2]), 'data', 'click-frame-sample', 'frame-100.jpg'))
        self.img2 = cv2.imread(os.path.join(os.sep.join(__file__.split(os.sep)[:-2]), 'data', 'click-frame-sample', 'frame-1400.jpg'))

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
        edge = cv2.Canny(image, threshold1 = 200, threshold2=300)
        edge = cv2.GaussianBlur(edge,(5,5),0)
        return edge

    @staticmethod
    def imshow(t, *args):
        if t == 'optical':
            plt.suptitle('optical flow')
            plt.subplot(1,3,1), plt.title('previous')
            plt.imshow(args[0]), plt.axis('off')
            plt.subplot(1,3,2), plt.title('current')
            plt.imshow(args[1]), plt.axis('off')
            plt.subplot(1,3,3), plt.title('optical flow')
            plt.imshow(args[2]), plt.axis('off')
            plt.show()
        elif t == 'edge':
            plt.suptitle('edge')
            plt.subplot(1,2,1), plt.title('rgb')
            plt.imshow(args[0]), plt.axis('off')
            plt.subplot(1,2,2), plt.title('edge')
            plt.imshow(args[1]), plt.axis('off')
            plt.show()

processer = Process()

if __name__ == '__main__':
    processer._init_test()
    # flow = processer.optical_flow(processer.img1, processer.img2)
    # processer.imshow('optical', processer.img1, processer.img2, flow)
    edge = processer.edge_detect(processer.img1)
    processer.imshow('edge', processer.img1, edge)