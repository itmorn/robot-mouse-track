from trace import trace
import numpy as np
import matplotlib.pyplot as plt


def show_track(arr_trace):
    plt.plot(arr_trace[:, 0], -arr_trace[:, 1], ".")  #
    plt.xlim(-100, 1000)
    plt.ylim(-1000, 100)
    plt.show()


class MouseTrajectoryAnalyzer:
    def __init__(self, trace):
        self.arr_trace = np.array(trace)
        self.arr_velocity = None  # 速度
        self.arr_acceleration = None  # 加速度
        self.arr_acceleration_order2 = None  # 2阶加速度
        self.arr_acceleration_order3 = None  # 3阶加速度
        self.arr_acceleration_order4 = None  # 4阶加速度

    def get_velocity(self):
        arr_diff = self.arr_trace[1:, :] - self.arr_trace[:-1, :]
        arr_distance = np.sum(arr_diff[:, :-1] ** 2, axis=1) ** 0.5
        self.arr_velocity = arr_distance / arr_diff[:, -1]
        return self.arr_velocity


if __name__ == '__main__':
    mta = MouseTrajectoryAnalyzer(trace)
    arr_velocity = mta.get_velocity()
    print(arr_velocity)
    # arr_trace = np.array(trace)
    #
    # # 轨迹可视化
    # # show_track(arr_trace)
    #
    # # 计算速度变化
    # arr_speed = calc_speed(arr_trace)
    # plt.plot(arr_speed)
    # plt.show()
