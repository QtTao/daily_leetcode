# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/11 00:02
# filename    : solution.py
# description : LC 100 相同的树


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """ DFS """
        # Case 1 两二叉树同一位置的结点为空
        if not p and not q:
            return True
        # Case 2 两二叉树同一位置的其中一个结点为空
        elif not p or not q:
            return False
        # Case 3 两二叉树的结点值不相同
        elif p.val != q.val:
            return False
        else:
            # Case 4 比较左右子树是否相同
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTreeBFS(self, p: TreeNode, q: TreeNode) -> bool:
        """ BFS """
        # 判断二叉树头结点是否相同
        if not p and not q:
            return True
        elif not p or not q:
            return False
        # 头结点入队
        queue1, queue2 = [p], [q]
        while queue1:
            # 结点出队
            node1, node2 = queue1.pop(), queue2.pop()
            # 首先判断同一位置的结点的值是否相同
            if node1.val != node2.val:
                return False
            # 判断左子结点是否为空，如果两左子结点为非空，入队
            left1, left2 = node1.left, node2.left
            if left1 and left2:
                queue1.append(left1)
                queue2.append(left2)
            # 否则不是相同的树
            elif (not left1 and left2) or (not left2 and left1):
                return False
            # 判断右子结点是否为空，如果两右子结点为非空，入队
            right1, right2 = node1.right, node2.right
            if right1 and right2:
                queue1.append(right1)
                queue2.append(right2)
            elif (not right1 and right2) or (not right2 and right1):
                return False
        # 两队必然相同为空，且对应结点的值都相同，所以是相同的树
        return True
