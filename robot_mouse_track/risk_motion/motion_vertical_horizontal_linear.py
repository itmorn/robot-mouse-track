import numpy as np
from robot_mouse_track.utils import num_runs, small_runs
from robot_mouse_track.mouse_track import MouseTrack
from robot_mouse_track import contants


class VerticalHorizontalLinearMotion:
    # 横/竖直线运动（人手可能会画出横/竖直线，但是很难画出非常长的横/竖直线）
    def __init__(self):
        self.least_point = 10  # 这条线上至少有多少个点

        self.th_length_x = 500  # 横向直线运动长度超过多少，认为是风险，单位px
        self.th_length_y = 500  # 纵向直线运动长度超过多少，认为是风险，单位px

    def judge_risk(self, mouse_track: MouseTrack):
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
