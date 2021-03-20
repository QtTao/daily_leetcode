# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/20 11:02
# filename    : solution.py
# description : LC 143 重排链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """ 线性表（链表 => 线性表） """
        if not head:
            return None

        node_list = []
        node = head
        # 将链表转化成线性表，支持索引访问
        while node:
            node_list.append(node)
            node = node.next

        # 创建头尾指针
        start, end = 0, len(node_list) - 1
        while start < end:
            # 将头指针指向尾部
            node_list[start].next = node_list[end]
            # 头指针向前移动一步
            start += 1
            # 指针重叠，结束循环
            if start == end:
                break
            # 将尾指针指向第二个节点
            node_list[end].next = node_list[start]
            # 尾指针向后移动一步
            end -= 1
        # 将尾部置空
        node_list[end].next = None

    def reorderList2(self, head: ListNode) -> None:
        """
        1. 寻找中间节点
        2. 链表划分成左右两部分
        3. 右链表反转
        4. 合并左右链表
        """
        if not head:
            return None

        mid = self.find_middle_node(head)
        left = head
        right = mid.next
        # 将链表折断
        mid.next = None
        # 将右半边链表反转
        right = self.reversed_list(right)

        while left and right:
            # 保存下一个节点
            left_next, right_next = left.next, right.next
            # 头节点指向尾部节点
            left.next = right
            # 更新头节点
            left = left_next
            # 尾部节点指向更新后的头节点
            right.next = left
            # 更新尾节点
            right = right_next

    def find_middle_node(self, head: ListNode) -> ListNode:
        """ 快慢指针 """
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            # 快指针的速度是慢指针的两倍
            fast = fast.next.next
        # 当快指针到达终点时，慢指针位于中间节点
        return slow

    def reversed_list(self, head: ListNode) -> ListNode:
        tail = None
        while head:
            next = head.next
            head.next = tail
            tail = head
            head = next
        return tail

    def reorderList3(self, head: ListNode) -> None:
        """ 递归 """
        if not head or not head.next or not head.next.next:
            return None
        # 计算链表节点个数
        num = 0
        node = head
        while node:
            num += 1
            node = node.next

        self.reorder_list_recursive(head, num)

    def reorder_list_recursive(self, head: ListNode, num: int) -> ListNode:
        """ 递归调整链表节点的顺序 """
        # 递归出口 1：只有一个节点的情况
        if num == 1:
            tail = head.next
            head.next = None
            return tail
        # 递归出口 2：有两个节点的情况
        if num == 2:
            tail = head.next.next
            head.next.next = None
            return tail

        # 返回对应的尾节点，将头节点和尾节点之间的链表通过递归调整顺序
        # 递归参数处理很巧妙
        tail = self.reorder_list_recursive(head.next, num - 2)
        # 调整指针指向
        sub_head = head.next
        head.next = tail
        # 注意这里返回上一层递归中头节点对应的尾节点
        next_tail = tail.next
        tail.next = sub_head
        return next_tail
