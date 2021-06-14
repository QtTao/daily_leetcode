# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/6/14 15:37
# filename    : solution.py
# description : LC 12 整数转罗马数字

from collections import OrderedDict


class Solution:
    MAPPING = OrderedDict({
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    })

    def intToRoman(self, num: int) -> str:
        """ 数学 """
        ans = ''
        for value, roman in self.MAPPING.items():
            if count := num // value:
                ans += (roman * count)
                num %= value
        return ans
