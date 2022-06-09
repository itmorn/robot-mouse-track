from robot_mouse_track.mouse_track import MouseTrack
import numpy as np
from robot_mouse_track.utils import num_runs, small_runs
from robot_mouse_track import contants


class ConstantVelocityMotion:
    # 分速度的匀速运动【实现】
    # 分速度的匀变速运动【实现】
    # 分速度的匀变加速运动
    # 合速度的匀速运动【实现】
    # 合速度的匀变速运动【实现】
    # 合速度的匀变加速运动
    def __init__(self):
        self.direction = contants.COMBINE  # 方向  x，y，combine
        self.n_order_dev = 2  # 距离对时间的几阶导数  1阶是速度  2阶是加速度  3阶是加速度的变化速率

        self.least_point = 5  # 最少要包含的点的个数
        self.least_length = 100  # 最少移动的距离

        self.th_span = 0.01  # 两点之间的最大变化幅度，低于这个值，则认为是风险

    def judge_risk(self, mouse_track: MouseTrack):
        # if self.direction==contants.COMBINE:
        feature_dev = mouse_track.get_feature_dev(order=self.n_order_dev, mode=self.direction)
        if self.direction == contants.COMBINE:
            arr_dev = feature_dev[self.n_order_dev - 1]
        elif self.direction == contants.X:
            arr_dev = feature_dev[self.n_order_dev - 1][:, 0]
        elif self.direction == contants.Y:
            arr_dev = feature_dev[self.n_order_dev - 1][:, 1]
        else:
            raise Exception("类型错误")

        lst_small = small_runs(arr_dev[:, 0], span=self.th_span)

        min_span = self.th_span
        for left, right in lst_small:
            if right - left + 1 < self.least_point:
                # 如果该直线上的点的个数少，则不考虑
                continue

            point1 = mouse_track.arr_trace[left, :-1]
            point2 = mouse_track.arr_trace[right, :-1]
            length = np.sum((point2 - point1) ** 2) ** 0.5
            if length < self.least_length:
                # 如果该直线的长度小，则不考虑
                continue

            a = arr_dev[left:right + 1]
            span = a.max() - a.min()
            if span < min_span:
                min_span = span

        exceed_times = self.th_span / min_span
        if exceed_times > 1.0:
            return True, exceed_times
        return False, exceed_times
