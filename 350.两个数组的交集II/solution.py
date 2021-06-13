# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/6/13 12:32
# filename    : solution.py
# description : LC 350 两个数组的交集II

from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ 排序 + 双指针 """
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        ans = []
        while i < n and j < m:
            num1, num2 = nums1[i], nums2[j]
            if num1 == num2:
                # 与 LC 349 不同之处是输出结果保留多个元素，每个元素出现次数与在两个数组出现次数最小值一致
                ans.append(num1)
                i += 1
                j += 1
            elif num1 > num2:
                j += 1
            else:
                i += 1
        return ans

    def intersectCounter(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ 哈希表 """
        # 将元素数量较少的数组放在前面
        if len(nums1) > len(nums2):
            self.intersect(nums2, nums1)
        # 将数组转换为计数器
        counter = Counter(nums1)
        ans = []
        for num in nums2:
            # 如果 num 在 nums1 的计数器中
            if counter.get(num, 0) > 0:
                # 加入结果数组
                ans.append(num)
                # 计数器减 1
                counter[num] -= 1
                # 如果 num 在 nums1 数组的个数为 0，将其剔除计数器
                # 这样能确保结果数组中每个元素出现的次数，与 nums1 和 nums2 中出现次数最小值一致
                if not counter[num]:
                    counter.pop(num)
        return ans
