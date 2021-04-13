# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/14 00:02
# filename    : solution.py
# description : LC 905 按奇偶排序数组

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        """ 双指针 """
        left, right = 0, len(A) - 1
        while left < right:
            # 当 left 是奇数，right 是偶数，交换位置
            if A[left] % 2 and not A[right] % 2:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
            # 当 left 指向偶数，left 指针向前移动
            while not A[left] % 2 and left < right:
                left += 1
            # 当 right 指向奇数，right 指针向后移动
            while A[right] % 2 and left < right:
                right -= 1
        return A
