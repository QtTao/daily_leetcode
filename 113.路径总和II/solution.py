# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/16 11:32
# filename    : solution.py
# description : LC 113 路径总和II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSumDFS(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        """ 二叉树前序遍历（双栈） """
        if not root:
            return []
        nodes = [root]
        paths = [[root.val]]
        rv = []
        while nodes:
            # 推出栈顶
            node = nodes.pop()
            path = paths.pop()
            # 遇到叶子节点，比较路径总和与目标值
            if not node.left and not node.right:
                if sum(path) == targetSum:
                    rv.append(path)
                else:
                    continue

            # 右子节点入栈
            if node.right:
                nodes.append(node.right)
                # 列表 + 列表 -> 创建新列表
                paths.append(path + [node.right.val])

            # 左子节点入栈
            if node.left:
                nodes.append(node.left)
                paths.append(path + [node.left.val])
        return rv

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        """ 递归 """
        rv, paths = [], []

        def path_sum_dfs(root: TreeNode, target_sum: int):
            if not root:
                return None
            paths.append(root.val)
            # 遇到叶子节点，比较路径总和与目标值
            if not root.left and not root.right:
                if target_sum == root.val:
                    # 拷贝当前路径，否则列表最后会被清空
                    rv.append(paths[:])
            # 每次访问一个节点，创建新列表记录节点值
            path_sum_dfs(root.left, target_sum - root.val)
            path_sum_dfs(root.right, target_sum - root.val)
            # 这个弹出操作很巧妙，当 root.left 和 root.right 都是空，说明 root 是叶子节点，访问完毕后弹出栈
            # 继续遍历该叶子节点的父节点的其他子节点
            paths.pop()

        path_sum_dfs(root, targetSum)
        return rv
