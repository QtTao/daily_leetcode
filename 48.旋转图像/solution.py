# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/5 21:14
# filename    : solution.py
# description : LC 48 旋转图像


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """ 两次翻转：水平 + 主对角线 """
        n = len(matrix)

        # 水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]

        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotateonce(self, matrix: List[List[int]]) -> None:
        """ 一次旋转 """
        n = len(matrix)

        # 注意索引的枚举范围，分奇偶两种情况
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                # 四角交换
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = temp
