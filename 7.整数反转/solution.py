# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/22 11:35
# filename    : solution.py
# description : LC 7 整数反转

class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT, MAX_INT = -2 ** 31, 2 ** 31 - 1

        rv = 0
        while x != 0:
            # 当 rv < -214748364 或者 rv > 214748364，已超出题目指定的范围
            # 由于 x 本身在 [MIN_INT, MAX_INT] 的限制，最高位只能是 0，1，2，-1 或者 -2，
            # 所以当 rv = 214748364 或者 -214748364，肯定不会超出范围
            if rv < MIN_INT // 10 + 1 or rv > MAX_INT // 10:
                return 0
            digit = x % 10
            # 当 x 为负数，digit 在 [0, 9) 范围内，比如 -2^31 % 10 返回 2，2 - 10 = -8 才是正确的末位数
            # 当 x 为整数，digit 直接返回不用处理，比如 2^31 % 10 返回 8
            if x < 0 < digit:
                digit -= 10
            # 当 x 为负数，比如 -2^31，-214748364 = (-2^31 - -8) // 10
            # 当 x 为正数，比如
            x = (x - digit) // 10
            rv = rv * 10 + digit
        return rv
