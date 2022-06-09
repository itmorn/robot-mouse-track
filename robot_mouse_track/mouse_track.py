import numpy as np
import matplotlib.pyplot as plt
from robot_mouse_track import contants


class MouseTrack:
    def __init__(self, trace):
        self.arr_trace = np.array(trace, np.float64)
        self.arr_time = self.arr_trace[:, -1]

        self.max_duration_silent = 20  # 间隔超过多少秒，算静止，将长间隔缩短为一个固定长度

        self.max_DOA_tan = 100  # 正切值峰值截断
        self.max_DOA_point = 5  # 两个点计算角度的时候，采用的是 arr[i] 和 arr[i+max_DOA_point]，太近的话，误差较大

        self.feature_dev_combine = []
        self.feature_dev_decomposition = []
        self.feature_DOA = []

    def get_feature_dev(self, order=2, mode=contants.COMBINE):
        """
        获取导数特征
        :param order: 求导阶数
        :return:list
        """
        if mode == contants.COMBINE:
            feature_dev = self.feature_dev_combine
        elif mode == contants.DECOMPOSITION:
            feature_dev = self.feature_dev_decomposition
        else:
            raise Exception("请输入正确的类型")

        if len(feature_dev) >= order:
            return feature_dev

        if not feature_dev: # 如果求导阶数不够，则增量计算缺的阶数
            self.arr_diff_dis = self.arr_trace[1:, :] - self.arr_trace[:-1, :]
            self.arr_diff_time = np.clip(self.arr_diff_dis[:, -1:], 0, self.max_duration_silent)
            if mode == contants.COMBINE:
                self.arr_diff_dis = (np.sum((self.arr_diff_dis[:, :-1] ** 2), axis=1) ** 0.5)[:, np.newaxis]
            else:
                self.arr_diff_dis = self.arr_diff_dis[:, :-1]
            order_cur = 0
        else:
            order_cur = len(feature_dev)

        while 1:
            arr_dev = self.arr_diff_dis / self.arr_diff_time[:len(self.arr_diff_dis)]
            # arr = np.c_[arr_dev, self.arr_trace[:len(arr_dev), -1]]
            feature_dev.append(arr_dev)
            order_cur += 1
            if order_cur >= order:
                break
            self.arr_diff_dis = arr_dev[1:] - arr_dev[:-1]

        return feature_dev

    def show_track(self):
        fig, ax = plt.subplots(1, 1)
        ax.invert_yaxis()
        plt.plot(self.arr_trace[:, 0], self.arr_trace[:, 1], ".")  #
        ax.set_xlim((-100, 1920))
        ax.set_ylim((1280, -100))
        plt.title("trace xy")
        plt.show()

    def get_feature_DOA(self):
        """
        计算方向角变化
        :return:
        """
        if self.feature_DOA:
            return self.feature_DOA

        arr_diff_dis = self.arr_trace[self.max_DOA_point:, :-1] - self.arr_trace[:-self.max_DOA_point, :-1]
        # 防止除以0
        arr_diff_dis[:, 0][np.where(arr_diff_dis[:, 0] == 0)] = 10e-8

        self.feature_DOA = np.clip(arr_diff_dis[:, 1] / arr_diff_dis[:, 0], -self.max_DOA_tan, self.max_DOA_tan)
        self.feature_DOA = np.arctan(self.feature_DOA) * 180 / np.pi
        return self.feature_DOA

if __name__ == '__main__':
    from examples import trace_example
    mt = MouseTrack(trace_example.trace1)
    x = mt.get_feature_dev(order=1, mode=contants.COMBINE)
    y = mt.get_feature_dev(order=2, mode=contants.COMBINE)
    print(x)
    print(y)