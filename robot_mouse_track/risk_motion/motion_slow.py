from robot_mouse_track.mouse_track import MouseTrack
import numpy as np
from robot_mouse_track.utils import num_runs, small_runs


class SlowMotion:
    # 鼠标跳变运动
    def __init__(self):
        self.th_slow = 10  # 超过多少毫秒的移动 算作 缓慢
        self.th_slow_rate = 0.5  # 缓慢移动的次数占比。超过该值判定为风险

    def judge_risk(self, mouse_track: MouseTrack):
        feature_diff_time = mouse_track.get_feature_diff_time()

        num_slow = np.sum(feature_diff_time > self.th_slow)
        rate = num_slow / len(feature_diff_time)

        exceed_times = rate / self.th_slow_rate
        if exceed_times > 1.0:
            return True, exceed_times
        return False, exceed_times
