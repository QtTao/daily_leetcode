# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/22 23:19
# filename    : solution.py
# description : LC 300 最长递增子序列

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """ 动态规划 """
        n = len(nums)
        # 假设 dp[i] 为 nums[i] 为结尾的最长递增子序列的长度
        # 初始化子序列长度为 1

        dp = [1] * len(nums)
        for i in range(n):
            for j in range(i):
                # dp[j] 是以 nums[j] 为结尾的最长递增子序列的长度，其中 i < j
                # 若 nums [i] 严格大于 nums[j]，长度加一
                if nums[j] < nums[i]:
                    # 这里注意要取到 i 位置的最大值，满足状态的定义
                    dp[i] = max(dp[j] + 1, dp[i])

        # 以最后的元素作为结尾的子序列不一定是最长，需选出最大值
        return max(dp)

    def lengthOfLISGreedy(self, nums: List[int]) -> int:
        """  贪心 + 二分查找 """
        n = len(nums)
        if n < 2:
            return 1

        # 创建数组保存最长递增子序列
        array = [nums[0]]
        for num in nums[1:]:
            # 如果 num 严格大于数组中的元素，那么插到最后
            if num > array[-1]:
                array.append(num)
                continue

            # 这里二分查找+插入的操作非常巧妙
            # 用 num 覆盖掉数组中比 num 大但最小的元素，让后续元素有更大可能加入到递增子序列中
            # 一旦覆盖，有可能跟真实的最长递增子序列不同，但长度一致
            # 比如 [10, 9, 2, 5, 7, 3] => array = [2, 3, 7]
            left, right = 0, len(array) - 1
            while left < right:
                mid = left + (right - left) // 2
                if array[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            array[left] = num
        return len(array)
