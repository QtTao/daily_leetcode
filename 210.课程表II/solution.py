# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/6/6 13:19
# filename    : solution.py
# description : LC 210 课程表II

from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """ BFS """
        # 邻接表：保存每个课程的所有后续课程
        edges = defaultdict(list)
        # 入度表：保存每个课程的先修课程数
        indegrees = [0] * numCourses

        # 更新邻接表和入度表
        for second, first in prerequisites:
            edges[first].append(second)
            indegrees[second] += 1

        # 将入度为 0 的课程加入队列中
        queue = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        # BFS 广度优先搜索
        ans = []
        while queue:
            course = queue.pop(0)
            ans.append(course)

            # 遍历 course 的所有后续课程
            for adjacency in edges[course]:
                # 入度减 1
                indegrees[adjacency] -= 1
                # 如果入度等于 0，加入队列中
                if indegrees[adjacency] == 0:
                    queue.append(adjacency)
        # 如果排序的长度等于课程数，说明排序完成，否则课程存在环形依赖
        if len(ans) == numCourses:
            return ans
        return []

    def findOrderDFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """ DFS """
        # 邻接表：存储每门课程的所有后续课程
        edges = defaultdict(list)
        # 状态数组，分别为未搜索 0，搜索中 1 和已完成 2
        visited = [0] * numCourses
        # 更新邻接表
        for second, first in prerequisites:
            edges[first].append(second)

        # 拓扑排序结果
        self.ans = []
        # 是否存在循环依赖
        self.valid = True

        def dfs(course):
            # 将课程标记为搜索中
            visited[course] = 1
            # 遍历所有后续课程
            for adjacency in edges[course]:
                # 如果状态为未搜索，那么搜索它的后续课程
                if visited[adjacency] == 0:
                    dfs(adjacency)
                    if not self.valid:
                        return None
                # 如果状态为搜索中，说明存在循环依赖
                elif visited[adjacency] == 1:
                    self.valid = False
                    return None
            # 将状态标记为已完成
            visited[course] = 2
            # 将课程入栈，注意课程入栈顺序
            self.ans.append(course)
            return None

        # 每次循环挑选一个未搜索的课程，进行深度优先搜索
        for course in range(numCourses):
            if self.valid and visited[course] == 0:
                dfs(course)
        if not self.valid:
            return []
        # 尤其注意下标 0 为栈底，需将数组反转输出
        return self.ans[::-1]
