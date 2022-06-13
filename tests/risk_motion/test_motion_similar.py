"""
@Auth: itmorn
@Date: 2022/6/13-20:27
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
    lst_vec_bank = []
    mouse_track1 = MouseTrack(trace_itmorn)
    vec1 = calc_vec(mouse_track1)
    lst_vec_bank.append(vec1)

    mouse_track2 = MouseTrack(trace_answer_unlock)
    vec_now = calc_vec(mouse_track2)

    rule_mouse = SimilarMotion()
    flag, exceed_times = rule_mouse.judge_risk(vec=vec_now, lst_vec_bank=lst_vec_bank)
    print(flag, "SimilarMotion", exceed_times)

    rule_mouse = SimilarMotion()
    flag, exceed_times = rule_mouse.judge_risk(vec=vec1, lst_vec_bank=lst_vec_bank)
    print(flag, "SimilarMotion", exceed_times)
