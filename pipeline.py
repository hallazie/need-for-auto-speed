# --*-- utf-8 --*--
# @Author: Xiao Shanghua
# @Date: 2020-04-12 21:51:30
# @LastEditTime: 2020-04-13 01:01:06
# @LastEditors: Xiao Shanghua
# @Description: 
# @FilePath: \machinelearning\vision\need-for-auto-speed\pipeline.py

from percept.speed_estimate.speedmeter_estimate import SpeedMeterInference
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
        self.speed_meter_inference = SpeedMeterInference(is_train=False)
        self.controller = None


if __name__ == '__main__':
    pipeline = Pipeline()

