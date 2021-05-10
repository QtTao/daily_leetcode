# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/10 17:14
# filename    : solution.py
# description : LC 617 合并二叉树

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """ DFS """
        if not root1:
            return root2
        if not root2:
            return root1
        node = TreeNode(val=root1.val + root2.val)
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)
        return node

    def mergeTreesBFS(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """ BFS """
        if not root1:
            return root2
        if not root2:
            return root1

        root = TreeNode(val=root1.val + root2.val)
        queue, queue1, queue2 = [root], [root1], [root2]
        while queue:
            n = len(queue)
            for _ in range(n):
                node, node1, node2 = queue.pop(), queue1.pop(), queue2.pop()
                for side in ['left', 'right']:
                    self.merge_subtrees(node, node1, node2, queue, queue1, queue2, side=side)
        return root

    def notnone_node(self, node):
        """ 非 Node 节点 """
        if node is None:
            return TreeNode(val=0)
        return node

    def merge_subtrees(self, node, node1, node2, queue, queue1, queue2, side='left'):
        """ 构造左/右子树 """
        if getattr(node1, side) or getattr(node2, side):
            side1, side2 = self.notnone_node(getattr(node1, side)), self.notnone_node(getattr(node2, side))
            setattr(node, side, TreeNode(val=side1.val + side2.val))
            queue1.append(side1)
            queue2.append(side2)
            queue.append(getattr(node, side))
