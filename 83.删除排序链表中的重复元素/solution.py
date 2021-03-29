# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/29 13:56
# filename    : solution.py
# description : LC 83 删除排序链表中的重复元素

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        # 保存当前节点和下一个节点
        prev_node, node = head, head.next
        while node:
            if prev_node.val != node.val:
                prev_node = node
            # 如果相邻两个节点的值相同，那么跳过该节点
            else:
                prev_node.next = node.next
            # 往前移动
            node = node.next
        return head
