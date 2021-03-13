# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/13 20:38
# filename    : solution.py
# description : LC 236 二叉树的最近公共祖先

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ 二叉树后序遍历（递归法） """
        # 当 root 为空或者 p 或 q 节点其中一个就是 root，则直接返回 root
        # 这也是递归终止条件
        if not root or root == p or root == q:
            return root
        # 后序遍历，返回左子树的最近公共祖先，可能是 None，也可能是 p 或 q 节点
        left = self.lowestCommonAncestor(root.left, p, q)
        # 返回右子树的最近公共祖先，可能是 None，也可能是 q 或 p 节点
        right = self.lowestCommonAncestor(root.right, p, q)
        # 当左子树的最近公共祖先为空，返回右子树的
        if not left:
            return right
        # 当右子树的最近公共祖先为空，返回左子树的
        if not right:
            return left
        # p 节点和 q 节点分属两侧，返回根节点
        return root

    def lowestCommonAncestorHashtable(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ 哈希表法  """
        parents = {root: None}
        seen = {}

        # 后序遍历存储所有节点的父节点
        def dfs(root):
            # 先判断是否有左节点
            if root.left:
                # root.left 的父节点是 root
                parents[root.left] = root
                dfs(root.left)
            if root.right:
                # root.right 的父节点是 root
                parents[root.right] = root
                dfs(root.right)

        dfs(root)
        # 从 p 节点往上溯源，并记录已经访问过的节点，其中肯定存在最近公共祖先节点
        while p:
            seen[p] = True
            # 父节点溯源
            p = parents[p]
        # 从 q 节点往上溯源
        while q:
            # 判断是否有某个节点已经访问过，若有立即返回结果（最近公共祖先）
            if seen.get(q):
                return q
            q = parents[q]
        return None
