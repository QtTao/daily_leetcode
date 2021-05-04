# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/4 11:21
# filename    : solution.py
# description : LC 41 缺失的第一个正数


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """ 利用数组构建哈希表 """
        n = len(nums)

        # 标记不是正数的元素为 N + 1
        for idx in range(n):
            if nums[idx] <= 0:
                nums[idx] = n + 1

        # 标记数组中在 [1, N] 范围内的元素
        # 标记方法是将 <= N 的元素对应位置设为负数
        for idx, num in enumerate(nums):
            num = abs(num)
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        # 找出第一个 > 0 的元素的下标
        for idx, num in enumerate(nums):
            if num > 0:
                return idx + 1
        # 如果数组所有元素都小于零，说明都在 [1, N] 中
        return n + 1

    def firstMissingPositiveSwap(self, nums: List[int]) -> int:
        """ 交换元素 """
        n = len(nums)
        for idx in range(n):
            # 交换元素，将 [1, N] 范围内的元素重新放置
            # 如果 `nums[idx]` 恰好 `nums[nums[idx] - 1]` 相等，进入死循环
            while 1 <= nums[idx] <= n and nums[nums[idx] - 1] != nums[idx]:
                nums[nums[idx] - 1], nums[idx] = nums[idx], nums[nums[idx] - 1]

        for idx, num in enumerate(nums):
            # 如果下标 idx + 1 不等于对应的元素值，说明这是第一个没有出现的正整数
            if idx + 1 != nums[idx]:
                return idx + 1
        return n + 1
