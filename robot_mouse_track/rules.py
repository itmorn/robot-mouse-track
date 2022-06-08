# class RuleBase:
#     def __init__(self):
#         self.score = 0
from robot_mouse_track.mouse_track import MouseTrack, COMBINE, DECOMPOSITION
import numpy as np
from robot_mouse_track.utils import num_runs, small_runs


class JumpMotion:
    # 鼠标跳变运动
    def __init__(self):
        self.max_velocity = 20  # 每毫秒移动的像素个数
        self.max_acceleration = 1.4  # 每毫秒的加速度

    def judge_risk(self, mouse_track: MouseTrack):
        feature_dev = mouse_track.get_feature_dev(order=2, mode=COMBINE)
        arr_velocity = feature_dev[0]
        arr_acceleration = feature_dev[1]

        exceed_times_velocity = np.max(arr_velocity) / self.max_velocity
        exceed_times_acceleration = np.max(arr_acceleration) / self.max_acceleration
        if exceed_times_velocity > 1.0 or exceed_times_acceleration > 1.0:
            return True, (exceed_times_velocity, exceed_times_acceleration)
        return False, (exceed_times_velocity, exceed_times_acceleration)


class VerticalHorizontalLinearMotion:
    # 横/竖直线运动（人手可能会画出横/竖直线，但是很难画出非常长的横/竖直线）
    def __init__(self):
        self.max_length_x = 500  # 横向直线运动的最大长度，单位px
        self.max_length_y = 500  # 纵向直线运动的最大长度，单位px
        self.max_point = 10  # 这条线上至少有多少个点

    def judge_risk(self, mouse_track: MouseTrack):
        arr_trace_x = mouse_track.arr_trace[:, 0]
        arr_trace_y = mouse_track.arr_trace[:, 1]
        arr_diff = mouse_track.arr_trace[1:, :-1] - mouse_track.arr_trace[:-1, :-1]
        arr_diff_x = arr_diff[:, 0]
        arr_diff_y = arr_diff[:, 1]
        lst_x_is_0 = num_runs(arr_diff_x)
        lst_y_is_0 = num_runs(arr_diff_y)
        lst_x_is_0 = [i for i in lst_x_is_0 if i[-1] - i[0] >= self.max_point]
        lst_y_is_0 = [i for i in lst_y_is_0 if i[-1] - i[0] >= self.max_point]

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

        exceed_times_x = max_length_x / self.max_length_x
        exceed_times_y = max_length_y / self.max_length_y
        if exceed_times_x > 1.0 or exceed_times_y > 1.0:
            return True, (exceed_times_x, exceed_times_y)
        return False, (exceed_times_x, exceed_times_y)


class LinearMotion:
    # 斜直线运动（人手可能会画出横/竖直线，但是画不出来斜直线）
    def __init__(self):
        self.max_length = 100  # 斜线运动的最大长度，单位px
        self.max_point = 5  # 这条线上至少有多少个点

    def judge_risk(self, mouse_track: MouseTrack):
        # n个点算斜率，斜率相近表示平行
        feature_DOA = mouse_track.get_feature_DOA()

        # 斜率变化幅度较小则认为是斜线
        # 获取斜率变化幅度较小的片段的左右闭区间
        lst_small = small_runs(feature_DOA, span=1)
        max_length = 0
        for left, right in lst_small:
            if right - left + 1 < self.max_point:
                # 如果该直线上的点的个数少，则不考虑
                continue
            point1 = mouse_track.arr_trace[left, :-1]
            point2 = mouse_track.arr_trace[right, :-1]
            length = np.sum((point2 - point1) ** 2) ** 0.5
            if length < self.max_length:
                # 如果该直线的长度小，则不考虑
                continue
            if length > max_length:  # 获取该轨迹中最长的直线长度
                max_length = length

        exceed_times_length = max_length / self.max_length
        if exceed_times_length > 1.0:
            return True, exceed_times_length
        return False, exceed_times_length
