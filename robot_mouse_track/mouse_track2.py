# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
# from robot_mouse_track import contants
import contants
# -*- coding: utf-8 -*-

'''Google注释风格111

详情见 `Google注释风格指南`_

.. _Google注释风格指南:
   https://google.github.io/styleguide/pyguide.html
'''


class GoogleStyle:
    '''Google注释风格

    用 ``缩进`` 分隔，
    适用于倾向水平，短而简单的文档

    Attributes:
        dividend (int or float): 被除数
        name (:obj:`str`, optional): 该类的命名
    '''

    def __init__(self, dividend, name='GoogleStyle'):
        '''初始化'''
        self.dividend = dividend
        self.name = name

    def divide(self, divisor):
        '''除法

        Google注释风格的函数，
        类型主要有Args、Returns、Raises、Examples

        Args:
            divisor (int):除数

        Returns:
            除法结果

        Raises:
            ZeroDivisionError: division by zero

        Examples:
            >>> google = GoogleStyle(divisor=10)
            >>> google.divide(10)
            1.0

        References:
            除法_百度百科  https://baike.baidu.com/item/%E9%99%A4%E6%B3%95/6280598
        '''
        try:
            return self.dividend / divisor
        except ZeroDivisionError as e:
            return e



# -*- coding: utf-8 -*-

"""NumPy注释风格

详情见 `NumPy注释风格指南`_

.. _NumPy注释风格指南:
   https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard
"""


class NumpyStyle:
    '''Numpy注释风格

    用 ``下划线`` 分隔，
    适用于倾向垂直，长而深的文档

    Attributes
    ----------
    multiplicand : int
        被乘数
    name : :obj:`str`, optional
        该类的命名
    '''

    def __init__(self, multiplicand, name='NumpyStyle'):
        '''初始化'''
        self.multiplicand = multiplicand
        self.name = name

    def multiply(self, multiplicator):
        '''乘法

        Numpy注释风格的函数，
        类型主要有Parameters、Returns

        Parameters
        ----------
        multiplicator :
            乘数

        Returns
        -------
        int
            乘法结果

        Examples
        --------
        >>> numpy = NumpyStyle(multiplicand=10)
        >>> numpy.multiply(10)
        100
        '''
        try:
            if isinstance(multiplicator, str):
                raise TypeError('Division by str')
            else:
                return self.multiplicand * multiplicator
        except TypeError as e:
            return e


# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
# from robot_mouse_track import contants
import contants


class MouseTrack:
    '''MouseTrack注释风格

        用 ``下划线`` 分隔，
        适用于倾向垂直，长而深的文档

        Attributes
        ----------
        arr_trace : int
            被乘数
        arr_trace : :obj:`str`, optional
            该类的命名
        '''
    def __init__(self, trace):
        self.arr_trace = np.array(trace, np.float64)
        self.arr_time = self.arr_trace[:, -1]

        self.max_duration_silent = 20  # 间隔超过多少秒，算静止，将长间隔缩短为一个固定长度

        self.max_DOA_tan = 100  # 正切值峰值截断
        self.max_DOA_point = 5  # 两个点计算角度的时候，采用的是 arr[i] 和 arr[i+max_DOA_point]，太近的话，误差较大

        self.feature_dev_combine = []
        self.feature_dev_decomposition = []
        self.feature_DOA = []
        self.feature_diff_time = None

    def get_feature_diff_time(self):
        if self.feature_diff_time:
            return self.feature_diff_time

        self.feature_diff_time = self.arr_trace[1:, -1] - self.arr_trace[:-1, -1]
        return self.feature_diff_time

    def get_feature_dev(self, order=2, mode=contants.COMBINE):
        """
        获取导数特征
        :param order: 求导阶数
        :return:list
        """
        if mode == contants.COMBINE:
            feature_dev = self.feature_dev_combine
        elif mode == contants.DECOMPOSITION:
            feature_dev = self.feature_dev_decomposition
        else:
            raise Exception("请输入正确的类型")

        if len(feature_dev) >= order:
            return feature_dev

        if not feature_dev:  # 如果求导阶数不够，则增量计算缺的阶数
            self._arr_diff_dis = self.arr_trace[1:, :] - self.arr_trace[:-1, :]
            self._arr_diff_time = np.clip(self._arr_diff_dis[:, -1:], 0, self.max_duration_silent)
            if mode == contants.COMBINE:
                self._arr_diff_dis = (np.sum((self._arr_diff_dis[:, :-1] ** 2), axis=1) ** 0.5)[:, np.newaxis]
            else:
                self._arr_diff_dis = self._arr_diff_dis[:, :-1]
            order_cur = 0
        else:
            order_cur = len(feature_dev)

        while 1:
            arr_dev = self._arr_diff_dis / self._arr_diff_time[:len(self._arr_diff_dis)]
            # arr = np.c_[arr_dev, self.arr_trace[:len(arr_dev), -1]]
            feature_dev.append(arr_dev)
            order_cur += 1
            if order_cur >= order:
                break
            self._arr_diff_dis = arr_dev[1:] - arr_dev[:-1]

        return feature_dev

    def show_track(self):
        fig, ax = plt.subplots(1, 1)
        ax.invert_yaxis()
        plt.plot(self.arr_trace[:, 0], self.arr_trace[:, 1], ".")  #
        ax.set_xlim((-100, 1920))
        ax.set_ylim((1280, -100))
        plt.title("trace xy")
        plt.show()

    def get_feature_DOA(self):
        """
        计算方向角变化
        :return:
        """
        if self.feature_DOA:
            return self.feature_DOA

        arr_diff_dis = self.arr_trace[self.max_DOA_point:, :-1] - self.arr_trace[:-self.max_DOA_point, :-1]
        # 防止除以0
        arr_diff_dis[:, 0][np.where(arr_diff_dis[:, 0] == 0)] = 10e-8

        self.feature_DOA = np.clip(arr_diff_dis[:, 1] / arr_diff_dis[:, 0], -self.max_DOA_tan, self.max_DOA_tan)
        self.feature_DOA = np.arctan(self.feature_DOA) * 180 / np.pi
        return self.feature_DOA


if __name__ == '__main__':
    from examples import trace_example

    mt = MouseTrack(trace_example.trace1)
    x = mt.get_feature_dev(order=1, mode=contants.COMBINE)
    y = mt.get_feature_dev(order=2, mode=contants.COMBINE)
    print(x)
    print(y)
