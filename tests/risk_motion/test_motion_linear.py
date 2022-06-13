"""
@Auth: itmorn
@Date: 2022/6/13-20:26
@Email: 12567148@qq.com
"""
from examples.trace_examples import trace_itmorn, trace_selenium_jump, trace_answer_unlock
from robot_mouse_track.mouse_track import MouseTrack
from robot_mouse_track.risk_motion.motion_jump import JumpMotion
from robot_mouse_track.risk_motion.motion_vertical_horizontal_linear import VerticalHorizontalLinearMotion
from robot_mouse_track.risk_motion.motion_linear import LinearMotion
from robot_mouse_track.risk_motion.motion_constant_velocity import ConstantVelocityMotion
from robot_mouse_track.risk_motion.motion_slow import SlowMotion
from robot_mouse_track.risk_motion.motion_similar import SimilarMotion, calc_vec


def test_judge_risk():
    mouse_track = MouseTrack(trace_itmorn)
    # mouse_track.show_track()
    rule_mouse_jump = LinearMotion()
    flag, exceed_times = rule_mouse_jump.judge_risk(mouse_track)
    print(flag, "LinearMotion", exceed_times)

    rule_mouse_jump = LinearMotion()
    rule_mouse_jump.least_point = 1  # 这条线上至少有多少个点
    rule_mouse_jump.th_length = 1  # 斜线运动长度超过多少，认为是风险，单位px
    flag, exceed_times = rule_mouse_jump.judge_risk(mouse_track)
    print(flag, "LinearMotion", exceed_times)
