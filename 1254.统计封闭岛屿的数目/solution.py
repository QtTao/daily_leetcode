# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/25 11:55
# filename    : solution.py
# description : LC 1254 统计封闭岛屿的数目

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """ DFS """
        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> bool:
            """ 深度优先搜索某一个岛屿中的所有陆地 """
            # 如果岛屿的四周超出网格范围，说明不是封闭岛屿
            if not (0 <= i < m and 0 <= j < n):
                return False
            # 如果当前位置是水域或者已访问的陆地，说明当前岛屿还是封闭的
            elif grid[i][j] != 0:
                return True
            else:
                # 如果当前位置是未访问的陆地，向四周搜索，同时标记为已访问
                grid[i][j] = 2
                # 只有四周都被水域包围才算是封闭岛屿
                return all([dfs(i - 1, j), dfs(i + 1, j), dfs(i, j - 1), dfs(i, j + 1)])

        num = 0
        for i in range(m):
            for j in range(n):
                # 当遇到陆地，开始深度优先遍历
                if grid[i][j] == 0 and dfs(i, j):
                    num += 1
        return num

    def closedIslandBFS(self, grid: List[List[int]]) -> int:
        """ BFS """
        m, n = len(grid), len(grid[0])

        def bfs(i: int, j: int) -> bool:
            """ 广度优先搜索某一个岛屿中的所有陆地 """
            queue = [(i, j)]
            # 注意不能遇到网格边界，就停止搜索，因为需要标记陆地的访问记录
            is_closed = True
            while queue:
                x, y = queue.pop(0)
                # 超出网格边界，不是封闭岛屿
                if not (0 <= x < m and 0 <= y < n):
                    is_closed = False
                # 当前位置是水域或者已访问的陆地，继续搜索其他区域
                elif grid[x][y] != 0:
                    continue
                else:
                    # 标记已访问，同时将四周位置加入队列，等待下一轮搜索
                    grid[x][y] = 2
                    queue.extend([
                        (x - 1, y),
                        (x + 1, y),
                        (x, y - 1),
                        (x, y + 1)
                    ])
            return is_closed

        num = 0
        for i in range(m):
            for j in range(n):
                # 封闭岛屿，数量加一
                if grid[i][j] == 0 and bfs(i, j):
                    num += 1
        return num
