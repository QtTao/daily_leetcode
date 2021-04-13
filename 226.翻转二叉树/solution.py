# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/12 21:48
# filename    : solution.py
# description : LC 226 翻转二叉树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """ DFS 递归（后序遍历） """
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root

    def invertTreeDFSNonRecursive(self, root: TreeNode) -> TreeNode:
        """ DFS 非递归（前序遍历） """
        if not root:
            return root
        # 显式调用栈
        stack = [root]
        while stack:
            # 栈后进先出
            node = stack.pop()
            # 翻转左右子树
            left, right = node.left, node.right
            node.left, node.right = right, left
            # 右子节点先入栈
            if node.right:
                stack.append(node.right)
            # 左子节点后入栈，先出栈
            if node.left:
                stack.append(node.left)
        return root

    def invertTreeBFS(self, root: TreeNode) -> TreeNode:
        """ BFS（层序遍历） """
        if not root:
            return root
        # 引入队列
        queue = [root]
        while queue:
            # 队列先进先出
            node = queue.pop(0)
            # 翻转左右子树
            left, right = node.left, node.right
            node.left, node.right = right, left
            # 左子节点先入队
            if node.left:
                queue.append(node.left)
            # 右子节点后入队
            if node.right:
                queue.append(node.right)
        return root
