# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/6/27 18:38
# filename    : solution.py
# description : LC 66 加一

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """ 数学 """
        n = len(digits) - 1
        carry = 0
        # 末尾加一
        digits[n] += 1
        # 从后向前遍历
        for i in range(n, -1, -1):
            # 加上进位
            num = digits[i] + carry
            # 计算进位
            digit, carry = num % 10, num // 10
            # 原地修改数组
            digits[i] = digit
        # 数组遍历完还有进位，在数组头部加一
        if carry:
            return [1] + digits
        return digits
