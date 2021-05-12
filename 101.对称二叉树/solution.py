# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/11 20:33
# filename    : solution.py
# description : LC 101 对称二叉树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """ DFS """
        if not root:
            return True

        def dfs(left: TreeNode, right: TreeNode) -> bool:
            # 当左右结点都为空，则对称
            if not left and not right:
                return True
            # 当左右结点其中一个为空，另一个不为空，则不对称
            elif not left or not right:
                return False
            # 当左右结点非空，但值不同，则不对称
            elif left.val != right.val:
                return False
            # 将左结点的左子结点与右结点的右子结点比较
            # 将左结点的右子结点与右结点的左子结点比较
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root, root)

    def isSymmetricBFS(self, root: TreeNode) -> bool:
        """ BFS """
        pass
