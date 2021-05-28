# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/25 17:31
# filename    : solution.py
# description : LC 139 单词拆分

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """ 动态规划 """
        n = len(s)
        # dp[i] 表示 s 的前 i 位是否可以用 wordDict 中的单词表示
        dp = [False] * (n + 1)
        # 初始化表示空字符可以被表示
        dp[0] = True
        # 遍历字符串 i 在区间 [0, n)
        for i in range(n):
            # 遍历结束索引 j 在区间 [i + 1, n + 1)
            for j in range(i + 1, n + 1):
                # 若 dp[i] = True 且 s[i,...,j) 在 wordDict 中
                # 说明 s 的前 i 位可以用 wordDict 表示，而 s[i,...,j) 在 wordDict 中，即 s 的前 j 位可以表示
                # 这里的状态转移方程设计得很巧妙，需要理解
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
                    break
        return dp[-1]

    def wordBreakBackTrack(self, s: str, wordDict: List[str]) -> bool:
        """ 回溯 """
        # 采用缓存实现记忆化回溯，backtrack 可以快速得到结果
        import functools
        @functools.lru_cache(None)
        def backtrack(s):
            # 当 s 长度为 0，表示已经使用 wordDict 中的单词分割完成，返回 True
            if not s:
                return True
            # 遍历字符串分割用的索引 i，将字符串分成两部分
            # 如果第一部分出现在 wordDict 中，那么递归寻找剩余部分中是否有出现在 wordDict 中单词
            # 如果有，继续递归剩余部分，直至 s 长度为 0；如果没有，说明剩余部分不能被表示，分割的索引向前移动
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict and backtrack(s[i:]):
                    return True
            return False

        return backtrack(s)
