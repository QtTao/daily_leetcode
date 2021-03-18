# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/18 14:06
# filename    : solution.py
# description : LC 123 买卖股票的最佳时机III


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ 动态规划-二维数组 """
        n = len(prices)
        dp = [[None] * 5 for _ in range(n)]
        # dp[i][j]：表示第 i 天持有的收益
        # dp[i][0]：第 i 天没持有过股票，收益为 0
        # dp[i][1]：第 i 天买了一支股票
        # dp[i][2]：第 i 天买了一只股票然后卖出
        # dp[i][3]：第 i 天买了第二支股票
        # dp[i][4]：第 i 天完成了两笔交易
        # 初始化
        dp[0][0] = 0  # 第 0 天没有操作，收益为 0
        dp[0][1] = -prices[0]  # 第 0 天买入，收益为 -price
        dp[0][2] = 0  # 第 0 天卖出，收益为 0
        dp[0][3] = -prices[0]  # 第 0 天第二次买入，收益为 -price
        dp[0][4] = 0  # 第 0 天第二次卖出，收益为 0
        for idx in range(1, n):
            # 没有操作，收益为 0
            dp[idx][0] = 0
            # Case 1 第 i 天买入股票，收益为 dp[i - 1][0] - price
            # Case 2 第 i - 1 天已买入票，没有操作，收益为 dp[i - 1][1]
            dp[idx][1] = max(dp[idx - 1][1], dp[idx - 1][0] - prices[idx])
            # Case 1 第 i 天卖出股票，收益为 dp[i - 1][1] + price
            # Case 2 第 i - 1 天已卖出股票，收益为 dp[i - 1][2]
            dp[idx][2] = max(dp[idx - 1][2], dp[idx - 1][1] + prices[idx])
            # Case 1 第 i 天买入股票（第二次），收益为 dp[i - 1][2] - price
            # Case 2 第 i - 1 天买入股票（第二次），收益为 dp[i - 1][3]
            dp[idx][3] = max(dp[idx - 1][3], dp[idx - 1][2] - prices[idx])
            # Case 1 第 i 天卖出股票，收益为 dp[i - 1][3] + price
            # Case 2 第 i - 1 天已卖出股票（第二次），收益为 dp[i - 1][4]
            dp[idx][4] = max(dp[idx - 1][4], dp[idx - 1][3] + prices[idx])
        return dp[n - 1][4]

    def maxProfitDPOpt(self, prices: List[int]) -> int:
        """ 动态规划-空间优化 """
        dp0, dp1, dp2 = 0, -prices[0], 0
        dp3, dp4 = -prices[0], 0
        # dp[i][j] 只依赖 dp[i - 1][j] 的状态，状态矩阵可压缩空间
        for idx in range(1, len(prices)):
            dp1 = max(dp1, dp0 - prices[idx])
            dp2 = max(dp2, dp1 + prices[idx])
            dp3 = max(dp3, dp2 - prices[idx])
            dp4 = max(dp4, dp3 + prices[idx])
        return dp4
