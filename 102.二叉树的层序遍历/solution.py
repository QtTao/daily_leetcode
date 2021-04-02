# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/2 16:34
# filename    : solution.py
# description : LC 102 二叉树的层序遍历


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """ BFS 队列 """
        if not root:
            return []

        queue = [root]
        order = []
        while queue:
            # 保存当前层的所有节点
            level = []
            # queue 的长度随着节点的入队而变化，所以使用固定的 n，表明当前层的节点个数
            # 将当前层的子节点全部入队，再进行统计
            n = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            order.append(level)

        return order

    def levelOrderRecursion(self, root: TreeNode) -> List[List[int]]:
        """ DFS 递归 """
        if not root:
            return []

        order = []

        def dfs(level, node):
            if len(order) <= level:
                # 初始化空列表，用于保存遍历的节点值
                order.append([])
            # 将当前节点加入排序结果中，level 代表当前层
            order[level].append(node.val)
            # 递归遍历左右子树，同时将层数 + 1
            if node.left:
                # 深度优先，首先遍历所有左子节点，并加入排序结果中
                dfs(level + 1, node.left)
            if node.right:
                # 在归时候，补充右节点
                dfs(level + 1, node.right)

        dfs(0, root)
        return order

    def levelOrderStack(self, root: TreeNode) -> List[List[int]]:
        """ DFS 迭代（等价于 levelOrderRecursion） """
        if not root:
            return []

        order = []
        # 从根节点开始，第 0 层
        stack = [(root, 0)]
        # 前序遍历
        while stack:
            node, level = stack.pop()
            if len(order) <= level:
                order.append([])
            order[level].append(node.val)
            # 右子节点先入栈
            if node.right:
                stack.append((node.right, level + 1))
            # 左子节点先入栈
            if node.left:
                stack.append((node.left, level + 1))
        return order
