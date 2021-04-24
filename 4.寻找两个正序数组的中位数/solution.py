# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/18 23:49
# filename    : solution.py
# description : LC 4 寻找两个正序数组的中位数

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """ 二分查找 """

        def get_kth_element(k):
            """寻找第 k 小的数，注意 k 不是索引
            当数组的元素个数为偶数，k 是 (n1 + n2) // 2 和 (n1 + n2) // 2 + 1
            当数组的元素个数为奇数，k 是 (n1 + n2 + 1) // 2
            """
            idx1, idx2 = 0, 0
            while True:
                # 边界条件 1: 当 idx1 达到 nums1 的尾部，那么中位数一定是 nums2 的第 idx2 + k - 1 个元素
                if idx1 == n1:
                    return nums2[idx2 + k - 1]
                # 边界条件 2: 当 idx2 达到 nums2 的尾部，那么中位数一定是 nums1 的第 idx1 + k - 1 个元素
                if idx2 == n2:
                    return nums1[idx1 + k - 1]
                # 边界条件 3: 当 k 减少至 1 时，直接比较数组 nums1 和 nums2 的剩余元素的第一个元素，取最小值即可
                if k == 1:
                    return min(nums1[idx1], nums2[idx2])

                # 避免越界
                # 取 k // 2 - 1 作为比较的下标的原因是两数组小于等于这个下标对应的元素的个数不会超过 2(k // 2 - 1) <= k - 2
                # 因此再加上 k // 2 - 1 本身最多只有 k - 1 个元素，可以通过二分查找不断逼近第 k 小这个位置
                new_idx1 = min(idx1 + k // 2 - 1, n1 - 1)
                new_idx2 = min(idx2 + k // 2 - 1, n2 - 1)
                pivot1, pivot2 = nums1[new_idx1], nums2[new_idx2]
                if pivot1 <= pivot2:
                    # new_idx1 - idx1 + 1 表示包括 new_idx1 在内的应排序的元素个数
                    k -= (new_idx1 - idx1 + 1)
                    # idx1 从 new_idx1 的下一个位置开始寻找第 k 小的数
                    idx1 = new_idx1 + 1
                else:
                    k -= (new_idx2 - idx2 + 1)
                    idx2 = new_idx2 + 1

        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        if total % 2:
            # 当数组元素个数为奇数时，两数组中位数是第 (total + 1) // 2 小的数
            return get_kth_element((total + 1) // 2)
        else:
            # 偶数时，中位数是第 k 小的数和第 k + 1 小的数的平均值
            return 0.5 * (get_kth_element(total // 2) + get_kth_element(total // 2 + 1))

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]):
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            # 保证第一个数组的长度不大于第二个数组
            return self.findMedianSortedArrays2(nums2, nums1)

        # 为了兼容临界条件，如 nums1[i - 1]，nums1[n1]，nums2[j - 1]，nums2[n2]，设置极大值
        infinity = float('inf')
        left, right = 0, n1
        # left side: nums1[0,..., i - 1] 和 nums2[0,...,j-1]
        # right side: nums1[i,..., n1 - 1] 和 nums2[j,...,n2 - 1]
        max_in_left_side, min_in_right_side = 0, 0
        # 当 left = right，需要再计算一次左半部分的最大值和右半部分的最小值，比如 nums1 为空的情况
        # 只要在较短数组上进行二分查找
        while left <= right:
            i = (left + right) // 2
            # 当 n1 + n2 为偶数，i + j = m - i + n - j
            # 当 n1 + n2 为奇数，i + j = m - i + n - j + 1
            # 左半部分元素与右半部分元素的数量关系
            j = (n1 + n2 + 1) // 2 - i

            # 计算 nums1[i - 1]，nums1[i]，nums2[j - 1]，nums2[j]，并进行比较
            # 让 nums2[j - 1] <= nums1[i] and nums1[i - 1] <= nums2[j] 保证 left side <= right side
            nums_i1 = -infinity if i == 0 else nums1[i - 1]
            nums_i = infinity if i == n1 else nums1[i]
            nums_j1 = -infinity if j == 0 else nums2[j - 1]
            nums_j = infinity if j == n2 else nums2[j]

            # 等价于找到最大的 i，使得 nums1[i - 1] <= nums2[j]
            # 这里如何证明？
            if nums_i1 <= nums_j:
                max_in_left_side, min_in_right_side = max(nums_i1, nums_j1), min(nums_i, nums_j)
                left = i + 1
            # 如果 nums1[i - 1] > nums2[j]，说明 nums1[i - 1] 偏大，减少右边界，缩小查找范围
            else:
                right = i - 1
        if (n1 + n2) % 2:
            # 中位数是左半部分的最大值
            return max_in_left_side
        # 中位数是左半部分最大值和右半部分最小值的平均值
        return (min_in_right_side + max_in_left_side) / 2
