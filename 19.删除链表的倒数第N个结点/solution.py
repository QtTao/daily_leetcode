# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/4 23:01
# filename    : solution.py
# description : LC 19 删除链表的倒数第N个结点

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEndArray(self, head: ListNode, n: int) -> ListNode:
        """ 将链表转换成数组，支持下标索引 """
        node_list = []
        node = head
        # 创建哑节点，减少判断
        dummy = ListNode(next=head)
        # 保存数组
        while node:
            node_list.append(node)
            node = node.next

        deleted_node = node_list[-1 * n]
        next = deleted_node.next
        # 删除头节点
        if len(node_list) == n:
            dummy.next = next
        # 删除其他节点
        else:
            prev_node = node_list[-1 * n - 1]
            prev_node.next = next
        return dummy.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """ 双指针 """
        dummy = ListNode(next=head)
        # 起点处，front 指针领先 back 指针一个位置
        front = head
        back = dummy

        # front 指针前进 n 个位置
        for _ in range(n):
            front = front.next
        # 同步前进，直至 front 指针到达链表尾部
        # back 正好位于倒数第 n 个节点的前一个节点
        while front:
            front = front.next
            back = back.next
        # 删除节点
        back.next = back.next.next
        return dummy.next
