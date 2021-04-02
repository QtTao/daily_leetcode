# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/1 13:21
# filename    : solution.py
# description : LC 3 无重复字符的最长子串

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ 动态规划 """
        hashmap = {}
        # 假设 dp[j] 为以 s[j] 为结尾的最长不重复子串的长度，同时固定右边界，假设 s[j] 左边距离最近的为 s[i]，即 s[j] = s[i]
        # 1. 当 i < 0，即 s[j] 左边无相同字符，则 dp[j] = dp[j - 1] + 1
        # 2. 当 dp[j - 1] < j - i，说明 s[i] 在子串 dp[j - 1] 区间外，则 dp[j] = dp[j - 1] + 1（可以与上一种情况合并）
        # 3. 当 dp[j - 1] >= j - i, 说明 s[i] 在子串 dp[j - 1] 区间内，则 dp[j] = j - i
        # max(dp) 即无重复最长子串
        max_len, dp = 0, 0
        for idx, x in enumerate(s):
            # 返回重复字符的上一个索引位置
            last_idx = hashmap.get(x, -1)
            # 更新索引
            hashmap[x] = idx
            # case 1 & 2
            if dp < idx - last_idx:
                dp += 1
            # case 3
            else:
                dp = idx - last_idx
            max_len = max(max_len, dp)
        return max_len

    def lengthOfLongestSubstringSlidingWindows(self, s: str) -> int:
        """ 滑动窗口 """
        hashmap = {}
        # start 为无重复子串的起始位置
        start, max_len = 0, 0
        for idx, x in enumerate(s):
            if x in hashmap:
                # 一旦出现重复字符，更新起始位置
                # hashmap[x] + 1: 重复字符的下一个位置
                # 这里必须取两者的最大值
                # 如果直接取 hashmap[x] + 1，有可能导致起始位置回退，如 'tmmzuxt'
                # 如果直接取 start，起始位置不能及时更新，如 'aabc'
                start = max(hashmap[x] + 1, start)
            # 进行 n 次比较，有可能出现冗余
            max_len = max(max_len, idx - start + 1)
            # 更新字符的最后位置
            hashmap[x] = idx
        return max_len

    def lengthOfLongestSubstringSlidingWindows2(self, s: str) -> int:
        """ 滑动窗口（优化版，减少长度比较） """
        hashmap = {}
        # start 为无重复子串的起始位置，这里初始化为 -1，表示在 s 左边界的左侧，还没开始滑动
        start, max_len = -1, 0
        for idx, x in enumerate(s):
            # 这里 hashmap[x] > start 很巧妙，相当将 max(hashmap[x], start) 拆分成 if 条件和赋值语句，
            # 可以进一步减少最大值比较次数
            if x in hashmap and hashmap[x] > start:
                # 更新起始位置，窗口移动，实质上是"跳动"窗口
                start = hashmap[x]
            else:
                # 当出现重复字符，且重复字符上次的位置在无重复子串起始位置之后，
                # 说明起始位置需要更新，最长子串的长度会缩短，也就没有比较出最大值的需要
                max_len = max(max_len, idx - start)
            # 更新字符的最后位置
            hashmap[x] = idx
        return max_len
