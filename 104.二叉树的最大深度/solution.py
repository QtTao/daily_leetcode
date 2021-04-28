# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/26 21:42
# filename    : solution.py
# description : LC 104 二叉树的最大深度

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """ DFS """
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1

    def maxDepthBFS(self, root: TreeNode) -> int:
        """ BFS """
        if not root:
            return 0
        # 初始化队列，先进先出
        queue = [root]
        level = 0
        while queue:
            # 记录每层节点个数
            num = len(queue)
            # 收集每层节点的所有子节点
            for _ in range(num):
                node = queue.pop(0)            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                # 层数 + 1
                level += 1
        return level
