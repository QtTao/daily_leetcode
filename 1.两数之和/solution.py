# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/16 00:35
# filename    : solution.py
# description : LC 1 两数之和

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ 哈希表 """
        # 哈希表用于记录每个数字出现的下标
        hashmap = {}
        for idx, num in enumerate(nums):
            rest = target - num
            # 判断 rest 是否存在哈希表中，如果存在返回其下标，与当前下标构成两数之和
            if rest in hashmap:
                return [idx, hashmap[rest]]
            # 否则记录当前数字的下标
            hashmap[num] = idx

    def twoSumSorted(self, nums: List[int], target: int) -> List[int]:
        """ 排序 + 双指针 """
        # 对 nums 进行排序，同时记录各个数字在原始数组的下标
        sorted_num = sorted((num, idx) for idx, num in enumerate(nums))
        left, right = 0, len(nums) - 1
        # 首尾指针向中间移动
        while left < right:
            two_sum = sorted_num[left][0] + sorted_num[right][0]
            # Case 1 如果双指针分别指向的数字之和等于 target，返回它们在原始数组的下标
            if two_sum == target:
                return [sorted_num[left][1], sorted_num[right][1]]
            # Case 2 如果两数之和小于 target，左指针右移一位
            elif two_sum < target:
                left += 1
            # Case 3 如果两束之和大于 target，右指针左移一位
            else:
                right -= 1
