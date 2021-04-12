# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/11 14:13
# filename    : solution.py
# description : LC 1143 最长公共子序列

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """ 动态规划 """
        n1, n2 = len(text1), len(text2)
        # dp[i + 1][j + 1] 表示 text[0,...,i] 和 text[0,...,j] 的最长公共子序列
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i in range(n1):
            for j in range(n2):
                # 当 text1[i] = text2[j] 时，dp[i + 1][j + 1] = dp[i][j] + 1
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                # 否则取 dp[i + 1][j] 和 dp[i][j + 1] 的最大值
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[n1][n2]
