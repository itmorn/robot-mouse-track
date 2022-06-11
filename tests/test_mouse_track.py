"""
@Auth: itmorn
@Date: 2022/6/11-16:52
@Email: 12567148@qq.com
"""

from tests import trace_example
from robot_mouse_track.mouse_track import MouseTrack
import numpy as np


def test_get_feature_diff_time():
    ma = MouseTrack(trace_example.trace1)
    feature_diff_time = ma.get_feature_diff_time()

    assert isinstance(feature_diff_time, np.ndarray)


def test_get_feature_dev():
    ma = MouseTrack(trace_example.trace1)
    feature_diff_time = ma.get_feature_diff_time()

    assert isinstance(feature_diff_time, np.ndarray)


def test_show_track():
    ma = MouseTrack(trace_example.trace1)
    feature_diff_time = ma.get_feature_diff_time()

    assert isinstance(feature_diff_time, np.ndarray)


def test_get_feature_doa():
    ma = MouseTrack(trace_example.trace1)
    feature_diff_time = ma.get_feature_diff_time()

    assert isinstance(feature_diff_time, np.ndarray)
