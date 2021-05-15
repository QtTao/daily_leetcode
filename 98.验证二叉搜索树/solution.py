# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/15 19:05
# filename    : solution.py
# description : LC 98 验证二叉搜索树


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    is_valid = True
    min_val = float('-inf')

    def isValidBST(self, root: TreeNode) -> bool:
        """ DFS（中序遍历，递归版） """
        if not root:
            return True

        def inorder_dfs(root: TreeNode):
            """ 中序遍历 """
            if not root or not self.is_valid:
                return None
            inorder_dfs(root.left)
            if root.val > self.min_val:
                self.min_val = root.val
            else:
                self.is_valid = False
            inorder_dfs(root.right)

        inorder_dfs(root)
        return self.is_valid

    def isValidBSTDFS(self, root: TreeNode) -> bool:
        """ DFS（自底而上） """

        def dfs(root, lower=float('-inf'), upper=float('inf')) -> bool:
            """ 加深递归函数的如何设计的理解 """
            if not root:
                return True
            val = root.val
            # 自底而上验证二叉搜索树
            # 验证二叉树的左子树，在 (lower, root.val) 范围内
            if not dfs(root.left, lower, val):
                return False
            # 验证二叉树的右子树，在 (root.val, upper) 范围内
            if not dfs(root.right, val, upper):
                return False
            # 最后验证根结点
            if not (lower < val < upper):
                return False
            return True

        return dfs(root)

    def isValidBSTNonRecursion(self, root: TreeNode) -> bool:
        """ DFS（中序遍历，非递归） """
        stack, min_val = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果当前结点值小于等于前一个结点值，说明不是二叉搜索树
            if root.val <= min_val:
                return False
            min_val = root.val
            root = root.right

        return True
