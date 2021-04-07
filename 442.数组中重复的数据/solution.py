# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/7 23:17
# filename    : solution.py
# description : LC 442 数组中重复的数据

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup = []
        # num 在 [1, n] 的范围内，遍历 nums 令第 num 个数变成它的相反数
        for num in nums:
            num = abs(num)
            # 如果第 num 个数字已经是负数，说明此前已被访问
            if nums[num - 1] < 0:
                dup.append(num)
            nums[num - 1] = -nums[num - 1]
        return dup
