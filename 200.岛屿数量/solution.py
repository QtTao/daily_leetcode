# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/22 12:32
# filename    : solution.py
# description : LC 200 岛屿数量


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """ DFS """
        m, n = len(grid), len(grid[0])

        def dfs(grid: List[List[str]], i: int, j: int):
            """ 递归遍历形成岛屿的所有陆地，并标记已访问 """
            # 若当前坐标已超出网格范围，或当前位置是海洋，或者是已发现的陆地，停止遍历
            if (not 0 <= i < m) or (not 0 <= j < n) or grid[i][j] in ('0', '2'):
                return None
            # 否则当前位置是陆地，首先标记已访问
            grid[i][j] = '2'
            # 遍历下方
            dfs(grid, i + 1, j)
            # 遍历上方
            dfs(grid, i - 1, j)
            # 遍历左边
            dfs(grid, i, j - 1)
            # 遍历右边
            dfs(grid, i, j + 1)

        num = 0
        for i in range(m):
            for j in range(n):
                # 若发现陆地，说明有岛屿
                if grid[i][j] == '1':
                    num += 1
                    dfs(grid, i, j)
        return num

    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        """ BFS """
        m, n = len(grid), len(grid[0])

        def bfs(grid, i, j):
            """ 把将要访问的陆地入队出队，来遍历形成岛屿的所有陆地 """
            queue = [(i, j)]
            while queue:
                i, j = queue.pop(0)
                if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                    # 标记已访问
                    grid[i][j] = '2'
                    # 将该陆地上下左右的陆地加入队列中，等待访问
                    queue.extend([(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)])

        num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num += 1
                    bfs(grid, i, j)
        return num
