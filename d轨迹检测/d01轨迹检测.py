import copy

# from trace import trace
import numpy as np
import matplotlib.pyplot as plt


class MouseTrajectoryAnalyzer:
    def __init__(self, trace):
        self.arr_trace = np.array(trace, np.float64)  #

    def get_derivative_to_xy(self, order=4):
        lst_derivative_to_xy = []
        arr_trace = copy.deepcopy(self.arr_trace)
        for _ in range(order):
            arr_diff = arr_trace[1:, :] - arr_trace[:-1, :]
            arr_trace[:-1, :-1] = arr_diff[:, :-1] / np.clip(arr_diff[:, -1:], 0, 20)  # 间隔超过多少秒，算静止，将长间隔缩短为一个固定长度
            arr_trace = arr_trace[:-1, :]
            arr = copy.deepcopy(arr_trace)
            lst_derivative_to_xy.append(arr)
        return lst_derivative_to_xy

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

    lst_derivative_to_xy = mta.get_derivative_to_xy(order=4)
    plt.figure()
    for arr_dev_order in lst_derivative_to_xy:
        plt.plot(arr_dev_order[:, -1], arr_dev_order[:, 0])
    plt.show()
