# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/15 12:19
# filename    : solution.py
# description : LC 111 二叉树的最小深度

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """ DFS """
        # 递归结束条件
        if not root:
            return 0
        # 如果左子结点为空，只计算右子树的最小深度
        elif not root.left:
            return self.minDepth(root.right) + 1
        # 如果右子结点为空，只计算左子树的最小深度
        elif not root.right:
            return self.minDepth(root.left) + 1
        # 只有当左子结点和右子结点非空时候，才比较左右子树的深度，取最小值 + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def minDepthBFS(self, root: TreeNode) -> int:
        """ BFS """
        if not root:
            return 0

        queue = [(root, 1)]
        while queue:
            node, depth = queue.pop(0)
            # 当遇到叶结点时候，中止循环，直接返回
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
