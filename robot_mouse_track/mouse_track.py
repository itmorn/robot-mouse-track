import numpy as np
import matplotlib.pyplot as plt

DECOMPOSITION = "decomposition"
COMBINE = "combine"


class MouseTrack:
    def __init__(self, trace):
        self.arr_trace = np.array(trace, np.float64)
        self.arr_time = self.arr_trace[:, -1]

        self.max_duration_silent = 20  # 间隔超过多少秒，算静止，将长间隔缩短为一个固定长度
        self.max_DOA = 20  # 正切值峰值截断

        self.feature_dev = []

    def get_feature_dev(self, order=2, mode=COMBINE):
        """
        获取导数特征
        :param order: 求导阶数
        :return:list
        """
        if self.feature_dev:
            return self.feature_dev

        arr_diff_dis = self.arr_trace[1:, :] - self.arr_trace[:-1, :]
        arr_diff_time = np.clip(arr_diff_dis[:, -1:],0,self.max_duration_silent)
        if mode == COMBINE:
            arr_diff_dis = (np.sum((arr_diff_dis[:, :-1] ** 2), axis=1) ** 0.5)[:, np.newaxis]
        elif mode == DECOMPOSITION:
            arr_diff_dis = arr_diff_dis[:, :-1]
        else:
            raise Exception("请输入正确的类型")

        order_cur = 1
        while 1:
            arr_dev = arr_diff_dis / arr_diff_time[:len(arr_diff_dis)]
            # arr = np.c_[arr_dev, self.arr_trace[:len(arr_dev), -1]]
            self.feature_dev.append(arr_dev)
            order_cur += 1
            if order_cur > order:
                break
            arr_diff_dis = arr_dev[1:] - arr_dev[:-1]

        return self.feature_dev

    def show_track(self):
        fig, ax = plt.subplots(1, 1)
        ax.invert_yaxis()
        plt.plot(self.arr_trace[:, 0], self.arr_trace[:, 1], ".")  #
        ax.set_xlim((-100, 1920))
        ax.set_ylim((1280, -100))
        plt.title("trace xy")
        plt.show()

    def get_feature_DOA(self):
        arr_diff_dis = self.arr_trace[1:, :-1] - self.arr_trace[:-1, :-1]
        # 防止除以0
        arr_diff_dis[:, 0][np.where(arr_diff_dis[:, 0] == 0)] = 10e-8
        arr_DOA = np.clip(arr_diff_dis[:, 1] / arr_diff_dis[:, 0], -self.max_DOA, self.max_DOA)
        return arr_DOA
