# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/4 16:26
# filename    : solution.py
# description : LC 62 不同路径

import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """ 动态规划 f(m, n) = f(m - 1, n) + f(m, n - 1) """
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def uniquePathsRollingArray(self, m: int, n: int) -> int:
        """ 动态规划 + 滚动数组 """
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                # dp[j] 的上一个状态即二维数组中的 dp[i - 1][j]
                # 所以 dp[j] = dp[j] + dp[j - 1]
                dp[j] += dp[j - 1]
        return dp[n - 1]

    def uniquePathsMath(self, m: int, n: int) -> int:
        """ 组合数学 C(m + n - 2, n - 1) = (m + n - 2)!/(m - 1)!/(n - 1)! """
        return int(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))
