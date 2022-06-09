from robot_mouse_track.mouse_track import MouseTrack
import numpy as np
from robot_mouse_track.utils import num_runs, small_runs
from robot_mouse_track import contants


def calc_vec(mouse_track: MouseTrack, len_x=1920, len_y=1280, bin_split_nx=4, bin_split_ny=4):
    hist_x, _ = np.histogram(mouse_track.arr_trace[:, 0], bins=len_x // bin_split_nx,
                             range=(0, len_x), density=True)
    hist_y, _ = np.histogram(mouse_track.arr_trace[:, 1], bins=len_y // bin_split_ny,
                             range=(0, len_y), density=True)
    return np.r_[hist_x, hist_y]


class SimilarMotion:
    def __init__(self):
        self.th_score_diff = 0.001  # 差异阈值，低于这个值，则认为是风险

    def judge_risk(self, vec, lst_vec_bank):
        arr_vec_bank = np.array(lst_vec_bank)
        arr_res = np.sum((arr_vec_bank - vec) ** 2, axis=1)
        min_score = min(arr_res)
        if min_score == 0:
            min_score = 0.000001
        exceed_times = self.th_score_diff / min_score
        if exceed_times > 1:
            return True, exceed_times
        return False, exceed_times
