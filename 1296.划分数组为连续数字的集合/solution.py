# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/9 00:10
# filename    : solution.py
# description : LC 1296 划分数组为连续数字的集合

from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k:
            return False
        # 统计每个元素出现次数
        counter = Counter(nums)

        # 不用全部元素排序，只对 key 进行排序
        keys = sorted(counter)
        for key in keys:
            count = counter[key]
            # 如果 count 被清空，使用下一数字作为连续数组的最小值
            if count > 0:
                for num in range(key + 1, key + k):
                    # 当 num 不存在时，counter 返回 0
                    if counter[num] >= count:
                        counter[num] -= count
                    else:
                        return False
        return True
