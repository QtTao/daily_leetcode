# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/5 21:34
# filename    : solution.py
# description : LC 647 回文子串


class Solution:
    def countSubstrings(self, s: str) -> int:
        """ 动态规划 """
        n = len(s)
        # dp[i][j] 表示字符串 s 从下标 i 到 j 是否为回文串
        dp = [[False for _ in range(n)] for _ in range(n)]
        # 记录回文串的数量
        count = 0

        # 从左往右，上往下更新状态，保证在更新 dp[i][j] 已完成 dp[i + 1][j - 1] 的更新
        for j in range(n):
            for i in range(j + 1):
                # 如果 s[i] 不等于 s[j]，那么 s[i:j+1] 肯定不是回文串，dp[i][j] = False
                if s[i] != s[j]:
                    continue
                # 这里分三种情况讨论
                # Case 1 j - i = 0，单字符必然是回文子串，dp[i][j] = True
                # Case 2 j - i = 1，两个相同字符也是回文子串，dp[i][j] = True
                # Case 2 j - i >= 2，如果 s[i:j + 1] 前后两个字符相同，且 s[i + 1:j] 为回文子串，即 dp[i + 1][j - 1] = True，那么 s[i:j + 1] 也是回文子串，dp[i][j] = True
                dp[i][j] = (j - i < 2) or dp[i + 1][j - 1]
                # 如果从 i 到 j 能构成回文串，count + 1
                if dp[i][j]:
                    count += 1
        return count

    def countSubstringsRollingArray(self, s: str) -> int:
        """ 动态规划 + 滚动数组 """
        n = len(s)
        dp = [False] * n
        count = 0

        for j in range(n):
            for i in range(j + 1):
                # 当头尾字符相同，且中间的字符串为回文串时，构成最新的回文串，count + 1
                if s[i] == s[j] and ((j - i < 2) or dp[i + 1]):
                    dp[i] = True
                    count += 1
                # 这里需要注意若不符合条件也要更新状态，i 位置的状态会被多次更新
                else:
                    dp[i] = False
        return count
