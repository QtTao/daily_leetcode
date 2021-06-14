# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/6/14 14:08
# filename    : solution.py
# description : LC 13 罗马数字转整数

class Solution:
    MAPPING = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        i, n = 0, len(s)
        ans = 0
        for i, ch in enumerate(s):
            num = self.MAPPING[ch]
            # 当小的数字在大的数字的左边时，根据规则减去小的数字
            if i + 1 < n and num < self.MAPPING[s[i + 1]]:
                ans -= num
            # 通常情况，小的数字在大的数字的右边，直接相加
            else:
                ans += num
        return ans
