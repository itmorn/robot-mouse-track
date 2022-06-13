from robot_mouse_track.mouse_track import MouseTrack
import numpy as np
from robot_mouse_track.utils import small_runs
from robot_mouse_track import contants


class ConstantVelocityMotion:
    """
    分速度的匀速运动
    分速度的匀变速运动
    分速度的匀变加速运动
    合速度的匀速运动
    合速度的匀变速运动
    合速度的匀变加速运动

    :var str default="combine" direction: 求导方向。 "x"：对 ``x`` 分量求导；"y"：对 ``y`` 分量求导；"combine"：对合速度 ``combine`` 求导
    :var int default=2 n_order_dev: 距离对时间的几阶导数  1阶是速度  2阶是加速度  3阶是加速度的变化速率
    :var int default=5 least_point: 最少要包含的点的个数
    :var int default=100 least_length: 最少移动的距离
    :var float default=0.01 th_span: 两点之间的最大变化幅度，低于这个值，则认为是风险
    """

    def __init__(self):
        self.direction = contants.COMBINE
        self.n_order_dev = 2
        self.least_point = 5
        self.least_length = 100
        self.th_span = 0.01

    def judge_risk(self, mouse_track: MouseTrack):
        """
        风险判定

        :param MouseTrack mouse_track: 鼠标轨迹对象
        :return: (have_risk, risk_level)
        :rtype: (bool, float)
        """
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

        min_span = 1000000
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

            if right - left + 1 >= self.least_point + 4:
                arr_part = arr_dev[left + 2:right - 2 + 1]
            elif right - left + 1 >= self.least_point + 2:
                arr_part = arr_dev[left + 1:right - 1 + 1]
            else:
                arr_part = arr_dev[left:right + 1]

            # 如果长度较大，则切头去尾（头尾可能有异常变化点），再算span
            span = arr_part.max() - arr_part.min()
            if span < min_span:
                min_span = span

        exceed_times = self.th_span / min_span
        if exceed_times > 1.0:
            return True, exceed_times
        return False, exceed_times
