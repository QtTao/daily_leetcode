# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/18 13:22
# filename    : solution.py
# description : LC 122 买卖股票的最佳时机II


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ 贪心 """
        max_profit = 0
        prev_price = prices[0]
        for price in prices[1:]:
            if price > prev_price:
                # 叠加每一次上涨带来的收益
                max_profit += price - prev_price
            # 更新价格
            prev_price = price
        return max_profit

    def maxProfitDP(self, prices: List[int]) -> int:
        """ 动态规划-二维数组 """
        n = len(prices)
        # 假设 dp[i][0] 表示第 i 天交易完后没有股票的最大收益
        # dp[i][1] 表示第 i 天交易完后持有一支股票的最大收益
        # 初始化状态矩阵
        dp = [[None, None] for _ in range(n)]
        # 第 0 天交易结束后，没有股票的最大收益 dp[0][0] = 0
        # 持有股票的最大收益 dp[0][1] = -第一支股票的价格
        dp[0][0], dp[0][1] = 0, -prices[0]

        for idx in range(1, n):
            # 第 i 天状态可由第 i - 1 天的状态转移
            # 下列有两种情况
            # 1. 第 i - 1 天没有股票，最大收益 dp[idx - 1][0]
            # 2. 第 i - 1 天持有一支股票，将其卖出，最大收益 dp[idx - 1][1] + price
            # 3. 取两者最大值
            dp[idx][0] = max(dp[idx - 1][0], dp[idx - 1][1] + prices[idx])
            # 1. 第 i - 1 天没有股票需要买进股票，最大收益 dp[idx - 1][0] - price
            # 2. 第 i - 1 天持有一支股票，最大收益 dp[idx - 1][1]
            # 3. 取两者最大值
            dp[idx][1] = max(dp[idx - 1][1], dp[idx - 1][0] - prices[idx])
        # 持有股票的最大收益一定低于不持有股票的最大收益
        return dp[n - 1][0]

    def maxProfitDPOPT(self, prices: List[int]) -> int:
        """ 动态规划-空间优化 """
        n = len(prices)
        # 从状态转移方程得知，第 i 天的状态是由第 i - 1 天决定的
        # 所以前一天的两种状态可以用 cash（没有股票只有现金）和hold（持有股票）来表示
        cash, hold = 0, -prices[0]
        for idx in range(1, n):
            # 保持 cash 状态，避免更新覆盖
            tmp_cash = cash
            cash = max(cash, hold + prices[idx])
            hold = max(tmp_cash - prices[idx], hold)
        return cash
