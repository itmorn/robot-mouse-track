from robot_mouse_track.mouse_track import MouseTrack
import numpy as np


class SlowMotion:
    """
    轨迹点间 时间间隔非常大的运动（比如pyautogui、鼠标录制软件【普通速度】）

    :var int default=15 th_slow:  超过多少毫秒的移动 算作 缓慢
    :var float default=0.5 th_length: 缓慢移动的次数占比。超过该值判定为风险
    """

    def __init__(self):
        self.th_slow = 15
        self.th_slow_rate = 0.5

    def judge_risk(self, mouse_track: MouseTrack):
        """
        风险判定

        :param MouseTrack mouse_track: 鼠标轨迹对象
        :return: (have_risk, risk_level)
        :rtype: (bool, float)
        """
        feature_diff_time = mouse_track.get_feature_diff_time()

        num_slow = np.sum(feature_diff_time > self.th_slow)
        rate = num_slow / len(feature_diff_time)

        exceed_times = rate / self.th_slow_rate
        if exceed_times > 1.0:
            return True, exceed_times
        return False, exceed_times
