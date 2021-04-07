# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/6 11:16
# filename    : solution.py
# description : LC 225 用队列实现栈

class MyStack:

    def __init__(self):
        """ 初始化队列 """
        self.queue = []

    def push(self, x: int) -> None:
        """ 压入栈顶 """
        n = len(self.queue)
        # 最新元素入队
        self.queue.append(x)
        # 在此前入队的元素出队并重新入队
        for _ in range(n):
            self.queue.append(self.queue.pop(0))

    def pop(self) -> int:
        """ 弹出栈顶 """
        return self.queue.pop(0)

    def top(self) -> int:
        """ 访问栈顶元素 """
        return self.queue[0]

    def empty(self) -> bool:
        """ 栈是否空 """
        return not self.queue
