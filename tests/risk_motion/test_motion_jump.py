"""
@Auth: itmorn
@Date: 2022/6/13-20:25
@Email: 12567148@qq.com
"""
from examples.trace_examples import trace_itmorn
from robot_mouse_track.mouse_track import MouseTrack
from robot_mouse_track.risk_motion.motion_jump import JumpMotion


def test_judge_risk():
    mouse_track = MouseTrack(trace_itmorn)
    # mouse_track.show_track()
    rule_mouse_jump = JumpMotion(th_velocity=20, th_acceleration=1.4)
    flag, (exceed_times_velocity, exceed_times_acceleration) = rule_mouse_jump.judge_risk(mouse_track)
    print(flag, "JumpMotion", exceed_times_velocity, exceed_times_acceleration)

    rule_mouse_jump = JumpMotion(th_velocity=1, th_acceleration=0.1)
    flag, (exceed_times_velocity, exceed_times_acceleration) = rule_mouse_jump.judge_risk(mouse_track)
    print(flag, "JumpMotion", exceed_times_velocity, exceed_times_acceleration)
