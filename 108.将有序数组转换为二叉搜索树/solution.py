# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/12 22:18
# filename    : solution.py
# description : LC 108 将有序数组转换为二叉搜索树


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """ DFS """
        def dfs(left, right):
            # 当 left 下标大于 right 下标，说明数组已经遍历完毕，直接返回空结点
            if left > right:
                return None
            # 取中间靠左的数字作为根结点
            # 保证每个结点的左右两个子树的高度差的绝对值不超过 1
            mid = (left + right) // 2
            # 模拟中序遍历
            root = TreeNode(val=nums[mid])
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root
        return dfs(0, len(nums) - 1)
