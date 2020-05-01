# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-12 21:50:39
# @LastEditTime: 2020-05-01 12:38:42
# @LastEditors: Xiao Shanghua
# @Description: 
# @FilePath: \machinelearning\vision\need-for-auto-speed\percept\lane_detect.py

from cv2 import cv2 as cv2
from process import processer

import os
import numpy as np

class Perception:
    def __init__(self):
        self.test_image = cv2.imread('f:/machinelearning/vision/need-for-auto-speed/data/click-frame-sample/frame-500.jpg')
        self.roi_points = np.array([[0,480],[0,400], [100,300], [700,300], [800,400], [800,480]], np.int32)

    def _test(self):
        self.test_image = cv2.cvtColor(self.test_image, cv2.COLOR_BGR2GRAY)
        roi_image = processer.roi_cropping(self.test_image, self.roi_points)
        processer.imshow('single', roi_image)

    def _process(self, image):
        image_raw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_edge = processer.edge_detect(image_raw)
        image_edge = processer.roi_cropping(image_edge, self.roi_points)
        lines = processer.hough_transfer(image_edge)
        image_hough = processer.draw_lines(image_edge, lines)
        processer.imshow('optical', image_raw, image_edge, image_hough)

perception = Perception()

if __name__ == '__main__':
    perception._process(perception.test_image)

