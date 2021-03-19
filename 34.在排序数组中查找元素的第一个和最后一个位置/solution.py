# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/19 10:11
# filename    : solution.py
# description : LC 34 在排序数组中查找元素的第一个和最后一个位置


class Solution:
    def searchRangeHeadTail(self, nums: List[int], target: int) -> List[int]:
        """ 双指针（头尾指针） """
        if not nums:
            return [-1, -1]
        start, end = 0, len(nums) - 1
        while start <= end:
            # 当 start 和 end 的位置均与目标值相同
            if nums[start] == target and nums[end] == target:
                return [start, end]
            # 下一个搜索区间 [start + 1, end]
            if nums[start] < target:
                start += 1
            # 下一个搜索区间 [start, end - 1]
            if nums[end] > target:
                end -= 1
        # 若没有找到目标值，直接范围 [-1, -1]
        return [-1, -1]

    def _find_left_border(self, nums: List[int], target: int) -> int:
        """ 搜索元素在数组中第一个位置 """
        start, end = 0, len(nums) - 1
        # 注意循环结束条件是 start = end
        while start < end:
            # 计算中间位置
            mid = (start + end) // 2
            # 下一个搜索区间 [mid + 1, end]
            if nums[mid] < target:
                start = mid + 1
            # 下一个搜索区间 [start, mid]
            elif nums[mid] == target:
                end = mid
            else:
                # 下一个搜索区间 [start, mid - 1]
                end = mid - 1
        # 循环体结束后，start = end，这时判断当前位置是否与目标值相同
        if nums[start] == target:
            return start
        # 不一致返回 -1
        return -1

    def _find_right_border(self, nums: List[int], target: int) -> int:
        """ 搜索元素在数组中最后一个位置 """
        start, end = 0, len(nums) - 1
        while start < end:
            # 计算中间位置
            # 注意处理比较特别，需要向上取整，否则会进入死循环
            mid = (start + end + 1) // 2
            # 下一个搜索区间 [mid + 1, end]
            if nums[mid] > target:
                end = mid - 1
            # 下一个搜索区间 [mid, end]
            elif nums[mid] == target:
                start = mid
            else:
                # 下一个搜索区间 [start, mid - 1]
                start = mid + 1
        # 由于 _find_left_border 先执行，保证了目标值一定在数组中，这里直接返回 start 或者 end 即可
        return start

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """ 二分查找 """
        if not nums:
            return [-1, -1]
        # 先执行第一个位置的搜索
        left_border = self._find_left_border(nums, target)
        # 若找不到，直接返回 [-1, -1]
        if left_border == -1:
            return [-1, -1]
        # 后执行最后一个位置的搜索
        right_border = self._find_right_border(nums, target)
        return [left_border, right_border]
