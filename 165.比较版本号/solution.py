# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/5 20:12
# filename    : solution.py
# description : LC 165 比较版本号

class Solution:
    def compareVersionSplitString(self, version1: str, version2: str) -> int:
        """ 字符串分割，逐个比较 """
        v1, v2 = version1.split('.'), version2.split('.')
        m, n = len(v1), len(v2)

        for idx in range(max(m, n)):
            # 如果 idx 超出数组范围，用 0 比较
            item1 = int(v1[idx]) if idx < m else 0
            item2 = int(v2[idx]) if idx < n else 0
            if item1 > item2:
                return 1
            elif item1 < item2:
                return -1
        return 0

    def compareVersion(self, version1: str, version2: str) -> int:
        """ 双指针 """
        p1, p2 = 0, 0
        n1, n2 = len(version1), len(version2)

        while p1 < n1 or p2 < n2:
            chunk1, p1 = self.get_next_chunk(version1, n1, p1)
            chunk2, p2 = self.get_next_chunk(version2, n2, p2)
            if chunk1 > chunk2:
                return 1
            elif chunk1 < chunk2:
                return -1
        return 0

    def get_next_chunk(self, version: str, n: int, p: int) -> List[int]:
        """ 寻找每一块以及下一块的起始位置 """
        if p >= n:
            return 0, p
        end = p
        # 寻找每一块的结尾指针
        while end < n and version[end] != '.':
            end += 1
        item = int(version[p:end])
        # 下一块的起始位置
        p = end + 1
        return item, p
