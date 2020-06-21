# --*-- coding:utf-8 --*--
# @author: Xiao Shanghua
# @contact: hallazie@outlook.com
# @file: loss_visualize.py
# @time: 2020/6/21 18:11
# @desc: visualize loss

import matplotlib.pyplot as plt
import re


class LossViz:
    def __init__(self):
        self.log_path = '../data/log/speedmeter-estimate.log'
        self.loss_regex = re.compile(r'MAELoss = ([0-9.]+) ')
        self._init_data()

    def _init_data(self):
        self.loss = []
        with open(self.log_path, 'r') as f:
            for line in f:
                loss = [x for x in self.loss_regex.findall(line) if len(x) > 1]
                if len(loss) != 1:
                    continue
                self.loss.append(float(loss[0]))

    def viz(self):
        plt.plot(self.loss)
        plt.show()


if __name__ == '__main__':
    v = LossViz()
    v.viz()
