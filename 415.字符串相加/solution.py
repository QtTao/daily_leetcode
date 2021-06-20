# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/6/20 21:50
# filename    : solution.py
# description : LC 415 字符串相加

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """ 模拟竖式加法 """
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        ans = ''
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            num = n1 + n2 + carry
            # 计算进位 carry
            carry = num // 10
            # 将余数放在 ans 的前面
            ans = str(num % 10) + ans
            i -= 1
            j -= 1
        # 这里注意判断是否还有进位 1，比如 '1' + '9' = '10'
        return '1' + ans if carry else ans
