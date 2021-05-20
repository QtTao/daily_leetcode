# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/20 00:12
# filename    : solution.py
# description : LC 160 相交链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNodeHash(self, headA: ListNode, headB: ListNode) -> ListNode:
        """ 哈希表 """
        seen = set()
        while headA:
            seen.add(headA)
            headA = headA.next
        while headB:
            if headB in seen:
                return headB
            headB = headB.next
        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """ 快慢指针 """
        if not headA or not headB:
            return None
        head1, head2 = headA, headB
        while head1 != head2:
            # 从 headA 出发遍历链表
            if head1:
                head1 = head1.next
            # 如果 headA 遍历结束，重定位至 headB
            else:
                head1 = headB
            # 从 headB 出发遍历链表
            if head2:
                head2 = head2.next
            # 如果 headB 遍历结束，重定位至 headA
            else:
                head2 = headA
        # head1 和 head2 走过的结点数相同，且相遇于相交结点
        return head1
