# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/14 12:52
# filename    : solution.py
# description : LC 264 丑数II

import heapq


class GenUglyNum:
    """ 动态规划（三指针）"""

    def __init__(self):
        self.nums = [1]
        self.init_nums()

    def init_nums(self, n=1690):
        """ 生成 1690 个丑数 """
        i2 = i3 = i5 = 0
        for _ in range(n):
            # 取三者最小值
            ugly_num = min(self.nums[i2] * 2, self.nums[i3] * 3, self.nums[i5] * 5)
            self.nums.append(ugly_num)
            # 当前丑数等于某个丑数 2，3，5 倍，对应指针后移一位
            if ugly_num == self.nums[i2] * 2:
                i2 += 1
            if ugly_num == self.nums[i3] * 3:
                i3 += 1
            if ugly_num == self.nums[i5] * 5:
                i5 += 1


class GenUglyNumHeap:
    """ 利用最小堆记录丑数 """

    def __init__(self):
        self.nums = []
        self.heap = []
        self.factors = [2, 3, 5]
        # 集合记录丑数
        self.seen = {1}
        # 初始化最小堆
        heapq.heappush(self.heap, 1)
        self.init_nums()

    def init_nums(self, n=1690):
        """ 生成 1690 个丑数 """
        for _ in range(n):
            # 弹出堆顶
            top = heapq.heappop(self.heap)
            # 记录丑数
            self.nums.append(top)
            for ugly in (m * top for m in self.factors):
                # 当堆顶的 2 倍，3 倍 和 5 倍是新出现的丑数，入堆并加入集合
                if ugly not in self.seen:
                    self.seen.add(ugly)
                    heapq.heappush(self.heap, ugly)


class Solution:
    ugly_nums = GenUglyNum()

    # ugly_nums = GenUglyNumHeap()

    def nthUglyNumber(self, n: int) -> int:
        return self.ugly_nums.nums[n - 1]
