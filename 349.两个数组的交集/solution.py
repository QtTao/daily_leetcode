# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/6/12 13:44
# filename    : solution.py
# description : LC 349 两个数组的交集

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ 排序 + 双指针 """
        n, m = len(nums1), len(nums2)
        nums1.sort()
        nums2.sort()

        i, j = 0, 0
        ans = []
        while i < n and j < m:
            num1, num2 = nums1[i], nums2[j]
            if num1 == num2:
                # 确保结果数组的元素的唯一性
                if not ans or num1 != ans[-1]:
                    ans.append(num1)
                i += 1
                j += 1
            elif num1 > num2:
                j += 1
            else:
                i += 1
        return ans

    def intersectionSet(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ 哈希表 """
        n, m = len(nums1), len(nums2)
        # 元素较少的集合为 set1
        if n > m:
            set1, set2 = set(nums2), set(nums1)
        else:
            set1, set2 = set(nums1), set(nums2)

        ans = []
        for num in set1:
            # O(1) 时间复杂度
            if num in set2:
                ans.append(num)
        return ans
