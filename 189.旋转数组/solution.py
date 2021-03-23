# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/23 13:23
# filename    : solution.py
# description : LC 189 旋转数组

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """ 使用额外的数组 """
        tmp_nums = nums[:]
        n = len(nums)
        for idx in range(n):
            new_idx = (idx + k) % n
            nums[new_idx] = tmp_nums[idx]

    def rotate_reverse(self, nums: List[int], k: int) -> None:
        """ 数组反转 """

        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        k %= n
        # 三次反转
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

    def rotate_ring(self, nums: List[int], k: int) -> None:
        """ 环状替换 """
        n = len(nums)
        idx, count = 0, 0
        # 当所有元素都被访问后，完成旋转操作
        while count < n:
            curr = idx
            num = nums[idx]
            while True:
                # 根据下标替换位置
                new_idx = (curr + k) % n
                tmp = nums[new_idx]
                nums[new_idx] = num
                curr, num = new_idx, tmp
                count += 1
                # 比如 [1, 2, 3, 4] k = 2 的替换路线没有交集，会陷入死循环
                # 当下标再次出现，表明替换已经完成，跳出循环
                if idx == curr:
                    break
            idx += 1
