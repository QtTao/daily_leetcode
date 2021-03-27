# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/27 21:27
# filename    : solution.py
# description : LC 70 爬楼梯

import math


class Solution:
    def climbStairs(self, n: int) -> int:
        """ 动态规划 """
        dp, dp1, dp2 = 0, 0, 1
        for _ in range(n):
            # T(n) = T(n - 1) + T(n - 2)
            dp = dp1 + dp2
            dp1 = dp2
            dp2 = dp
        return dp

    def climbStairsMatrix(self, n: int) -> int:
        """ 矩阵快速幂 """
        q = [[1, 1], [1, 0]]
        rv = self.matrix_pow(q, n)
        return rv[0][0]

    def matrix_pow(self, a: List[List[int]], n: int) -> List[List[int]]:
        """ 二阶矩阵幂 """
        rv = [[1, 0], [0, 1]]
        while n > 0:
            # 判断最后一位是否为 1，奇偶性
            if n & 1:
                rv = self.matrix_multiply(rv, a)
            n >>= 1
            a = self.matrix_multiply(a, a)
        return rv

    def matrix_multiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        """ 二阶矩阵乘法 """
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
        return c

    def climbStairsFormula(self, n: int) -> int:
        """ 斐波那契数列通项公式 """
        sqrt5 = math.sqrt(5)
        rv = math.pow((1 + sqrt5) / 2, n + 1) - math.pow((1 - sqrt5) / 2, n + 1)
        return round(rv / sqrt5)
