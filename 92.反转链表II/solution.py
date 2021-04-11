# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/10 18:50
# filename    : solution.py
# description : LC 92 反转链表II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode):
        """ LC 206 反转链表 """
        tail = None
        while head:
            next = head.next
            head.next = tail
            tail = head
            head = next

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """ 朴素解法 """
        if left == right:
            return head
        # 创建哑节点
        dummy = ListNode(next=head)

        # 从哑节点出发，到达 left 节点的前驱节点，需要 left - 1 步
        pre_node = dummy
        for _ in range(left - 1):
            pre_node = pre_node.next

        # 从 left 节点的前驱节点出发，前进 right - left + 1 步
        right_node = pre_node
        for _ in range(right - left + 1):
            right_node = right_node.next

        # 截取需要反转链表范围
        left_node = pre_node.next
        next_node = right_node.next
        pre_node.next = None
        right_node.next = None
        # 反转链表
        self.reverseList(left_node)
        # 拼接链表
        pre_node.next = right_node
        left_node.next = next_node
        return dummy.next

    def reverseBetweenOnce(self, head: ListNode, left: int, right: int) -> ListNode:
        """ 头插法（一次遍历） """
        dummy = ListNode(next=head)
        pre_node = dummy
        # 从哑节点出发，前进 left - 1 步到达 left 节点的前驱节点
        for _ in range(left - 1):
            pre_node = pre_node.next

        cur_node = pre_node.next
        # 从 left 节点的后继节点开始操作头插法，所以只需操作 right - left 次
        # 完成一次操作之后， cur_node 被后移一位
        for _ in range(right - left):
            next_node = cur_node.next
            cur_node.next = next_node.next
            next_node.next = pre_node.next
            pre_node.next = next_node
        return dummy.next
