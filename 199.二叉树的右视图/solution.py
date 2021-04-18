# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/17 22:34
# filename    : solution.py
# description : LC 199 二叉树的右视图

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """ 前序遍历，递归（从右子树开始） """

        def dfs(node: TreeNode, depth: int):
            if not node:
                return None
            # 小技巧：当 depth 正好与数组长度相等，那么 root 就是 depth + 1 层次的第一个节点
            # 例如第一次进入下列条件判断时，depth = 0，数组长度为 0，root 为第一层的第一个节点，故加入右视图数组中
            if depth == len(rv):
                rv.append(node.val)
            depth += 1
            # 先递归遍历右子树
            dfs(node.right, depth)
            # 再遍历左子树
            dfs(node.left, depth)

        rv = []
        dfs(root, 0)
        return rv

    def rightSideViewBFS(self, root: TreeNode) -> List[int]:
        """ 层序遍历（从右子树开始） """
        if not root:
            return []
        queue = [root]
        rv = []
        while queue:
            n = len(queue)
            for idx in range(n):
                node = queue.pop(0)
                if idx == 0:
                    rv.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return rv

    def rightSideViewDFSNonRecursion(self, root: TreeNode) -> List[int]:
        """ 前序遍历，非递归（从右子树开始） """
        stack = [(root, 0)]
        rv = []
        while stack:
            node, depth = stack.pop()
            if node:
                # 此处的判断很巧妙，具体分析过程见递归版本
                if depth == len(rv):
                    rv.append(node.val)
                # 左节点先入栈后出栈
                stack.append((node.left, depth + 1))
                # 右节点后入栈先出栈
                stack.append((node.right, depth + 1))
        return rv
