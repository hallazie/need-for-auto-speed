# --*-- coding:utf-8 --*--
# @author: Xiao Shanghua
# @contact: hallazie@outlook.com
# @file: common.py
# @time: 2020/6/21 13:52
# @desc:

from config import logger

import time
import numpy as np


def time_monitor(func):
    def warp(*args):
        start = time.time()
        ret = func(*args)
        end = time.time()
        logger.info('func %s cost [%s] ms' % (str(func), round((end - start) * 1000, 5)))
        return ret
    return warp


def speed_to_vec(speed):
    if not 0 <= speed <= 999:
        return [0 if i != 0 else 1 for i in range(10)] * 3
    speed = str(speed).zfill(3)
    v1 = [1 if str(i) == speed[0] else 0 for i in range(10)]
    v2 = [1 if str(i) == speed[1] else 0 for i in range(10)]
    v3 = [1 if str(i) == speed[2] else 0 for i in range(10)]
    return np.array(v1 + v2 + v3)


def vec_to_speed(vec):
    s1 = np.argmax(np.array(vec[:10]))
    s2 = np.argmax(np.array(vec[10:20]))
    s3 = np.argmax(np.array(vec[20:30]))
    ss = str(s1) + str(s2) + str(s3)
    return int(ss)


if __name__ == '__main__':
    print(speed_to_vec(143))
    print(vec_to_speed(speed_to_vec(243)))
    print(speed_to_vec(1))
    print(vec_to_speed([0.28204027, 0.7356036, 0.3616177, 0.50450927, 0.44730622, 0.46925727, 0.2946604, 0.32755107, 0.5407517, 0.73662645, 0.49820295, 0.35801214, 0.44046822, 0.92693216, 0.36902648, 0.3588559, 0.43562058, 0.6000769, 0.5352033, 0.1441437, 0.3043302, 0.500643, 0.4520338, 0.37544662, 0.31462455, 0.8753471, 0.4375557, 0.39101076, 0.45179933, 0.40260974]))
