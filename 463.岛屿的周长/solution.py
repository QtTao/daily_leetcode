# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/24 13:06
# filename    : solution.py
# description : LC 463 岛屿的周长


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """ 迭代 """
        m, n = len(grid), len(grid[0])
        num = 0
        for i in range(m):
            for j in range(n):
                # 遇到水域，跳过
                if grid[i][j] == 0:
                    continue
                # 遇到陆地，遍历陆地的上下左右四个位置，如果不是陆地，周长 + 1
                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        continue
                    num += 1
        return num

    def islandPerimeterDFS(self, grid: List[List[int]]) -> int:
        """ DFS """
        m, n = len(grid), len(grid[0])

        def dfs(grid: List[List[int]], i: int, j: int):
            """ 深度优先遍历岛屿中的所有陆地 """
            # 超出网格范围，周长 + 1
            if not (0 <= i < m and 0 <= j < n):
                return 1
            # 从陆地移动到水域，周长 + 1
            elif grid[i][j] == 0:
                return 1
            # 已遍历过的陆地，对周长无影响
            elif grid[i][j] == 2:
                return 0
            else:
                # 标记陆地已遍历
                grid[i][j] = 2
                # 统计当前位置为中心的上下左右的位置的周长
                return dfs(grid, i - 1, j) + dfs(grid, i + 1, j) + dfs(grid, i, j - 1) + dfs(grid, i, j + 1)

        for i in range(m):
            for j in range(n):
                # 根据题意，只包含一个岛屿，所以只需计算一个即可
                if grid[i][j] == 1:
                    return dfs(grid, i, j)
