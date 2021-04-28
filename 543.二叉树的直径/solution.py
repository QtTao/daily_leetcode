# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/27 18:55
# filename    : solution.py
# description : LC 543 二叉树的直径


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def get_depth(root: TreeNode) -> int:
            """ 计算二叉树深度 """
            if not root:
                return 0

            # 计算左子树深度
            left_depth = get_depth(root.left)
            # 计算右子树深度
            right_depth = get_depth(root.right)
            # 二叉树的直径 = 所有节点的左子树深度与右子树深度之和的最大值
            self.diameter = max(left_depth + right_depth, self.diameter)
            # 加上根节点，深度加一
            return max(left_depth, right_depth) + 1

        get_depth(root)
        return self.diameter
