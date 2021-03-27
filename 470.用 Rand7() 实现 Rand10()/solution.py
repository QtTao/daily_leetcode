# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/26 23:47
# filename    : solution.py
# description : LC 470 用 Rand7() 实现 Rand10()


class Solution:
    def rand10(self):
        """ 拒绝采样 """
        while True:
            num = (rand7() - 1) * 7 + rand7()  # rand49
            # 舍弃 [41, 49]
            if num <= 40:
                return num % 10 + 1

    def rand10_new(self):
        """ 拒绝采样-减少舍弃数字 """
        while True:
            num = (rand7() - 1) * 7 + rand7()  # rand49
            # 回收 [41, 49]
            if num <= 40:
                return num % 10 + 1
            rand9 = num - 40  # rand9
            num = (rand9 - 1) * 7 + rand7()  # rand63
            # 回收 [61, 63]
            if num <= 60:
                return num % 10 + 1
            rand3 = num - 60  # rand3
            num = (rand3 - 1) * 7 + rand7()  # rand21
            # 舍弃 [21]
            if num <= 20:
                return num % 10 + 1
