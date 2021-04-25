# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/25 22:14
# filename    : solution.py
# description : LC 47 全排列II

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        rv, temp = [], []
        visited = [False for _ in range(n)]
        # 预先排序，让相同的元素放在一起，便于剪枝
        nums.sort()

        def backtrack():
            # 到达回溯树的底部
            if len(temp) == n:
                rv.append(temp[:])
            for idx in range(n):
                # 理解这里的剪枝条件
                # 条件一：用过的元素不能再使用
                # 条件二：当前元素和前一个元素值相同，并且前一个元素还没有被使用，否则得到的排列结果是重复的
                if visited[idx] or (idx > 0 and nums[idx] == nums[idx - 1] and not visited[idx - 1]):
                    continue
                # 加入临时排列数组
                temp.append(nums[idx])
                # 标记为已访问
                visited[idx] = True
                backtrack()
                # 弹出临时数组
                temp.pop()
                # 撤销已访问标记
                visited[idx] = False

        backtrack()
        return rv
