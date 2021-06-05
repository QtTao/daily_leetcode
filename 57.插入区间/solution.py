# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/6/5 00:43
# filename    : solution.py
# description : LC 57 插入区间

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        ans = []
        flag = False
        for li, ri in intervals:
            # 当前区间在插入区间的右侧，且无交集
            if li > right:
                if not flag:
                    ans.append([left, right])
                    flag = True
                ans.append([li, ri])
            # 当前区间在插入区间的左侧，且无交集
            elif ri < left:
                ans.append([li, ri])
            # 与插入区间有交集，更新插入区间的左右端点
            else:
                left = min(left, li)
                right = max(right, ri)
        if not flag:
            ans.append([left, right])
        return ans
