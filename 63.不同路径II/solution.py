# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/4 18:10
# filename    : solution.py
# description : LC 63 不同路径II

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """动态规划
        f(m, n) = f(m - 1, n) + f(m, n - 1) if obstacleGrid[m][n] != 0 else 0
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # 特殊处理起点就是障碍物的情况
        dp[0][0] = 0 if obstacleGrid[0][0] else 1
        # 初始化第一列
        for idx in range(1, m):
            # 障碍物之后的状态均为 0
            if obstacleGrid[idx][0] == 1 or dp[idx - 1][0] == 0:
                dp[idx][0] = 0
            else:
                dp[idx][0] = 1
        # 初始化第一行
        for idx in range(1, n):
            # 障碍物之后的状态均为 0
            if obstacleGrid[0][idx] == 1 or dp[0][idx - 1] == 0:
                dp[0][idx] = 0
            else:
                dp[0][idx] = 1
        for i in range(1, m):
            for j in range(1, n):
                # 如果当前位置没有障碍物，dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                # 否则 dp[i][j] = 0
                if not obstacleGrid[i][j]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def uniquePathsWithObstaclesRollingArray(self, obstacleGrid: List[List[int]]) -> int:
        """ 动态规划 + 滚动数组 """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 0 if obstacleGrid[0][0] else 1
        # 注意这里从 0 开始遍历，将初始化状态和状态转移放在一个循环中完成
        for i in range(m):
            for j in range(n):
                # 遇到障碍物，状态设为 0
                if obstacleGrid[i][j]:
                    dp[j] = 0
                # 从网格的第二行开始，通过状态转移方程更新状态
                elif obstacleGrid[i][j] == 0 and j - 1 >= 0:
                    dp[j] += dp[j - 1]
        return dp[n - 1]
