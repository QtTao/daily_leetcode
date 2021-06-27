# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/6/20 23:08
# filename    : solution.py
# description : LC 14 最长公共前缀


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """ 横向扫描 """
        if not strs:
            return ''
        prefix = strs[0]
        n = len(strs)
        i = 1
        while i < n:
            tmp = ''
            # 每次将公共前缀与下一个字符串进行比较
            for a, b in zip(prefix, strs[i]):
                # 如果字符匹配，将它加到临时结果中
                if a == b:
                    tmp += a
                # 否则退出循环
                else:
                    break
            # 将临时结果赋值给公共前缀，用于下一轮的比较
            if tmp:
                prefix = tmp
                i += 1
            else:
                return ''
        return prefix

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        """ 纵向扫描 """
        if not strs:
            return ''
        n, length = len(strs), len(strs[0])
        # 取第一个字符串的长度，进行纵向扫描
        for i in range(length):
            # 取第一个字符串的字符
            c = strs[0][i]
            # 如果 i 超过其中的字符串的长度，或者字符不匹配，直接返回第一个字符串前 i 部分
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, n)):
                return strs[0][:i]
        # 否则返回第一个字符串
        return strs[0]
