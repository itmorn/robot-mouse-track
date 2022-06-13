"""
@Auth: itmorn
@Date: 2022/6/13-20:27
@Email: 12567148@qq.com
"""
from examples.trace_examples import trace_itmorn
from robot_mouse_track.mouse_track import MouseTrack
from robot_mouse_track.risk_motion.motion_slow import SlowMotion


def test_judge_risk():
    mouse_track = MouseTrack(trace_itmorn)
    # mouse_track.show_track()

    rule_mouse = SlowMotion()
    flag, exceed_times = rule_mouse.judge_risk(mouse_track)
    print(flag, "SlowMotion", exceed_times)

    rule_mouse = SlowMotion()
    rule_mouse.th_slow=5
    flag, exceed_times = rule_mouse.judge_risk(mouse_track)
    print(flag, "SlowMotion", exceed_times)


