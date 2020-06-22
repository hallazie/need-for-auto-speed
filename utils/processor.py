# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-13 00:32:55
# @LastEditTime: 2020-05-01 12:33:16
# @LastEditors: Xiao Shanghua
# @Description: 
# @FilePath: \machinelearning\vision\need-for-auto-speed\percept\processor.py

from cv2 import cv2
from config import logger

import matplotlib.pyplot as plt
import numpy as np
import os
import math


class Process:
    """
    图像处理工具类
    """
    def __init__(self):
        pass

    def _init_test(self):
        self.img1 = cv2.imread(
            os.path.join(os.sep.join(__file__.split(os.sep)[:-2]), 'data', 'click-frame-sample', 'frame-2000.jpg'))
        self.img2 = cv2.imread(
            os.path.join(os.sep.join(__file__.split(os.sep)[:-2]), 'data', 'click-frame-sample', 'frame-2020.jpg'))

    @staticmethod
    def optical_flow(previous_, current_):
        """
        光流
        :param previous_:
        :param current_:
        :return:
        """
        previous = cv2.cvtColor(previous_, cv2.COLOR_BGR2GRAY)
        current = cv2.cvtColor(current_, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(previous, current, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        hsv = np.zeros_like(previous_)
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 1] = 255
        hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        flow = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        return flow

    @staticmethod
    def hough_transfer(image):
        """
        hough变换，在图像中找到所有直线
        :param image:
        :return:
        """
        lines = cv2.HoughLinesP(image, 1, np.pi / 180, 180, 20, 15)
        return lines

    @staticmethod
    def draw_lines(image, lines):
        """
        在图像上画线，方便观察
        :param image:
        :param lines:
        :return:
        """
        try:
            for line in lines:
                coords = line[0]
                cv2.line(image, (coords[0], coords[1]), (coords[2], coords[3]), [255, 255, 255], 1)
        except Exception as e:
            logger.error('line drawing error')
        finally:
            return image

    @staticmethod
    def edge_detect(image):
        """
        使用canny变换进行边缘检测
        不适用sobel等算子，canny更平滑
        :param image:
        :return:
        """
        edge = cv2.Canny(image, threshold1=200, threshold2=300)
        edge = cv2.GaussianBlur(edge, (5, 5), 0)
        return edge

    @staticmethod
    def roi_cropping(image, points):
        """
        将游戏画面裁剪，只保留道路相关区域，丢弃天空等无关信息
        :param image:
        :param points:
        :return:
        """
        mask = np.zeros_like(image)
        cv2.fillPoly(mask, [points], 255)
        masked = cv2.bitwise_and(image, mask)
        return masked

    @staticmethod
    def fft(image):
        """
        快速傅里叶变换，没用到
        :param image:
        :return:
        """
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fft2 = np.fft.fft2(image)
        fshift = np.fft.fftshift(fft2)
        result = 20 * np.log(np.abs(fshift))
        return result

    @staticmethod
    def feature_extraction(image):
        """
        特征点检测，没用到
        :param image:
        :return:
        """
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        akaze = cv2.AKAZE_create()
        kps = akaze.detect(image, None)
        draw = image.copy()
        draw = cv2.drawKeypoints(image, kps, draw)
        return draw, kps

    @staticmethod
    def corner_extraction(image):
        """
        角点检测，没用到
        :param image:
        :return:
        """
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image.copy()
        dst = cv2.cornerHarris(image, 2, 3, 0.04)
        print('before dilate size:', dst.shape)
        dst = cv2.dilate(dst, None)
        print('after dilate size:', dst.shape)
        image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        image[dst > 0.01 * dst.max()] = [0, 0, 255]
        return image, dst

    @staticmethod
    def to_gray(image):
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return image

    @staticmethod
    def equalizer(image):
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        eq = cv2.equalizeHist(image)
        return eq

    @staticmethod
    def imshow(t, *args):
        if t == 'optical':
            plt.suptitle('optical flow')
            plt.subplot(1, 3, 1), plt.title('previous')
            plt.imshow(args[0]), plt.axis('off')
            plt.subplot(1, 3, 2), plt.title('current')
            plt.imshow(args[1]), plt.axis('off')
            plt.subplot(1, 3, 3), plt.title('optical flow')
            plt.imshow(args[2]), plt.axis('off')
            plt.show()
        elif t == 'edge':
            plt.suptitle('edge')
            plt.subplot(1, 2, 1), plt.title('rgb')
            plt.imshow(args[0]), plt.axis('off')
            plt.subplot(1, 2, 2), plt.title('edge')
            plt.imshow(args[1]), plt.axis('off')
            plt.show()
        elif t == 'single':
            plt.suptitle('single image')
            plt.subplot(1, 1, 1), plt.title('single')
            plt.imshow(args[0]), plt.axis('off')
            plt.show()
        elif t == 'random':
            size = len(args)
            height = math.ceil(size / 2.0)
            for i in range(size):
                plt.subplot(2, height, i + 1)
                plt.imshow(args[i])
            plt.show()


processor = Process()

if __name__ == '__main__':
    processor._init_test()
    gray = processor.to_gray(processor.img1)
    eq = processor.equalizer(processor.img1)
    edge = processor.edge_detect(eq)
    edge2 = processor.edge_detect(gray)
    feature, _ = processor.feature_extraction(gray)
    corner, _ = processor.corner_extraction(gray)
    processor.imshow('random', gray, eq, edge2, edge, feature, corner)
