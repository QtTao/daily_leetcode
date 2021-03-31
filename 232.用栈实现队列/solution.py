# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/31 11:56
# filename    : solution.py
# description : LC 232 用栈实现队列


class MyQueue:

    def __init__(self):
        """ 初始化输入栈和输出栈 """
        self.stack_input = []
        self.stack_output = []
        self.front = None

    def push(self, x: int) -> None:
        """ 把元素压入输入栈 """
        if not self.stack_input:
            self.front = x
        self.stack_input.append(x)

    def pop(self) -> int:
        """ 弹出输出栈元素 """
        if not self.stack_output:
            while self.stack_input:
                self.stack_output.append(self.stack_input.pop())
        return self.stack_output.pop()

    def peek(self) -> int:
        """  访问输出栈栈顶元素 """
        if self.stack_output:
            return self.stack_output[-1]
        return self.front

    def empty(self) -> bool:
        """ 栈是否为空 """
        return not bool(self.stack_input or self.stack_output)
