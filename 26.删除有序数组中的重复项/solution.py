# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/6/27 15:44
# filename    : solution.py
# description : LC 26 删除有序数组中的重复项


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """ 双指针 """
        if not nums:
            return 0
        n = len(nums)
        i, j = 1, 1
        # num 为最新的排序元素
        num = nums[0]
        while i < n:
            # 若当前的元素不等于上一个已经排序元素
            if nums[i] != num:
                # 那么将它加入排序结果
                nums[j] = nums[i]
                j += 1
                # 更新最新排序元素
                num = nums[i]
            i += 1
        return j
