# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/21 14:59
# filename    : solution.py
# description : LC 125 验证回文串

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """ 双指针 """
        if not s:
            return True
        start, end = 0, len(s) - 1
        while start < end:
            if not s[start].isalnum() or not s[end].isalnum():
                if not s[start].isalnum():
                    start += 1
                if not s[end].isalnum():
                    end -= 1
            elif s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False
        return True

    def isPalindrome2(self, s: str) -> bool:
        """ 字符串预处理 + 反转 """
        new = ''.join(i.lower() for i in s if i.isalnum())
        return new == new[::-1]
