# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/31 20:27
# filename    : solution.py
# description : LC 382 链表随机节点

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random


class Solution:
    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        """ Reservoir Sampling """
        # 记录结点数目
        n = 1
        val = None
        node = self.head
        while node:
            # 以 1 / n 的概率更新结点值，(n - 1) / n 不更新结点值
            if random.randrange(0, n) < 1:
                val = node.val
            n += 1
            # 指针向前移动
            node = node.next
        return val
