from examples.trace_example import trace1
from robot_mouse_track.mouse_track import MouseTrack, COMBINE
from robot_mouse_track.rules import *
import matplotlib.pyplot as plt

if __name__ == '__main__':
    mouse_track = MouseTrack(trace1)
    mouse_track.show_track()

    # lst_feature = mouse_track.get_feature_dev(order=2, mode=COMBINE)  # DECOMPOSITION
    # for arr_feature in lst_feature:
    #     plt.figure()
    #     plt.plot(mouse_track.arr_time[:len(arr_feature)], arr_feature[:, 0])
    #     plt.show()

    # arr_DOA = mta.get_feature_DOA()
    # plt.figure(figsize=(10, 10))
    # # plt.plot(mta.arr_time[:100], arr_DOA[:100])
    # plt.plot(mta.arr_time[:len(arr_DOA)], arr_DOA)
    # print(arr_DOA)
    # plt.show()

    # rule_mouse_jump = JumpMotion()
    # rule_mouse_jump.judge_risk(mouse_track)
    # rule_mouse_jump = VerticalHorizontalLinearMotion()
    # rule_mouse_jump.judge_risk(mouse_track)
    rule_mouse_jump = LinearMotion()
    rule_mouse_jump.judge_risk(mouse_track)
