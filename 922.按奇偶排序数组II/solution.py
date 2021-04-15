# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/15 09:49
# filename    : solution.py
# description : LC 922 按奇偶排序数组II

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """ 双指针 """
        odd_idx = 1
        for even_idx in range(0, len(nums), 2):
            # 当偶数指针指向奇数后，寻找奇数指针对应的偶数，并交换位置
            if nums[even_idx] % 2:
                # 奇数指针向前移动，直至遇到偶数
                while nums[odd_idx] % 2:
                    odd_idx += 2
                # 交换位置
                nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
        return nums
