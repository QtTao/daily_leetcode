# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/30 22:11
# filename    : solution.py
# description : LC 398 随机数索引

import random


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        """ Reservoir Sampling """
        n = 1
        ans = None
        for idx, num in enumerate(self.nums):
            if num == target:
                # 以 1 / n 的概率更新索引，(n - 1) / n 不更新索引
                # 假设一个 [0, 1) 的随机数 x，x < 1 / n 说明满足 1 / n 的概率
                if random.randrange(0, n) < 1:
                    ans = idx
                # 统计符合 num == target 的索引个数
                n += 1
        return ans
