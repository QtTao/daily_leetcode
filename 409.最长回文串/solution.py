# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/10 00:21
# filename    : solution.py
# description : LC 409 最长回文串

import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        counter = collections.Counter(s)

        for count in counter.values():
            ans += count // 2 * 2
            if ans % 2 == 0 and count % 2:
                ans += 1
        return ans
