# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/8 23:30
# filename    : solution.py
# description : LC 5 最长回文子串

class Solution:
    def longestPalindromeDP(self, s: str) -> str:
        """ 动态规划，可用滚动数组进行空间优化 """
        n = len(s)
        # dp[i][j] 表示字符串 s 从下标 i 到 j 是否为回文串
        dp = [[False for _ in range(n)] for _ in range(n)]
        # 记录全局最长回文串的长度，左和右边界
        max_len, left, right = 0, 0, 0

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
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    left, right = i, j
        return s[left:right + 1]

    def longestPalindrome(self, s: str) -> str:
        """ 中心扩展 """
        max_len = 0
        max_left, max_right = 0, 0
        n = len(s)
        for i in range(n):
            for j in range(2):
                left, right = i, i + j
                length = 1
                while left >= 0 and right < n and s[left] == s[right]:
                    length = right - left + 1
                    left -= 1
                    right += 1
                if length > max_len:
                    max_len = length
                    max_left, max_right = left, right
        return s[max_left + 1:max_right]

    def longestPalindromeManacher(self, s: str) -> str:
        """ Manacher 算法 """
        t = '$#' + '#'.join(s)
        n = len(t)
        t += '#!'

        # f[i] 为改造后的 t 的第 i 个字符为回文中心的最大回文半径（包含中心点）
        # 由此， 第 i 个字符的最大回文串长度 L = f(i) - 1
        f = [0] * n
        # 全局最长回文串长度
        max_f = 0
        # im 当前最长回文串的中心点
        # rm 当前最长回文串右端点
        im, rm = 0, 0
        # 全局最长回文串的中心点和右端点
        max_im, max_rm = 0, 0

        for i in range(1, n):
            # 初始化 f[i]
            if i <= rm:
                # 2 * im - i 是 i 关于 im 对称的位置，f[2 * im - i] 就是对称位置的最大回文半径
                # rm - i + 1 是右端点距离 i 的长度，这时 i 的最长回文串长度 f[i] 有可能大于 rm - i + 1
                # 因为不确定长度，所以取最小值，保证以 i 为中心的回文串在当前最大回文串内
                f[i] = min(rm - i + 1, f[2 * im - i])
            # 中心扩展
            while t[i + f[i]] == t[i - f[i]]:
                f[i] += 1
            # 以 i 为中心点的最右端位是 i + f[i] - 1
            # 更新最长回文串，包括中心点和最右端点
            if i + f[i] - 1 > rm:
                im, rm = i, i + f[i] - 1
                # 记录全局最长回文串的中心点和最右端点
                if f[i] > max_f:
                    max_f = f[i]
                    max_im, max_rm = im, rm
        # 由于 t 中插入了 # 分隔符，所以切片步长为 2
        return t[2 * max_im - max_rm + 1:max_rm + 1:2]
