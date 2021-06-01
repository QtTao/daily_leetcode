# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/31 21:21
# filename    : solution.py
# description : LC 150 逆波兰表达式求值


from operator import add, sub, mul


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """ 栈 """
        stack = []
        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                stack.append(token)
            else:
                x, y = int(stack.pop()), int(stack.pop())
                if token == '+':
                    stack.append(x + y)
                # 注意减法和除法的顺序
                elif token == '-':
                    stack.append(y - x)
                elif token == '*':
                    stack.append(x * y)
                else:
                    stack.append(y / x)
        return int(stack[0])

    def evalRPNArray(self, tokens: List[str]) -> int:
        """ 数组模拟栈 """
        op_to_binary_fn = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': lambda x, y: int(x / y),
        }

        n = len(tokens)
        stack = [0] * ((n + 1) // 2)
        index = -1
        for token in tokens:
            try:
                num = int(token)
                index += 1
                stack[index] = num
            except ValueError:
                index -= 1
                stack[index] = op_to_binary_fn[token](stack[index], stack[index + 1])

        return stack[0]
