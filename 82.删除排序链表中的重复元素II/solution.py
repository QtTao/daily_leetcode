# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/30 00:49
# filename    : solution.py
# description : LC 82 删除排序链表中重复元素II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        # 因为头节点可能会被删除，所以使用哑节点
        dummy = ListNode(0, head)
        cur_node = dummy
        # next 和 next.next 有可能为空节点
        while cur_node.next and cur_node.next.next:
            if cur_node.next.val == cur_node.next.val:
                # 获取相等的值，用作后续节点值的比较
                val = cur_node.next.val
                # 跳过所有值相等的节点
                while cur_node.next and cur_node.next.val == val:
                    # 节点往后移动，直至找到相邻节点值不相同
                    cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        return dummy.next
