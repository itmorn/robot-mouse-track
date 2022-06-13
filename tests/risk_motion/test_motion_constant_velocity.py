"""
@Auth: itmorn
@Date: 2022/6/13-20:25
@Email: 12567148@qq.com
"""
import pytest

from examples.trace_examples import trace_itmorn, trace_selenium_jump, trace_answer_unlock
from robot_mouse_track import contants
from robot_mouse_track.mouse_track import MouseTrack
from robot_mouse_track.risk_motion.motion_jump import JumpMotion
from robot_mouse_track.risk_motion.motion_vertical_horizontal_linear import VerticalHorizontalLinearMotion
from robot_mouse_track.risk_motion.motion_linear import LinearMotion
from robot_mouse_track.risk_motion.motion_constant_velocity import ConstantVelocityMotion
from robot_mouse_track.risk_motion.motion_slow import SlowMotion
from robot_mouse_track.risk_motion.motion_similar import SimilarMotion, calc_vec

def test_judge_risk():
    mouse_track = MouseTrack(trace_itmorn)

    rule_mouse_jump = ConstantVelocityMotion()
    rule_mouse_jump.direction=contants.X
    flag, exceed_times = rule_mouse_jump.judge_risk(mouse_track)

    rule_mouse_jump = ConstantVelocityMotion()
    rule_mouse_jump.direction = contants.Y
    flag, exceed_times = rule_mouse_jump.judge_risk(mouse_track)

    rule_mouse_jump = ConstantVelocityMotion()
    rule_mouse_jump.direction = contants.COMBINE
    flag, exceed_times = rule_mouse_jump.judge_risk(mouse_track)

    rule_mouse_jump = ConstantVelocityMotion()
    rule_mouse_jump.direction = "xx"
    try:
        flag, exceed_times = rule_mouse_jump.judge_risk(mouse_track)
    except Exception as e:
        assert "请输入正确的类型" in e.args[0]

    trace_selenium_jump = [[6, 83, 1655038106398], [6, 84, 1655038107474], [6, 85, 1655038108650], [6, 86, 1655038109698], [6, 87, 1655038110224], [6, 88, 1655038110738]]#, [345, 601, 1655038111263], [365, 601, 1655038111782], [385, 601, 1655038112307], [405, 601, 1655038112831], [425, 601, 1655038113342], [445, 601, 1655038113884], [465, 601, 1655038114396], [485, 601, 1655038114921], [505, 601, 1655038115453], [525, 601, 1655038115973], [545, 601, 1655038116500], [565, 601, 1655038117035], [585, 601, 1655038117566], [605, 601, 1655038118095], [625, 601, 1655038118635], [645, 601, 1655038119177], [15, 721, 1655038120794]]
    mouse_track = MouseTrack(trace_selenium_jump)
    rule_mouse_jump = ConstantVelocityMotion()
    rule_mouse_jump.least_length = 2
    rule_mouse_jump.least_point = 2
    rule_mouse_jump.direction = contants.COMBINE
    flag, exceed_times = rule_mouse_jump.judge_risk(mouse_track)

    trace_selenium_jump = [[6, 83, 1655038106398], [6, 84, 1655038107474], [6, 85, 1655038108650], [6, 86, 1655038109698], [6, 87, 1655038110224], [6, 88, 1655038110738]]#, [345, 601, 1655038111263], [365, 601, 1655038111782], [385, 601, 1655038112307], [405, 601, 1655038112831], [425, 601, 1655038113342], [445, 601, 1655038113884], [465, 601, 1655038114396], [485, 601, 1655038114921], [505, 601, 1655038115453], [525, 601, 1655038115973], [545, 601, 1655038116500], [565, 601, 1655038117035], [585, 601, 1655038117566], [605, 601, 1655038118095], [625, 601, 1655038118635], [645, 601, 1655038119177], [15, 721, 1655038120794]]
    mouse_track = MouseTrack(trace_selenium_jump)
    rule_mouse_jump = ConstantVelocityMotion()
    rule_mouse_jump.least_length = 3
    rule_mouse_jump.least_point = 3
    rule_mouse_jump.direction = contants.COMBINE
    flag, exceed_times = rule_mouse_jump.judge_risk(mouse_track)









