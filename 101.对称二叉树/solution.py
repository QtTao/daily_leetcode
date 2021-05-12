# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/11 20:33
# filename    : solution.py
# description : LC 101 对称二叉树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """ DFS """
        if not root:
            return True

        def dfs(left: TreeNode, right: TreeNode) -> bool:
            # 当左右结点都为空，则对称
            if not left and not right:
                return True
            # 当左右结点其中一个为空，另一个不为空，则不对称
            elif not left or not right:
                return False
            # 当左右结点非空，但值不同，则不对称
            elif left.val != right.val:
                return False
            # 将左结点的左子结点与右结点的右子结点比较
            # 将左结点的右子结点与右结点的左子结点比较
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root, root)

    def isSymmetricBFS(self, root: TreeNode) -> bool:
        """ BFS """
        if not root:
            return True
        queue1, queue2 = [root], [root]
        while queue1:
            left, right = queue1.pop(), queue2.pop()
            # 当左右子结点为空，比较下一个出队的结点
            if not left and not right:
                continue
            # 当一个结点为空，另一个结点非空，或者两结点的值不相同，说明非对称
            if (not left or not right) or left.val != right.val:
                return False
            # 注意结点入队顺序，由于检查的是对称性，所以首先入队的是左结点的左子结点
            queue1.append(left.left)
            # 随后是左结点的右子结点，这样在下一个循环中就能比较左结点的左子结点和右结点的右子结点
            queue1.append(left.right)
            # 右结点同理
            queue2.append(right.right)
            queue2.append(right.left)
        return True
