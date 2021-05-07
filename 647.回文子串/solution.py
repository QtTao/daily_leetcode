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

    def countSubstringsCenter(self, s: str) -> int:
        """ 中心扩展 """
        ans = 0
        n = len(s)
        # 回文中心个数有 2n - 1 个，其中单字符有 n 个，双字符有 n - 1 个
        for center in range(2 * n - 1):
            # 关键是找出回文中文的左边界，右边界和中心点的关系
            # 回文中心的左边界 left 和右边界 right 要么相等（单字符），要么相隔一个位置（双字符），即 left + 1 = right
            left, right = int(center / 2), int(center / 2 + center % 2)
            # 注意越界问题
            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1
                # 如果左边界和右边界的字符相同，中心向两边扩展
                left -= 1
                right += 1
        return ans

    def countSubstringManacher(self, s: str) -> int:
        """ Manacher 算法 """
        t = '$#' + '#'.join(s)
        n = len(t)
        t += '#!'  # 加入 $ 和 ! 是为了中心扩展时避免越界

        # f[i] 为改造后的 t 的第 i 个字符为回文中心的最大回文半径（包含中心点）
        # 由此， 第 i 个字符的最大回文串长度 L = f(i) - 1
        f = [0] * n
        # im 当前最长回文串的中心点
        # rm 当前最长回文串右端点
        im, rm, ans = 0, 0, 0

        for i in range(1, n):
            # 初始化 f[i]
            if i <= rm:
                # 2 * im - i 是 i 关于 im 对称的位置，f[2 * im - i] 就是对称位置的最大回文半径
                # rm - i + 1 是右端点距离 i 的长度，这时 i 的最长回文串长度 f[i] 有可能大于 rm - i + 1
                # 因为不确定长度，所以取最小值，保证以 i 为中心的回文串在当前最大回文串内
                f[i] = min(rm - i + 1, f[2 * im - i])
            # 中心扩展
            # i + f[i] 是以 i 为中心的回文半径的下一个位置，特别地当 f[i] = 0，就是单字符
            while t[i + f[i]] == t[i - f[i]]:
                f[i] += 1
            # 以 i 为中心点的最右端位是 i + f[i] - 1
            # 更新最长回文串，包括中心点和最右端点
            if i + f[i] - 1 > rm:
                im, rm = i, i + f[i] - 1
            # 统计回文子串个数
            ans += f[i] // 2
        return ans
