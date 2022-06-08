# class RuleBase:
#     def __init__(self):
#         self.score = 0
from robot_mouse_track.mouse_track import MouseTrack, COMBINE
import numpy as np


class RuleMouseJump():
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
