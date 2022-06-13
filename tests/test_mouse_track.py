"""
@Auth: itmorn
@Date: 2022/6/11-16:52
@Email: 12567148@qq.com
"""
from robot_mouse_track import contants
from examples.trace_examples import trace_itmorn
from robot_mouse_track.mouse_track import MouseTrack
import numpy as np

def test_get_feature_diff_time():
    ma = MouseTrack(trace_itmorn)
    feature_diff_time = ma.get_feature_diff_time()
    feature_diff_time2 = ma.get_feature_diff_time()

    assert isinstance(feature_diff_time2, np.ndarray)


def test_get_feature_dev():
    ma = MouseTrack(trace_itmorn)
    feature_diff_time = ma.get_feature_dev()

    assert isinstance(feature_diff_time, list)

    ma = MouseTrack(trace_itmorn)
    feature_diff_time = ma.get_feature_dev(order=1,mode=contants.DECOMPOSITION)
    feature_diff_time = ma.get_feature_dev(order=2,mode=contants.DECOMPOSITION)
    feature_diff_time = ma.get_feature_dev(order=2,mode=contants.DECOMPOSITION)

    assert isinstance(feature_diff_time, list)

    try:
        feature_diff_time = ma.get_feature_dev(order=2, mode="xxx")
    except Exception as e:
        assert "请输入正确的类型" in e.args[0]



def test_show_track():
    ma = MouseTrack(trace_itmorn)
    ma.show_track()


def test_get_feature_doa():
    ma = MouseTrack(trace_itmorn)
    feature_doa = ma.get_feature_doa()
    feature_doa = ma.get_feature_doa()

    assert isinstance(feature_doa, np.ndarray)
