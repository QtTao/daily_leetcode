# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/28 18:55
# filename    : solution.py
# description : LC 146 LRU 缓存机制


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # 哈希表
        self.hashmap = {}
        # 创建伪头部和伪尾部节点
        self.head = DListNode()
        self.tail = DListNode()
        # 初始化双向链表
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """ 获取节点 """
        if key in self.hashmap:
            # 将节点移动到链表头部
            self.move_node_to_head(key)
            node = self.hashmap[key]
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """ 新增节点 """
        if key in self.hashmap:
            # 更新哈希表中链表节点值
            node = self.hashmap[key]
            node.value = value
            #  移动节点至链表头部
            self.move_node_to_head(key)
        else:
            # 超出链表或哈希表容量
            if len(self.hashmap) >= self.capacity:
                # 移除最久未使用节点
                self.pop()
            self.add_node_to_head(key, value)

    def move_node_to_head(self, key):
        """ 移动节点至链表头部 """
        node = self.hashmap[key]
        # 关联 node 前后两个节点
        node.prev.next = node.next
        node.next.prev = node.prev
        # 将 node 插入到链表头部
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def add_node_to_head(self, key, value):
        """ 在链表头部新增节点 """
        node = DListNode(key=key, value=value)
        self.hashmap[key] = node
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def pop(self):
        """ 移除尾部节点（最久未使用） """
        last_node = self.tail.prev
        # 注意需要删除哈希表中的对应节点
        self.hashmap.pop(last_node.key)
        # 移除最久未使用的节点
        last_node.prev.next = self.tail
        self.tail.prev = last_node.prev
        return last_node


class DListNode:
    """ 双向链表节点 """

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
