# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/24 23:35
# filename    : solution.py
# description : LC 695 岛屿的最大面积

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """ DFS """
        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int):
            """ 深度优先搜索一个岛屿中的所有陆地，计算其面积 """
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                nonlocal area
                # 当 (i, j) 是陆地，面积 + 1
                area += 1
                # 标记为已访问
                grid[i][j] = 2
                # 搜索上方
                dfs(i - 1, j)
                # 搜索下方
                dfs(i + 1, j)
                # 搜索左边
                dfs(i, j - 1)
                # 搜索右边
                dfs(i, j + 1)

        max_area = 0
        for i in range(m):
            for j in range(n):
                # 跳过水域和已访问过的陆地
                if grid[i][j] != 1:
                    continue
                area = 0
                # 深度优先搜索岛屿
                dfs(i, j)
                if area > max_area:
                    max_area = area
        return max_area
