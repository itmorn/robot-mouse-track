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
