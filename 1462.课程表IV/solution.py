# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/6/8 00:11
# filename    : solution.py
# description : LC 1462 课程表IV（可采用 Floyd 算法）


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        is_reachable = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        for first, second in prerequisites:
            # 先修 first 课程，才能修 second 课程
            is_reachable[first][second] = True
            # 遍历所有课程，找出与 first 和 second 的所有依赖关系
            for course in range(numCourses):
                # 如果 first 课程依赖当前课程，即 current -> first，结合 first -> second，得到 current -> second
                if is_reachable[course][first]:
                    # 所以从当前课程可以到达 second 课程
                    is_reachable[course][second] = True
                # 如果当前课程依赖 second 课程，即 second -> second，结合 first -> second，得到 first -> current
                if is_reachable[second][course]:
                    # 所以从 first 课程可以到达当前课程
                    is_reachable[first][course] = True
        # 根据 prerequisites 找出所有课程通路后，再对 queries 中关系进行判断
        return [is_reachable[first][second] for first, second in queries]
