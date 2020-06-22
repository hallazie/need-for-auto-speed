# --*-- coding:utf-8 --*--
# @author: Xiao Shanghua
# @contact: hallazie@outlook.com
# @file: run.py
# @time: 2020/6/22 1:14
# @desc: 最外层run入口，初始化pipeline
import os
import time

from PIL import ImageGrab

from cv2 import cv2
from control.controller import Controller
from utils.processor import processor

import numpy as np
import traceback


def script():
    """
    执行脚本：data/source/script.txt
    :return:
    """
    controller = Controller()

    for i in range(2)[::-1]:
        print(i + 1)
        time.sleep(1)
    with open(os.path.join(os.sep.join(__file__.split(os.sep)[:-1]), 'data', 'source', 'script.txt'), 'r') as f:
        moves = [x.strip() for x in f.readlines() if x.strip() in ['left', 'right', 'forward', 'backward', 'stop']]

    previous, current = None, None
    while True:
        for m in moves:
            try:
                current = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
                controller.react_basic(m)
                print('performing: %s' % m)
                flow = processor.optical_flow(previous, current)
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


def main_loop():
    """
    使用pipeline
    :return:
    """
    pass


def run():
    script()


if __name__ == '__main__':
    run()
