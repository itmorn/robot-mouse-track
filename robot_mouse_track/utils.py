import numpy as np


def num_runs(arr, num=0):
    """
    获取ndarray中连续为0的开始结束索引，[a, b)
    :param arr:
    :return:
    """
    # Create an array that is 1 where a is 0, and pad each end with an extra 0.
    is_zero = np.concatenate(([0], np.equal(arr, num).view(np.int8), [0]))
    absdiff = np.abs(np.diff(is_zero))
    # Runs start and end where absdiff is 1.
    ranges = np.where(absdiff == 1)[0].reshape(-1, 2)
    return ranges


def small_runs(arr, span=5):
    """
    获取ndarray中连续变化幅度较小的开始结束索引，[a, b]
    :param arr:
    :param span: 容差多少度
    :return:
    """
    # Create an array that is 1 where a is 0, and pad each end with an extra 0.
    arr_diff = np.abs(np.diff(arr))
    is_small = np.concatenate(([0], (arr_diff < span).view(np.int8), [0]))
    abs_diff = np.abs(np.diff(is_small))
    # Runs start and end where absdiff is 1.
    ranges = np.where(abs_diff == 1)[0].reshape(-1, 2)
    return ranges


if __name__ == '__main__':
    a = [1, 2, 3, 0, 0, 0, 0, 0, 0, 4, 25, 9, 0, 0, 0, 0, 9, 8, 7, 0, 5, 5]
    runs = num_runs(a, num=0)
    print(runs)
    a = [89.99, 89.98, 90.01, 0, 0, 4, 25.7, 25.6, 25.8, 0, 0, 0, 9, 8, 7, 0, 5, 5]
    # a = [89.8, 89.91, 90.2, 0, 5, 5]
    runs = small_runs(a, span=1)
    print(runs)
