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
    s1 = [str(i) for i in range(10) if vec[i] == 1]
    s2 = [str(i) for i in range(10) if vec[10+i] == 1]
    s3 = [str(i) for i in range(10) if vec[20+i] == 1]
    ss = (s1[0] if len(s1) == 1 else '0') + (s2[0] if len(s2) == 1 else '0') + (s3[0] if len(s3) == 1 else '0')
    return int(ss)


if __name__ == '__main__':
    print(speed_to_vec(143))
    print(speed_to_vec(1))
    print(vec_to_speed((speed_to_vec(145))))
    print(vec_to_speed((speed_to_vec(986))))
    print(vec_to_speed((speed_to_vec(9999))))
    print(vec_to_speed((speed_to_vec(-2))))
