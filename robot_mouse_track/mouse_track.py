import numpy as np
import matplotlib.pyplot as plt
from robot_mouse_track import contants


class MouseTrack:
    """

    **summary line** Function to do something interesting.鼠标轨迹对象

    **description starts after blank line above**Keyword arguments:
    :var ndarray arr_trace: 轨迹数组转成的ndarray
    :var ndarray arr_time: 时间ndarray
    :var int default=20 max_duration_silent: 鼠标在移动的过程中可能会停止。需要定义一个时间间隔，超过多少秒，算静止，将长间隔缩短为一个固定长度
    :var int default=100 max_doa_tan: 方向角正切值峰值截断，超过该值，置为np.clip(angle, -max_doa_tan, max_doa_tan)
    :var int default=5 max_doa_point: 两个点计算角度的时候，采用的是 arr[i] 和 arr[i+max_doa_point]，因为太近的话，误差较大
    :var list[ndarray] feature_dev_combine: 合速度的n阶导数
    :var list[ndarray] feature_dev_decomposition: 分速度的n阶导数
    :var list[ndarray] feature_doa: 方向角
    :var list[ndarray] feature_diff_time: 当前时间差
    """

    def __init__(self, trace):
        """
        :param list[list] trace: 轨迹数组，例如：[[x_1,y_1,timestamp_1],[x_2,y_2,timestamp_2],...]
        """
        self.arr_trace = np.array(trace, np.float64)
        self.arr_time = self.arr_trace[:, -1]

        self.max_duration_silent = 20  # 间隔超过多少秒，算静止，将长间隔缩短为一个固定长度

        self.max_doa_tan = 100  # 正切值峰值截断
        self.max_doa_point = 5  # 两个点计算角度的时候，采用的是 arr[i] 和 arr[i+max_DOA_point]，太近的话，误差较大

        self.feature_dev_combine = []
        self.feature_dev_decomposition = []
        self.feature_doa = []
        self.feature_diff_time = None

        self._arr_diff_dis = None
        self._arr_diff_time = None

    def get_feature_diff_time(self):
        """
        获取样本点之间的时间差

        :return: 时间差的一维数组
        :rtype: ndarray
        """
        if self.feature_diff_time:
            return self.feature_diff_time

        self.feature_diff_time = self.arr_trace[1:, -1] - self.arr_trace[:-1, -1]
        return self.feature_diff_time

    def get_feature_dev(self, order=2, mode=contants.COMBINE):
        """
        计算n-order阶导数

        :param order: 求到第n阶导数
        :param mode: 求导的方式。``combine``：对合速度求导； ``decomposition``：对分速度求导
        :return: 求导后的结果
        :rtype: list[ndarray]
        """
        if mode == contants.COMBINE:
            feature_dev = self.feature_dev_combine
        elif mode == contants.DECOMPOSITION:
            feature_dev = self.feature_dev_decomposition
        else:
            raise Exception("请输入正确的类型")

        if len(feature_dev) >= order:
            return feature_dev

        if not feature_dev:  # 如果求导阶数不够，则增量计算缺的阶数
            self._arr_diff_dis = self.arr_trace[1:, :] - self.arr_trace[:-1, :]
            self._arr_diff_time = np.clip(self._arr_diff_dis[:, -1:], 0, self.max_duration_silent)
            if mode == contants.COMBINE:
                self._arr_diff_dis = \
                    (np.sum((self._arr_diff_dis[:, :-1] ** 2), axis=1) ** 0.5)[:, np.newaxis]
            else:
                self._arr_diff_dis = self._arr_diff_dis[:, :-1]
            order_cur = 0
        else:
            order_cur = len(feature_dev)

        while 1:
            arr_dev = self._arr_diff_dis / self._arr_diff_time[:len(self._arr_diff_dis)]
            # arr = np.c_[arr_dev, self.arr_trace[:len(arr_dev), -1]]
            feature_dev.append(arr_dev)
            order_cur += 1
            if order_cur >= order:
                break
            self._arr_diff_dis = arr_dev[1:] - arr_dev[:-1]

        return feature_dev

    def show_track(self):
        """
        画出鼠标轨迹

        :return: None
        """
        _, axis = plt.subplots(1, 1)
        axis.invert_yaxis()
        plt.plot(self.arr_trace[:, 0], self.arr_trace[:, 1], ".")  #
        axis.set_xlim((-100, 1920))
        axis.set_ylim((1280, -100))
        plt.title("trace xy")
        plt.show()

    def get_feature_doa(self):
        """
        计算方向角变化

        :return: 返回方向角的变化特征
        :rtype: ndarray
        """
        if self.feature_doa:
            return self.feature_doa

        arr_diff_dis = self.arr_trace[self.max_doa_point:, :-1] - \
                       self.arr_trace[:-self.max_doa_point, :-1]
        # 防止除以0
        arr_diff_dis[:, 0][np.where(arr_diff_dis[:, 0] == 0)] = 10e-8

        self.feature_doa = np.clip(
            arr_diff_dis[:, 1] / arr_diff_dis[:, 0], -self.max_doa_tan, self.max_doa_tan
        )

        self.feature_doa = np.arctan(self.feature_doa) * 180 / np.pi
        return self.feature_doa


if __name__ == '__main__':
    from examples import trace_example

    mt = MouseTrack(trace_example.trace1)
    x = mt.get_feature_dev(order=1, mode=contants.COMBINE)
    y = mt.get_feature_dev(order=2, mode=contants.COMBINE)
    print(x)
    print(y)
