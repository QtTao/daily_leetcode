# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/10 23:14
# filename    : solution.py
# description : LC 876 链表的中间结点

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNodeArray(self, head: ListNode) -> ListNode:
        """ 链表转换数组 """
        node_list = []
        node = head
        while node:
            if node:
                node_list.append(node)
            node = node.next
        return node_list[len(node_list) // 2]

    def middleNode(self, head: ListNode) -> List:
        """ 快慢指针 """
        slow = fast = head
        # while fast and fast.next 当结点个数为偶数， slow 会停留在靠右的中间结点
        # while fast.next and fast.next.next 当结点个数为偶数， slow 会停留在靠左的中间结点
        while fast and fast.next:
            # fast 指针的速度是 slow 指针的两倍
            slow = slow.next
            fast = fast.next.next
        # 当 fast 指针到达链表尾部时，slow 位于链表的中间结点
        return slow
