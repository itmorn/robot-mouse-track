import copy
from trace import trace
import numpy as np
import matplotlib.pyplot as plt


class MouseTrajectory:
    def __init__(self, trace):
        self.arr_trace = np.array(trace, np.float64)

        self.max_duration_silent = 20  # 间隔超过多少秒，算静止，将长间隔缩短为一个固定长度

    # def get_feature_dev_partial(self, order=2):
    #     """
    #     获取偏导数特征
    #     :param order: 求导阶数
    #     :return:list
    #     """
    #     arr_dev = self.arr_trace
    #     lst_feature_dev_partial = []
    #     for _ in range(1, order + 1):
    #         arr_diff = arr_dev[1:, :] - arr_dev[:-1, :]
    #         arr_dev = arr_diff[:, :-1] / np.clip(arr_diff[:, -1:], 0, self.max_duration_silent)
    #         arr_dev = np.c_[arr_dev, self.arr_trace[:len(arr_dev), -1]]
    #         lst_feature_dev_partial.append(arr_dev)
    #     return lst_feature_dev_partial

    def get_feature_dev(self, order=2, mode="all"):
        """
        获取导数特征
        :param order: 求导阶数
        :return:list
        """
        lst_feature_dev = []

        arr_diff_dis = self.arr_trace[1:, :] - self.arr_trace[:-1, :]
        arr_diff_time = arr_diff_dis[:, -1:]
        if mode == "all":
            arr_diff_dis = (np.sum((arr_diff_dis[:, :-1] ** 2), axis=1) ** 0.5)[:, np.newaxis]
        else:
            arr_diff_dis = arr_diff_dis[:, :-1]

        order_cur = 1
        while 1:
            arr_dev = arr_diff_dis / arr_diff_time[:len(arr_diff_dis)]
            arr = np.c_[arr_dev, self.arr_trace[:len(arr_dev), -1]]
            lst_feature_dev.append(arr)
            order_cur += 1
            if order_cur > order:
                break
            arr_diff_dis = arr_dev[1:] - arr_dev[:-1]

        return lst_feature_dev

    def show_track(self):
        fig, ax = plt.subplots(1, 1)
        ax.invert_yaxis()
        plt.plot(self.arr_trace[:, 0], self.arr_trace[:, 1], ".")  #
        ax.set_xlim((-100, 1920))
        ax.set_ylim((1280, -100))
        plt.title("trace xy")
        # plt.xlim(0, 2000)
        # plt.ylim(0, 2000)
        plt.show()


if __name__ == '__main__':
    mta = MouseTrajectory(trace)
    mta.show_track()

    lst_feature = mta.get_feature_dev(order=3, mode="") #all

    for arr_feature in lst_feature:
        plt.figure()
        x_time = arr_feature[:, -1]
        y_dev = arr_feature[:, 0]
        plt.plot(x_time, y_dev)
        plt.show()
