# -*- coding: utf-8 -*-
# Python2.7

def fibonacci_iterative_memorization(n):
    """
    将已计算实例的结果制表备查
    :param n:
    :return:
    """
    f = []
    for i in range(n + 1):
        if i <= 1:
            f.append(1)
        else:
            f.append(f[i - 1] + f[i - 2])
    return f[n]


def fibonacci_recursive(n):
    """
    递归方法：自顶而下递归，产生大量重复计算实例
    :param n:
    :return:
    """
    if n <= 1:
        return 1
    else:
        return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)


def fibonacci_iterative_dynamic_programming(n):
    """
    颠倒计算方向，自底而上迭代
    :param n:
    :return:
    """
    f = 0
    g = 1
    while n > 0:
        g = g + f  # 只需要O(n)的时间，和O(1)的空间！ 最优
        f = g - f
        n -= 1
    return g
