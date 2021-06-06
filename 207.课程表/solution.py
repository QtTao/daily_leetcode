# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/6/5 14:46
# filename    : solution.py
# description : LC 207 课程表

from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """ BFS """
        # 邻接表：存储每一个没有任何先修课程的课程的（去重后的）后续课程
        edges = defaultdict(set)
        # 入度数组：记录所有后续课程的先修课程数，初始化为 0
        indegrees = [0] * numCourses

        # 更新邻接表和入度数组
        for second, first in prerequisites:
            indegrees[second] += 1
            edges[first].add(second)

        # 先手机所有入度为 0 的课程加入队列中，即没有先修课程的课程
        queue = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        visited = 0
        # 入度为 0 的课程开始往后续课程遍历，直至队列为空，所有课程完成遍历，得到拓扑排序结果
        while queue:
            course = queue.pop(0)
            visited += 1
            # 遍历队首课程的所有后续课程，入度减 1
            # 如果课程入度降至 0，加入队列中，
            for adjacency in edges[course]:
                indegrees[adjacency] -= 1
                if indegrees[adjacency] == 0:
                    queue.append(adjacency)
        return visited == numCourses

    def canFinishDFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """ DFS """
        # 邻接表
        edges = defaultdict(set)
        # 状态数组：记录每个课程的状态，分别为未搜索 0，搜索中 1 和已完成 2
        visited = [0] * numCourses

        # 更新邻接表
        for second, first in prerequisites:
            edges[first].add(second)

        # 标记是否存在环形依赖
        self.can_finish = True

        def dfs(course):
            visited[course] = 1
            for adjacency in edges[course]:
                # 在遍历相邻课程时候，如果状态为搜索中，说明有环形依赖，不存在拓扑排序
                if visited[adjacency] == 1:
                    self.can_finish = False
                    return None
                # 状态为未搜索，深度优先搜索它的相邻课程
                elif visited[adjacency] == 0:
                    dfs(adjacency)
                    # 如果它的某一个相邻课程的状态为搜索中，即不存在拓扑排序
                    if not self.can_finish:
                        return None
                # 状态为已完成，直接跳过
                else:
                    continue
            # 所有相邻课程已搜索完成，将当前课程状态标记为已完成
            visited[course] = 2
            return None

        for course in range(numCourses):
            # 深度优先搜索所有未搜索的课程
            if self.can_finish and visited[course] == 0:
                dfs(course)
        return self.can_finish
