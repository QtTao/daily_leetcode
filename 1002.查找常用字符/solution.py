# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/6/13 16:05
# filename    : solution.py
# description : LC 1002 查找常用字符


from collections import Counter


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """ 哈希表 """
        # 记录每个字符串对应的计数器
        counters = []
        # 记录出现在所有字符串的字符集合
        letters = set(words[0])
        for word in words:
            counters.append(Counter(word))
            letters &= set(word)

        ans = []
        for letter in letters:
            # 记录出现在所有字符串的字符的最少次数
            count = float('inf')
            for counter in counters:
                count = min(count, counter.get(letter, 0))
            # 结果数组中需要重复的字符，重复的次数为最少次数
            ans.extend([letter] * count)
        return ans

    def commonChars2(self, words: List[str]) -> List[str]:
        """ 官方答案 """
        # 由于题目保证了所有字符均为小写字母，可用长度为 26 的数组来存储字符在所有字符串中出现的次数
        min_freq = [float('inf')] * 26
        for word in words:
            # 在遍历某个字符串时，使用 freq 统计每个字符出现的次数
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            # 统计完成后，更新出现次数的最小值
            for i in range(26):
                min_freq[i] = min(min_freq[i], freq[i])

        ans = []
        for i in range(26):
            # 将 min_freq 个字符加入结果数组中
            ans.extend([chr(i + ord('a'))] * min_freq[i])
        return ans
