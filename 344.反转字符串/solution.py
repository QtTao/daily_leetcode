# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/16 12:48
# filename    : solution.py
# description : LC 344 反转字符串

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """ 双指针 """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return None
