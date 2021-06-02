# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/6/2 22:28
# filename    : solution.py
# description : LC 322 零钱兑换

import functools


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """ 动态规划（自底而上） """
        # 假设 dp[i] 为组成金额 i 所需最少的硬币数量
        dp = [float('inf')] * (amount + 1)
        # 当金额为 0，无法硬币组成，所以 dp[0] = 0
        dp[0] = 0
        for coin in coins:
            # 比硬币还小的值，不用进行比较 dp[i] i < 0 直接忽略
            for i in range(coin, amount + 1):
                # dp[i] 初始化为 float('inf')，是通过前面能转移过来的状态的最小值加上枚举的硬币数量 1
                # 即 dp[i] = min(dp[i - c0], dp[i - c1], dp[i - c2], ..., dp[i - cn-1]) + 1，其中 c0，c1，...，cn-1 共有 n 个硬币
                dp[i] = min(dp[i], dp[i - coin] + 1)
        # 如果 dp 状态没有改变，保持初始化的状态，说明无法使用硬币组成金额
        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChangeMemory(self, coins: List[int], amount: int) -> int:
        """ 记忆化回溯（自顶而上） """

        # 使用 lru_cache 缓存 memory_search 的结果
        @functools.lru_cache(amount)
        def memory_search(amount) -> int:
            # 金额 0 由 0 个硬币组成
            if amount == 0:
                return 0
            # 将最少硬币数量初始化成一个极大值，方便比较
            coin_num = float('inf')
            for coin in coins:
                # 只计算 amount >= coin 的情况，负数金额没有意义
                if amount >= coin:
                    # 深度优先搜索
                    ans = memory_search(amount - coin)
                    # coin_num 是遍历 coins 中产生的，< coin_num 是为了计算最小值
                    if 0 <= ans < coin_num:
                        coin_num = ans + 1
            # 如果硬币数量没有变化，说明当前金额无法由硬币组成
            return coin_num if coin_num < float('inf') else -1

        return memory_search(amount)
