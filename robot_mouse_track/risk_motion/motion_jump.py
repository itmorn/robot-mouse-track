"""
@Auth: itmorn
@Date: 2022/6/10-20:15
@Email: 12567148@qq.com
"""

from ..mouse_track import MouseTrack
from .. import contants
import numpy as np


class JumpMotion:
    """
    鼠标跳跃运动

    :var int default=20 th_velocity: 每毫秒移动的像素个数  超过该值，就认为是风险
    :var float default=1.4 th_acceleration: 每毫秒的加速度  超过该值，就认为是风险
    """

    def __init__(self):
        self.th_velocity = 20
        self.th_acceleration = 1.4

    def judge_risk(self, mouse_track: MouseTrack):
        """
        风险判定

        :param MouseTrack mouse_track: 鼠标轨迹对象
        :return: (have_risk, velocity_risk_level, acceleration_risk_level)
        :rtype: (bool, float, float)
        """
        feature_dev = mouse_track.get_feature_dev(order=2, mode=contants.COMBINE)
        arr_velocity = feature_dev[0]
        arr_acceleration = feature_dev[1]

        exceed_times_velocity = np.max(arr_velocity) / self.th_velocity
        exceed_times_acceleration = np.max(arr_acceleration) / self.th_acceleration
        if exceed_times_velocity > 1.0 or exceed_times_acceleration > 1.0:
            return True, (exceed_times_velocity, exceed_times_acceleration)
        return False, (exceed_times_velocity, exceed_times_acceleration)
