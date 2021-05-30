# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/29 21:03
# filename    : solution.py
# description : LC 138 复制带随机指针的链表

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def __init__(self):
        # 保存新旧结点的映射关系
        self.visited_nodes = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        """ 回溯 + 哈希表 """
        # 当结点为空，返回 None
        if head is None:
            return None

        # 如果当前结点已经访问过，直接返回它对应的全新结点
        # 这里主要用于 random 指向结点，因为 next 指针先处理
        if head in self.visited_nodes:
            return self.visited_nodes[head]

        # 创建新结点
        node = Node(head.val)
        # 保存新旧结点的关系
        self.visited_nodes[head] = node

        # 先顺序拷贝下一个结点
        node.next = self.copyRandomList(head.next)
        # 后逆序拷贝 random 指针指向的结点
        node.random = self.copyRandomList(head.random)

        return node

    def get_cloned_node(self, node):
        """ 从哈希表中搜索访问过的结点 """
        if not node:
            return None
        # 如果当前结点没有访问过，那么创建新结点，并加入哈希表中
        if node not in self.visited_nodes:
            self.visited_nodes[node] = Node(node.val)
        return self.visited_nodes[node]

    def copyRandomList2(self, head: 'Node') -> 'Node':
        """ 链表遍历 + 哈希表 """
        if not head:
            return None
        # 初始化 dummy 结点，next 指针指向深拷贝的新结点
        dummy = Node(0, next=self.get_cloned_node(head))
        new_head = dummy.next
        while head:
            # 遍历链表，并拷贝结点，包括 next 和 random 指针指向的结点
            new_head.next = self.get_cloned_node(head.next)
            new_head.random = self.get_cloned_node(head.random)
            # 指针向前移动
            head = head.next
            new_head = new_head.next
        return dummy.next

    def copyRandomList3(self, head: 'Node') -> 'Node':
        """ 链表遍历 + 使用原始链表进行关联 （copyRandomList2 的空间优化版） """
        if not head:
            return None

        old_node = head
        # 将复制的新结点插入到两结点中间
        while old_node:
            # 深拷贝结点
            new_node = Node(old_node.val)
            # 将新结点插入到原始链表中，位置在前后两个结点的中间
            new_node.next = old_node.next
            old_node.next = new_node
            old_node = new_node.next

        old_node = head
        # 复制随机指针
        while old_node:
            if old_node.random:
                # 新结点 new_node = old_node.next
                # new_node.random 指向的结点是 old_node.random 指向的下一个结点，即 new_node.random = old_node.random.next
                old_node.next.random = old_node.random.next
            else:
                old_node.next.random = None
            old_node = old_node.next.next

        # 拆分和还原链表
        # 将 A -> A' -> B -> B' -> C -> C'
        # 拆分成原始链表 A -> B -> C 和深拷贝链表 A' -> B' -> C'
        old_node = head
        new_node = head.next
        dummy = Node(0, next=new_node)
        while old_node:
            old_node.next = old_node.next.next
            # 由于新链表的最后一个结点肯定是 new_node，所以需要对 new_node.next 是否为空进行判断，再进行赋值
            new_node.next = new_node.next.next if new_node.next else None
            old_node = old_node.next
            new_node = new_node.next
        return dummy.next
