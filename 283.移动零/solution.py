# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/20 23:18
# filename    : solution.py
# description : LC 283 移动零

class Solution:
    def moveZeroes1(self, nums: List[int]) -> None:
        """ 直接填充 """
        j = 0
        n = len(nums)
        for i in range(n):
            if nums[i]:
                nums[j] = nums[i]
                j += 1
        for i in range(j, n):
            nums[i] = 0

    def moveZeros2(self, nums: List[int]) -> None:
        """双指针
        一个指针用于遍历数组
        另一个指针用于指向数组中的 0
        """
        j = 0
        for i in range(len(nums)):
            if not nums[i]:
                continue
            # 保证 j 的左边均不为 0
            # 当 i 对应的数字不为 0，那么可以将 i 对应的数值赋值到 j 位置
            # 然后 i 直接赋值为 0
            if i > j:
                nums[j] = nums[i]
                nums[i] = 0
            # 如果 i = j，且 nums[i] 不为 0，j += 1
            j += 1
