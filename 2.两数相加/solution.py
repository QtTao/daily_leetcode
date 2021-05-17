# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/16 13:05
# filename    : solution.py
# description : LC 2 两数相加


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """ 链表遍历 """
        dummy = ListNode()
        head = dummy
        carry = 0
        while l1 or l2:
            # 根据两个链表对应的结点存在情况，计算两数之和
            if l1 and l2:
                num = l1.val + l2.val + carry
                l1, l2 = l1.next, l2.next
            elif l1:
                num = l1.val + carry
                l1 = l1.next
            else:
                num = l2.val + carry
                l2 = l2.next

            carry, val = num // 10, num % 10
            head.next = ListNode(val=val)
            head = head.next
        # 保留进位的节点
        if carry:
            head.next = ListNode(val=carry)
        return dummy.next
