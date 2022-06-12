from examples.trace_examples import trace_itmorn,trace_selenium_jump
from robot_mouse_track.mouse_track import MouseTrack
from robot_mouse_track.risk_motion.motion_jump import JumpMotion
# from robot_mouse_track.risk_motion.motion_linear import LinearMotion
# from robot_mouse_track.risk_motion.motion_constant_velocity import ConstantVelocityMotion
# from robot_mouse_track.risk_motion.motion_slow import SlowMotion
from robot_mouse_track.risk_motion.motion_similar import SimilarMotion, calc_vec

# import matplotlib.pyplot as plt

if __name__ == '__main__':
    # mouse_track = MouseTrack(trace_itmorn)
    # mouse_track.show_track()
    # rule_mouse_jump = JumpMotion(th_velocity=20, th_acceleration=1.4)
    # flag, (exceed_times_velocity, exceed_times_acceleration) = rule_mouse_jump.judge_risk(mouse_track)
    # print(flag,exceed_times_velocity,exceed_times_acceleration)

    mouse_track = MouseTrack(trace_selenium_jump)
    mouse_track.show_track()
    rule_mouse_jump = JumpMotion(th_velocity=20, th_acceleration=1.4)
    flag, (exceed_times_velocity, exceed_times_acceleration) = rule_mouse_jump.judge_risk(mouse_track)
    print(flag,exceed_times_velocity,exceed_times_acceleration)


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
    # rule_mouse_jump = LinearMotion()
    # flag, exceed_times = rule_mouse_jump.judge_risk(mouse_track)
    # print(flag, exceed_times)
    #
    # rule_mouse_jump = ConstantVelocityMotion()
    # flag, exceed_times = rule_mouse_jump.judge_risk(mouse_track)
    # print(flag, exceed_times)

    # rule_mouse = SlowMotion()
    # flag, exceed_times = rule_mouse.judge_risk(mouse_track)
    # print(flag, exceed_times)
    # lst_vec_bank = []
    #
    # mouse_track1 = MouseTrack(trace1)
    # vec1 = calc_vec(mouse_track1)
    # lst_vec_bank.append(vec1)
    #
    # mouse_track2 = MouseTrack(trace2)
    # vec2 = calc_vec(mouse_track2)
    # lst_vec_bank.append(vec2)
    #
    # mouse_track3 = MouseTrack(trace3)
    # vec3 = calc_vec(mouse_track3)
    #
    # rule_mouse = SimilarMotion()
    #
    # flag, exceed_times = rule_mouse.judge_risk(vec=vec3, lst_vec_bank=lst_vec_bank)
    # print(flag, exceed_times)
