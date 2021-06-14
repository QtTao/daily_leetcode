# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/6/13 23:30
# filename    : solution.py
# description : LC 35 搜索插入位置

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """ 二分查找 """
        # 初始化头尾指针
        i, j = 0, len(nums) - 1
        # 注意循环中止的条件是 i > j
        while i <= j:
            # 计算中间位置的索引
            mid = (i + j) // 2
            # 如果找与目标值相同的数字，返回其下标
            if nums[mid] == target:
                return mid
            # 如果大于目标值，更新尾指针为 mid - 1
            elif nums[mid] > target:
                j = mid - 1
            # 如果小于目标值，更新头指针为 mid + 1
            else:
                i = mid + 1
        # 如果 nums 中不存在与 target 相等的数值，那么有三种情况需要考虑
        # Case 1，数组的所有数字都比 target 大，那么循环结束时，i = 0 > j = -1，返回 i
        # Case 2，数组中所有数字都比 target 小，那么循环结束时，i = len(nums) > j = len(nums) - 1，同样返回 i
        # Case 3，target 在数组内部，那么循环结束前的一轮，i == j，如果 nums[i] == nums[j] > target，j -= 1，结束循环，返回 i
        # 如果 nums[i] == nums[j] < target，i += 1，结束循环，同样返回 i，综上，i 是第一个大于等于 target 的下标
        return i

    def searchInsert2(self, nums: List[int], target: int) -> int:
        """ 官方答案，返回第一个大于等于 target 的下标 """
        n = len(nums)
        if nums[n - 1] < target:
            return n
        elif nums[0] > target:
            return 0

        left, right = 0, n - 1
        # 在区间 nums[left,...,right] 里查找第一个大于等于 target 的下标
        while left < right:
            mid = left + (right - left) // 2
            # 如果中间元素小于 target，那么可以排除 [left,...,mid] 区间的元素，故更新 left = mid + 1
            if nums[mid] < target:
                # 下一轮搜索的区间是 [mid + 1,...,right]
                left = mid + 1
            else:
                # 下一轮搜索的区间是 [left,...,mid]
                right = mid
        # 循环结束后，left == right，直接返回 left 或者 right
        return left
