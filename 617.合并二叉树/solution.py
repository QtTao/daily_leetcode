# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/10 17:14
# filename    : solution.py
# description : LC 617 合并二叉树

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """ DFS """
        if not root1:
            return root2
        if not root2:
            return root1
        node = TreeNode(val=root1.val + root2.val)
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)
        return node

    def mergeTreesBFS(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """ BFS """
        pass
