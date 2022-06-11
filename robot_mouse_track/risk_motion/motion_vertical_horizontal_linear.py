"""
@Auth: itmorn
@Date: 2022/6/10-20:15
@Email: 12567148@qq.com
"""
import numpy as np
from robot_mouse_track.utils import num_runs
from robot_mouse_track.mouse_track import MouseTrack


class VerticalHorizontalLinearMotion:
    """
    横/竖直线运动（人手可能会画出横/竖直线，但是很难画出非常长的横/竖直线）

    :var int default=10 least_point: 这条线上至少有多少个点
    :var int default=500 th_length_x: 横向直线运动长度超过多少，认为是风险，单位px
    :var int default=500 th_length_y: 纵向直线运动长度超过多少，认为是风险，单位px
    """

    def __init__(self):
        self.least_point = 10

        self.th_length_x = 500
        self.th_length_y = 500

    def judge_risk(self, mouse_track: MouseTrack):
        """
        风险判定

        :param MouseTrack mouse_track: 鼠标轨迹对象
        :return: (have_risk, x_risk_level, y_risk_level)
        :rtype: (bool, float, float)
        """
        arr_trace_x = mouse_track.arr_trace[:, 0]
        arr_trace_y = mouse_track.arr_trace[:, 1]
        arr_diff = mouse_track.arr_trace[1:, :-1] - mouse_track.arr_trace[:-1, :-1]
        arr_diff_x = arr_diff[:, 0]
        arr_diff_y = arr_diff[:, 1]
        lst_x_is_0 = num_runs(arr_diff_x)
        lst_y_is_0 = num_runs(arr_diff_y)
        lst_x_is_0 = [i for i in lst_x_is_0 if i[-1] - i[0] >= self.least_point]
        lst_y_is_0 = [i for i in lst_y_is_0 if i[-1] - i[0] >= self.least_point]

        max_length_y = 0
        for y_start, y_end in lst_x_is_0:
            arr = arr_trace_y[y_start:y_end + 1]
            length = np.max(arr) - np.min(arr)
            if length > max_length_y:
                max_length_y = length

        max_length_x = 0
        for x_start, x_end in lst_y_is_0:
            arr = arr_trace_x[x_start:x_end + 1]
            length = np.max(arr) - np.min(arr)
            if length > max_length_x:
                max_length_x = length

        exceed_times_x = max_length_x / self.th_length_x
        exceed_times_y = max_length_y / self.th_length_y
        if exceed_times_x > 1.0 or exceed_times_y > 1.0:
            return True, (exceed_times_x, exceed_times_y)
        return False, (exceed_times_x, exceed_times_y)
