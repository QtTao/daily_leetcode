# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/4 00:18
# filename    : solution.py
# description : LC 169 多数元素


class Solution:
    def majorityElementHashmap(self, nums: List[int]) -> int:
        """ 哈希表 """
        hashmap = {}
        maj, appearance = None, 0
        for num in nums:
            # 利用哈希表记录每一个元素出现的次数，可以使用 collections.defaultdict(int)
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
            # 每次比较，返回当前出现次数最多的元素
            if hashmap[num] > appearance:
                appearance = hashmap[num]
                maj = num
        return maj

    def majorityElementRecursion(self, nums: List[int]) -> int:
        """ 分治法 """

        def appearance(num, left, right):
            """ 计算出现次数 """
            count = 0
            for idx in range(left, right + 1):
                if num == nums[idx]:
                    count += 1
            return count

        def majority(left, right):
            """ 基于下标的分治法 """
            # 如果 nums 只有一个元素，或者在分治过程 left 和 right 重合，直接返回
            if left == right:
                return nums[left]

            # 将数组分成左右两份
            mid = (right - left) // 2 + left
            # 左边数组出现的众数
            left_maj = majority(left, mid)
            # 右边数组出现的众数
            right_maj = majority(mid + 1, right)
            # 如果两边众数相同，直接返回
            if left_maj == right_maj:
                return left_maj

            # 比较两个众数在整个区间内出现的次数来决定该区间的众数
            left_count = appearance(left_maj, left, right)
            right_count = appearance(right_maj, left, right)

            if left_count > right_count:
                return left_maj
            else:
                return right_maj

        return majority(0, len(nums) - 1)

    def majorityElement(self, nums: List[int]) -> int:
        """ Boyer-Moore 投票算法 """
        supporter = 0
        candidate = None

        for num in nums:
            # 当支持者被抵消至 0 后，重新选择候选人
            if supporter == 0:
                candidate = num
            # 当候选人与当前的相同，支持者加一
            if num == candidate:
                supporter += 1
            # 否则减一
            else:
                supporter -= 1
        return candidate
