# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/17 11:32
# filename    : solution.py
# description : LC 121 买卖股票的最佳时机

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ 遍历数组 """
        min_price = float('int')
        max_profit = 0

        for price in prices:
            # 每次与最小值比较，获取当前的最小值
            min_price = min(price, min_price)
            # 每次将差值与最大值比较，获取当前最大值
            max_profit = max(price - min_price, max_profit)
        return max_profit

    def maxProfitDP(self, prices: List[int]) -> int:
        """ 动态规划 """
        profit = 0  # profit 为某天卖出股票的收益，初始化为 0
        max_profit = 0  # max_profit 为最大收益

        for idx in range(1, len(prices)):
            # 状态转移方程
            profit = max(profit, 0) + prices[idx] - prices[idx - 1]
            # 记录最大收益
            max_profit = max(profit, max_profit)
        return max_profit
