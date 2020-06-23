# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-12 21:51:30
# @LastEditTime: 2020-04-13 01:01:06
# @LastEditors: Xiao Shanghua
# @Description: 
# @FilePath: \machinelearning\vision\need-for-auto-speed\pipeline.py

from cv2 import cv2
from utils.frame_catch import FrameCatcher
from percept.percepter import Percepter
from control.controller import Controller
from items import SensorData
from config import logger


class Pipeline:
    """
    执行的总pipeline main loop，在这里初始化各个感知模块，并运行控制模块及其与感知的交互
    """
    def __init__(self):
        self._init_component()

    def __del__(self):
        logger.info('auto drive pipeline finished...')

    def _init_component(self):
        """
        初始化各组件
        :return:
        """
        self.frame_catcher = FrameCatcher()
        self.percepter = Percepter()
        self.controller = Controller()

    def _sensing(self):
        sensor = SensorData()
        frame = self.frame_catcher.loop_catch()
        sensor.main_camera = frame
        return sensor

    def run(self):
        logger.info('pipeline start running main loop...')
        while True:
            sensor = self._sensing()
            state = self.percepter.run(sensor)
            self.controller.react(state)
            cv2.imshow('data frame', cv2.cvtColor(sensor.main_camera, cv2.COLOR_BGR2RGB))

            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break


if __name__ == '__main__':
    pipeline = Pipeline()

