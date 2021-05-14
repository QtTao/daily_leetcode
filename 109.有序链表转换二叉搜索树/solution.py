# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/14 00:23
# filename    : solution.py
# description : LC 109 有序链表转换二叉搜索树

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedListToBSTArray(self, head: ListNode) -> TreeNode:
        """ 链表转换数组 """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def dfs(left: int, right: int):
            """ 前序遍历构建二叉搜索树 """
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(val=nums[mid])
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root

        return dfs(0, len(nums) - 1)

    def find_middle_node(self, left: ListNode, right: List) -> ListNode:
        """ 寻找链表中间结点 """
        slow = fast = left
        while fast != right and fast.next != right:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortedListToBSTDPointers(self, head: ListNode) -> TreeNode:
        """ 快慢指针 """

        def dfs(left: ListNode, right: List) -> TreeNode:
            """ 前序遍历构建二叉搜索树 """
            if left == right:
                return None
            # [left, right) 左闭右开
            mid = self.find_middle_node(left, right)
            root = TreeNode(val=mid.val)
            root.left = dfs(left, mid)
            root.right = dfs(mid.next, right)
            return root

        return dfs(head, None)

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """ 通过长度范围（高度平衡）和链表元素升序的特点（二叉搜索树的中序遍历）进行优化 """

        def get_length(head: ListNode) -> int:
            """ 借助数组的特点，通过 length 控制子树的范围 """
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        def in_order_dfs(left: int, right: int) -> TreeNode:
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode()
            # 遍历链表，模拟中序遍历
            # 先访问左子树
            root.left = in_order_dfs(left, mid - 1)
            # 然后访问根结点
            nonlocal head
            root.val = head.val
            head = head.next
            # 最后访问右子树
            root.right = in_order_dfs(mid + 1, right)
            return root

        length = get_length(head)
        return in_order_dfs(0, length - 1)
