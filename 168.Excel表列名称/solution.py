# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/6/27 22:28
# filename    : solution.py
# description : LC 168 Excel表列名称

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """ openpyxl.utils.get_column_letter """
        letters = []
        col_idx = columnNumber
        while col_idx > 0:
            # 计算 col_idx 被 26 相除的余数，从后向前找出列名称对应的字母
            col_idx, remainder = divmod(col_idx, 26)
            # 如果余数为 0，列名称为 Z
            if remainder == 0:
                remainder = 26
                # 这里处理很关键
                col_idx -= 1
            letters.append(chr(remainder + 64))
        # 因为是从后向前，返回结果时要反转字母
        return ''.join(reversed(letters))
