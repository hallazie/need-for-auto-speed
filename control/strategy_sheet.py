# --*-- coding:utf-8 --*--
# @author: Xiao Shanghua
# @contact: hallazie@outlook.com
# @file: strategy_sheet.py
# @time: 2020/6/23 1:53
# @desc: 具体的if-else流程


def size_turn_dodge_obstacle(hidden_state, perception_state):
    """
    向侧面驾驶躲过障碍物
    :return:
    """
    raise NotImplementedError


def slow_down_dodge_obstacle(hidden_state, perception_state, vol):
    """
    减速躲避障碍物，减速程度根据vol确定，vol达到N时为停车
    :param perception_state:
    :param hidden_state:
    :param vol:
    :return:
    """
    raise NotImplementedError


def back_from_obstacle(hidden_state, perception_state):
    """
    前面堵住了，比如撞墙了或撞车了，倒车回到路上
    :param perception_state:
    :param hidden_state:
    :return:
    """
    raise NotImplementedError


def drift_on_shape_turn(hidden_state, perception_state):
    """
    der漂
    :param perception_state:
    :param hidden_state:
    :return:
    """
    raise NotImplementedError


def honk_on_other_cars(hidden_state, perception_state):
    """
    路怒症
    :param hidden_state:
    :param perception_state:
    :return:
    """
    raise NotImplementedError