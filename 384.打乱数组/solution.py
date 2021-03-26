# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/25 16:55
# filename    : solution.py
# description : LC 384 打乱数组

import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.nums_ori = nums[:]

    def reset(self) -> List[int]:
        """ 返回初始状态 """
        # 如果使用 Inside-Out 洗牌算法，不需要重新赋值，直接返回即可
        self.nums = self.nums_ori[:]
        return self.nums

    def shuffle(self) -> List[int]:
        """ 返回打乱后的数组 """
        tmp_nums = self.nums[:]
        for idx in range(self.n):
            delete_idx = random.randrange(len(tmp_nums))
            # 弹出对应下标的元素，直接填充至原数组
            self.nums[idx] = tmp_nums.pop(delete_idx)
        return self.nums

    def shuffleFisherYates(self) -> List[int]:
        """ Fisher-Yates 原地修改 """
        for idx in range(self.n):
            # 从剩余下标 [idx, n) 中随机选择
            swap_idx = random.randrange(idx, self.n)
            # 交换位置
            self.nums[idx], self.nums[swap_idx] = self.nums[swap_idx], self.nums[idx]
        return self.nums

    def shuffleInsideOut(self) -> List[int]:
        """ Inside-Out 不原地修改 """
        tmp_nums = self.nums[:]
        for idx in range(self.n):
            # 在 [0, idx] 中随机选择下标与当前元素进行交换
            swap_idx = random.randint(0, idx)
            tmp_nums[idx] = tmp_nums[swap_idx]
            # 借助原数组来实现元素交换，不污染原数组
            tmp_nums[swap_idx] = self.nums[idx]
        return tmp_nums
