from robot_mouse_track import contants
from robot_mouse_track.mouse_track import MouseTrack
import numpy as np
from robot_mouse_track.utils import num_runs, small_runs


class LinearMotion:
    """
    斜直线运动（人手可能会画出横/竖直线，但是画不出来斜直线）

    :var int default=5 least_point: 这条线上至少有多少个点
    :var int default=100 th_length: 斜线运动长度超过多少，认为是风险，单位px
    """

    def __init__(self):
        self.least_point = 5  # 这条线上至少有多少个点
        self.th_length = 100  # 斜线运动长度超过多少，认为是风险，单位px

    def judge_risk(self, mouse_track: MouseTrack):
        """
        风险判定

        :param MouseTrack mouse_track: 鼠标轨迹对象
        :return: (have_risk, risk_level)
        :rtype: (bool, float)
        """

        # n个点算斜率，斜率相近表示平行
        feature_DOA = mouse_track.get_feature_DOA()

        # 斜率变化幅度较小则认为是斜线
        # 获取斜率变化幅度较小的片段的左右闭区间
        lst_small = small_runs(feature_DOA, span=1)
        max_length = 0
        for left, right in lst_small:
            if right - left + 1 < self.least_point:
                # 如果该直线上的点的个数少，则不考虑
                continue
            point1 = mouse_track.arr_trace[left, :-1]
            point2 = mouse_track.arr_trace[right, :-1]
            length = np.sum((point2 - point1) ** 2) ** 0.5
            if length < self.th_length:
                # 如果该直线的长度小，则不考虑
                continue
            if length > max_length:  # 获取该轨迹中最长的直线长度
                max_length = length

        exceed_times_length = max_length / self.th_length
        if exceed_times_length > 1.0:
            return True, exceed_times_length
        return False, exceed_times_length
