# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/10 00:55
# filename    : solution.py
# description : LC 20 有效的括号

class Solution:
    def isValid(self, s: str) -> bool:
        """ 栈 """
        stack = []
        for i in s:
            if i in '(':
                stack.append(')')
            elif i in '[':
                stack.append(']')
            elif i in '{':
                stack.append('}')
            # Case 1 ']' 栈为空
            # Case 2 '()]' 栈也为空
            # Case 3 '(]' 栈非空，但右括号不能匹配
            elif not stack or i != stack.pop():
                return False
        # Case 4 '[' 栈非空，但没有右括号进行匹配
        return not bool(stack)

    def isValidDict(self, s: str) -> bool:
        """ 栈 + 哈希表 """
        # 添加 ? 是为了避免空栈的情况
        stack = ['?']
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']',
            '?': '?'
        }
        for i in s:
            if i in brackets:
                stack.append(i)
            # Case 1 ']' ']' != '?'
            # Case 2 '()]' ']' != '?'
            # Case 3 '(]' ')' != ']'
            elif i != brackets[stack.pop()]:
                return False
        # Case 4 '[' stack = ['?', '['] 左括号 ( 没有匹配成功
        return len(stack) == 1
