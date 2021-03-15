# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/15 13:39
# filename    : solution.py
# description : LC 112 路径总和

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def hasPathSumBFS(self, root: TreeNode, targetSum: int) -> bool:
        """ BFS（双队列） """
        if not root:
            return False
        # 记录节点辅助二叉树层次遍历
        nodes = [root]
        # 记录节点的加和，用于比较目标值
        vals = [root.val]
        while nodes:
            node = nodes.pop(0)
            val = vals.pop(0)
            # 到达叶子节点的时候，比较路径总和与目标值
            if not node.left and not node.right:
                if val == targetSum:
                    return True
                continue
            # 加入左子节点
            if node.left:
                nodes.append(node.left)
                # 记录路径总和
                vals.append(node.left.val + val)
            # 加入右子节点
            if node.right:
                nodes.append(node.right)
                vals.append(node.right.val + val)
        return False

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """ 递归法 """
        if not root:
            return False
        # 递归到只有一个节点的时候，直接比较 val 和 targetSum
        if not root.left and not root.right:
            return root.val == targetSum
        # 比较左子树的路径总和和右子树的路径总和与（目标值 - root.val）大小
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
