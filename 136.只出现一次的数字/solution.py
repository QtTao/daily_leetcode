# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/5 00:07
# filename    : solution.py
# description : LC 136 只出现一次的数字

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """ 异或运算 """
        rv = 0
        for num in nums:
            rv ^= num
        return rv

    def singleNumberWithSet(self, nums: List[int]) -> int:
        """ 集合 """
        num_set = set()
        for num in nums:
            if num not in num_set:
                num_set.add(num)
            else:
                num_set.remove(num)
        return num_set.pop()
