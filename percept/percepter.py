# --*-- coding:utf-8 --*--
# @author: Xiao Shanghua
# @contact: hallazie@outlook.com
# @file: percepter.py.py
# @time: 2020/6/24 1:48
# @desc: 感知融合

from speed_estimate.speedmeter_estimate import SpeedMeterInference
from items import HiddenState
from config import logger


class Percepter:
    def __init__(self):
        self._init_component()

    def _init_component(self):
        self.speed_meter_inference = SpeedMeterInference(is_train=False)
        self.lane_detect = None
        self.object_detect = None

    @staticmethod
    def _fusion(speed):
        """
        传感器融合，卡尔曼滤波，由sensor data转换为hidden state
        :return:
        """
        state = HiddenState()
        return state

    def run(self, sensor_data):
        """
        将传感器数据（目前只有游戏截图）转换为hidden state
        :param sensor_data:
        :return: new HiddenState()
        """
        speed = self.speed_meter_inference.predict(sensor_data.main_camera)
        state = self._fusion(speed)
        return state
