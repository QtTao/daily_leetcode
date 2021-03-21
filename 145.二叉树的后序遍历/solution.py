# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/21 15:19
# filename    : solution.py
# description : LC 145 二叉树的后序遍历

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversalRecursive(self, root: TreeNode) -> List[int]:
        """ 递归遍历 """
        if not root:
            return []

        def postorder(root: TreeNode, order: List[int]):
            if not root:
                return None
            # 左子树遍历
            postorder(root.left, order)
            # 右子树遍历
            postorder(root.right, order)
            # 最后的根节点
            order.append(root.val)

        order = []
        postorder(root, order)
        return order

    def postorderTraversalNonRecursive1(self, root: TreeNode) -> List[int]:
        """ 非递归遍历1 """
        if not root:
            return []

        node = root
        # 记录完成排序的节点
        prev_node = node
        order = []
        stack = []
        while stack or node:
            # 收集左子树节点
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            # 如果当前节点没有右子树或者右子树已经完成排序，那么将当前节点加入排序结果
            if not node.right or node.right == prev_node:
                order.append(node.val)
                # 记录当前节点已完成排序
                prev_node = node
                # 将当前节点置空，避免重复左子树的遍历
                node = None
            # 如果当前节点右子树，将当前节点重新压入栈中，并开始遍历右子树
            else:
                stack.append(node)
                node = node.right
        return order

    def postorderTraversalNonRecursive2(self, root: TreeNode) -> List[int]:
        """ 非递归遍历 2 """
        order = []
        stack = [(root, False)]
        while stack:
            root, is_visited = stack.pop()
            if root is None:
                continue
            if is_visited:
                # 入栈两次后，已访问状态为 True，输出节点值
                order.append(root.val)
            else:
                # 后序遍历：左 => 右 => 中
                # 入栈顺序：中 => 右 => 左
                stack.append((root, True))
                stack.append((root.right, False))
                stack.append((root.left, False))
        return order

    def postorderTraversalMorris(self, root: TreeNode) -> List[int]:
        """ Morris 遍历 """
        dummy = TreeNode(0)
        dummy.left = root
        order = []
        curr_node = dummy
        while curr_node:
            if curr_node.left is None:
                curr_node = curr_node.right
            else:
                node = curr_node.left
                while node.right and node.right != curr_node:
                    node = node.right

                if node.right is None:
                    node.right = curr_node
                    curr_node = curr_node.left
                else:
                    order += self.trackback(curr_node.left, node)
                    node.right = None
                    curr_node = curr_node.right
        return order

    def trackback(self, frm, to):
        order = []
        curr_node = frm
        while curr_node != to:
            order.append(curr_node.val)
            curr_node = curr_node.right
        order.append(to.val)
        order.reverse()
        return order
