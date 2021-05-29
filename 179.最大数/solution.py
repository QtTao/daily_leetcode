# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/29 11:10
# filename    : solution.py
# description : LC 179 最大数

import math
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """ 比较 """
        def compare(x, y):
            """ 比较函数，从大到小排序 """
            # 这里设计得很巧妙，将两个数字字符串拼接，再进行比较
            # 如 nums = ['3', '30']，'3' + '30' > '30' + '3
            if y + x > x + y:
                return 1
            return -1
        nums = sorted(map(str, nums), key=cmp_to_key(compare))
        # 从大到小排序后，第一位是 '0'，直接返回 '0'
        if nums[0] == '0':
            return '0'
        # 返回拼接结果
        return ''.join(nums)

    def largestNumberMath(self, nums: List[int]) -> str:
        """ 数学 """
        def func(x):
            if not x:
                return 0
            n = int(math.log10(x)) + 1
            # 将数组元素转换为 x / (10^n - 1)
            return x / (10 ** n - 1)
        nums.sort(key=func, reverse=True)
        if not nums[0]:
            return '0'
        return ''.join(map(str, nums))
