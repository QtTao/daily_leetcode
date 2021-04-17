# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/15 14:07
# filename    : solution.py
# description : LC 105 从前序与中序遍历序列构造二叉树


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """ 递归 """
        hashmap = {}
        # 利用哈希表存储中序数组的值和下标，快速定位下标
        for idx, val in enumerate(inorder):
            hashmap[val] = idx

        def _buildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int) -> TreeNode:
            """基于数组下标的递归遍历
            preorder_left: 左或右子树在前序数组的起始位置
            preorder_right: 左或右子树在前序数组的结束位置
            inorder_left: 左或右子树在中序数组的起始位置
            inorder_right: 左或右子树在中序数组的结束位置
            """
            # 递归结束条件，起始位置超过结束位置，返回空节点
            if preorder_left > preorder_right or inorder_left > inorder_right:
                return None
            # 根节点的值
            val = preorder[preorder_left]
            # 创建根节点
            root = TreeNode(val=val)

            # 中序遍历根节点的下标
            inorder_root = hashmap[val]
            # 左子树的节点个数
            size_of_left_tree = inorder_root - inorder_left
            # 这里要小心数组下标的计算
            # 前序遍历左子树区间 [根节点的下一个位置, preorder_left + 左子树的节点数]
            # 中序遍历左子树区间 [inorder_left, 根节点的前一个位置]
            root.left = _buildTree(preorder_left + 1, preorder_left + size_of_left_tree, inorder_left, inorder_root - 1)
            # 前序遍历右子树区间为完整数组 - 根节点 - 左子树区间
            # 中序遍历右子树区间 [根节点的后一个位置， inorder_right]
            root.right = _buildTree(preorder_left + size_of_left_tree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root

        n = len(preorder)
        return _buildTree(0, n - 1, 0, n - 1)

    def buildTreeIteration(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """ 迭代法 """
        root = TreeNode(val=preorder[0])
        # 用栈来记录尚未考虑右节点的节点
        stack = [root]
        inorder_idx = 0
        for idx in range(1, len(preorder)):
            # 记录前序数组中右节点的值
            val = preorder[idx]
            node = stack[-1]
            # 比较栈顶元素与中序数组元素，如果不相同，说明是左子树节点
            if node.val != inorder[inorder_idx]:
                node.left = TreeNode(val=val)
                # 入栈
                stack.append(node.left)
            else:
                # 当栈顶元素与中序数组元素相同，不断弹出栈顶元素，找出祖先节点
                while stack and stack[-1].val == inorder[inorder_idx]:
                    node = stack.pop()
                    inorder_idx += 1
                # 跳出循环，找到右节点的祖先节点
                node.right = TreeNode(val)
                # 右节点入栈
                stack.append(node.right)
        return root
