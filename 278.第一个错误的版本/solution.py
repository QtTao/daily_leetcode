# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/18 01:10
# filename    : solution.py
# description : LC 278 第一个错误的版本


class Solution:
    def firstBadVersion(self, n):
        """ 二分查找 """
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
