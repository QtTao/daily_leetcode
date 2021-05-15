# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/15 01:01
# filename    : solution.py
# description : LC 110 平衡二叉树

class Solution:
    def max_depth(self, root: TreeNode) -> int:
        """ 二叉树的最大深度 """
        if not root:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1

    def isBalancedTop2Bottom(self, root: TreeNode) -> bool:
        """ 从顶到底 """
        if not root:
            return True
        elif abs(self.max_depth(root.left) - self.max_depth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced(self, root: TreeNode) -> bool:
        """ 从底到顶部，需掌握 """
        is_balanced = True

        def get_height(root: TreeNode) -> int:
            nonlocal is_balanced
            # 进一步优化，当二叉树不是平衡树，直接返回结果，停止遍历
            if not root or not is_balanced:
                return 0
            # 从底部开始计算左右子树的高度
            left_height = get_height(root.left) + 1
            right_height = get_height(root.right) + 1
            # 在底部往顶部计算二叉树高度过程中，出现左右子树高度大于 1，说明不是平衡树
            if abs(left_height - right_height) > 1:
                is_balanced = False
            return max(left_height, right_height)

        get_height(root)
        return is_balanced
