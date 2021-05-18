# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/18 19:27
# filename    : solution.py
# description : LC 234 回文链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """ 递归遍历 """
        self.head = head

        def check(head):
            if not head:
                return True
            # 从链表尾部开始检查是否符合回文
            if not check(head.next):
                return False
            # 如果结点值不相等，说明不是回文链表
            if self.head.val != head.val:
                return False
            # 链表结点向前移动，递归将结点向后移动
            self.head = self.head.next
            return True
        return check(head)

    def isPalindrome(self, head: ListNode) -> bool:
        """ 快慢指针 + 反转链表 """
        if not head:
            return True

        # 找到链表的中间结点
        mid_node = self.find_middle_node(head)
        # 将右半部分链表反转
        right_half = self.reverse(mid_node.next)

        is_palindrome = True
        left_half = head
        while is_palindrome and right_half:
            # 判断是否回文
            if left_half.val != right_half.val:
                is_palindrome = False
            left_half, right_half = left_half.next, right_half.next

        # 还原链表
        mid_node.next = self.reverse(right_half)
        return is_palindrome

    def find_middle_node(self, head: ListNode) -> ListNode:
        """ 链表的中间结点 """
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 如果链表长度为奇数，slow 指向中间结点
        # 如果链表长度为偶数，slow 指向中间两个结点靠左的一个
        return slow

    def reverse(self, head: ListNode) -> ListNode:
        """ 反转链表 """
        tail = None
        cur = head
        while cur:
            next = cur.next
            cur.next = tail
            tail = cur
            cur = next
        return tail
