"""
@Auth: itmorn
@Date: 2022/6/10-20:15
@Email: 12567148@qq.com
"""

from robot_mouse_track.mouse_track import MouseTrack
import numpy as np


def calc_vec(mouse_track: MouseTrack, len_x=1920, len_y=1280, bin_split_nx=4, bin_split_ny=4):
    """
    计算鼠标轨迹的特征向量

    :param MouseTrack mouse_track: 鼠标轨迹对象
    :param int default=1920 len_x: 屏幕横向的像素点个数
    :param int default=1280 len_y: 屏幕纵向的像素点个数
    :param int default=4 bin_split_nx: 屏幕横向的像素点 分成几个等宽的桶（可以提升鲁棒性，但不能太大，太大就会损失精确性）
    :param int default=4 bin_split_ny: 屏幕纵向的像素点 分成几个等宽的桶（可以提升鲁棒性，但不能太大，太大就会损失精确性）
    :return: 特征向量
    :rtype: ndarray ``shape=(1,len_x/bin_split_nx+len_y/bin_split_ny)``
    """
    hist_x, _ = np.histogram(mouse_track.arr_trace[:, 0], bins=len_x // bin_split_nx,
                             range=(0, len_x), density=True)
    hist_y, _ = np.histogram(mouse_track.arr_trace[:, 1], bins=len_y // bin_split_ny,
                             range=(0, len_y), density=True)
    return np.r_[hist_x, hist_y]


class SimilarMotion:
    """
    路径重复的运动（防止一些未知的鼠标录制软件可以躲过以上防御，这里可以加最后一层防御）

    :var float default=0.001 th_score_diff: 差异阈值，低于这个值，则认为是风险
    """

    def __init__(self):
        self.th_score_diff = 0.001

    def judge_risk(self, vec, lst_vec_bank):
        """
        风险判定

        :param ndarray vec: 鼠标轨迹的特征向量
        :param list[ndarray] lst_vec_bank: 鼠标轨迹的特征向量列表，实践中可以为每个用户维护了一个向量池，防止用户使用多段录像交替攻击
        :return: (have_risk, risk_level)
        :rtype: (bool, float)
        """
        arr_vec_bank = np.array(lst_vec_bank)
        arr_res = np.sum((arr_vec_bank - vec) ** 2, axis=1)
        min_score = min(arr_res)
        if min_score == 0:
            min_score = 0.000001
        exceed_times = self.th_score_diff / min_score
        if exceed_times > 1:
            return True, exceed_times
        return False, exceed_times
