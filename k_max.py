#!/usr/bin/env python
# coding: utf-8

"""
Description: 求数组中第 k 大数
"""


def k_max(k, array):

    sorted_array = sorted(list(set(array)), reverse=True)
    print sorted_array
    k_th = sorted_array[k+1]
    return k_th


if __name__ == "__main__":


    a = [1,432,2,2,0,4,21,23,4,6,56,7,78,67]
    print k_max(3, a)

