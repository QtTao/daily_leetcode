# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/5 00:11
# filename    : solution.py
# description : LC 137 只出现一次的数字II

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        rv = 0
        for i in range(32):
            # i 是 32 位的其中一位
            # num >> i & 1 取右移 i 位后的 0 或 1，然后加和
            total = sum((num >> i) & 1 for num in nums)
            # 对 3 取余，就是只出现一次的数字的第 i 个二进制位
            if total % 3:
                if i == 31:
                    # Python 对最高位进行特殊判断
                    rv -= (1 << i)
                else:
                    # 按位或运算
                    rv |= (1 << i)
        return rv
