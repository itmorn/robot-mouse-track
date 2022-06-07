import copy
from trace import trace
import numpy as np
import matplotlib.pyplot as plt


class MouseTrajectory:
    def __init__(self, trace):
        self.arr_trace = np.array(trace, np.float64)

        self.max_duration_silent = 20  # 间隔超过多少秒，算静止，将长间隔缩短为一个固定长度

    def get_derivative_to_xy(self, order=4):
        lst_derivative_to_xy = []
        arr_trace = copy.deepcopy(self.arr_trace)
        for _ in range(order):
            arr_diff = arr_trace[1:, :] - arr_trace[:-1, :]
            arr_trace[:-1, :-1] = arr_diff[:, :-1] / np.clip(arr_diff[:, -1:], 0, self.max_duration_silent)
            arr_trace = arr_trace[:-1, :]
            arr = copy.deepcopy(arr_trace)
            lst_derivative_to_xy.append(arr)
        return lst_derivative_to_xy

    def get_derivative(self, order=4):
        lst_derivative = []
        for _ in range(order):
            arr_diff = self.arr_trace[1:, :] - self.arr_trace[:-1, :]
            arr_diff_time = arr_diff[:, -1]
            arr_diff = np.sum((arr_diff[:, :-1] ** 2), axis=1) ** 0.5
            arr_dev = arr_diff / np.clip(arr_diff_time, 0, self.max_duration_silent)  # 间隔超过多少秒，算静止，将长间隔缩短为一个固定长度
            arr_dev = np.c_[arr_dev, self.arr_trace[:len(arr_dev), -1]]
            lst_derivative.append(arr_dev)
        return lst_derivative

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
    mta = MouseTrajectoryAnalyzer(trace)
    mta.show_track()

    lst_derivative = mta.get_derivative(order=2)
    plt.figure()
    for arr_dev_order in lst_derivative:
        plt.plot(arr_dev_order[:, -1], arr_dev_order[:, 0])
    plt.show()
