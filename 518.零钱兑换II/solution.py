# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/6/3 00:50
# filename    : solution.py
# description : LC 518 零钱兑换II

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """ 动态规划 """
        # 假设 dp 为金额 i 的硬币组合数
        dp = [0] * (amount + 1)
        # 如果金额为 0，那么只有一种零硬币的组合情况，所以 dp[0] = 1
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                # 对于元素之和等于 i - coin 的每一个组合，在最后添加 coin 之后即可得到一个元素之和等于 i 的组合
                # 因此在计算 dp[i]，应该计算所有 dp[i - coin] 之和
                # 如何保证这里的组合数不会出现重复？
                dp[i] += dp[i - coin]
        return dp[-1]
