# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/6/17 00:11
# filename    : solution.py
# description : LC 88 合并两个有序数组

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """ 双指针 """
        i, j = 0, 0
        # 初始化临时数组，避免合并时被覆盖
        tmp = []
        while i < m or j < n:
            # i 超过 m 或者 nums2[j] 小于 nums1[i]
            if i >= m or (j < n and nums2[j] < nums1[i]):
                # 将较小的数放入临时数组中
                tmp.append(nums2[j])
                j += 1
            else:
                tmp.append(nums1[i])
                i += 1
        # 原地修改 nums1
        nums1[:] = tmp

    def mergeReverse(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """ 逆向双指针（重点理解） """
        tail = len(nums1) - 1
        # 初始化，分别指向末尾数字
        i, j = m - 1, n - 1
        while j >= 0:
            # 当 nums1 所有元素遍历结束，或 nums2[j] 大于 nums1[i]
            if i < 0 or nums1[i] <= nums2[j]:
                # 从后开始对数组进行合并
                nums1[tail] = nums2[j]
                j -= 1
            else:
                nums1[tail] = nums1[i]
                i -= 1
            # 指针向前移动
            tail -= 1
