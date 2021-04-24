# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/24 21:58
# filename    : solution.py
# description : LC 46 全排列


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        rv = []

        def backtrack(start: int):
            if start == n:
                # 注意拷贝数组
                rv.append(nums[:])
            # 每次循环 start 往前移动一个位置，说明 start 前的数组已被固定，对剩余的部分进行全排列
            for idx in range(start, n):
                # 当 idx = start，不需要交换元素
                if idx != start:
                    # 【重点理解】在回溯的过程，不断交换元素
                    # 第一次 start = 1，idx = 2，交换得到数组 [1, 3, 2]
                    # 第二次，start = 0, idx = 1，交换得到数组 [2, 1, 3]
                    # 第三次，start = 1, idx = 2，交换得到数组 [2, 3, 1]
                    # 第四次，start = 0, idx = 2，交换得到数组 [3, 2, 1]
                    # 第五次，start = 1, idx = 2，交换得到数组 [3, 1, 2]
                    nums[idx], nums[start] = nums[start], nums[idx]
                backtrack(start + 1)
                if idx != start:
                    # 完成第一次时，start = 1，idx = 2，数组 [1, 3, 2]，交换后恢复成 [1, 2, 3]
                    # 完成第三次时，start = 1, idx = 2，数组 [2, 3, 1]，交换后恢复为 [2, 1, 3]
                    # 完成第二次时，start = 0, idx = 1，数组 [2, 1, 3]，交换后恢复为 [1, 2, 3]
                    # 完成第五次时，start = 1, idx = 2，数组 [3, 1, 2]，交换后恢复为 [3, 2, 1]
                    # 完成第四次时，start = 0, idx = 2，数组 [3, 2, 1]，交换后恢复为 [1, 2, 3]
                    nums[idx], nums[start] = nums[start], nums[idx]

        backtrack(0)
        return rv
