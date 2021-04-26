# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/26 21:42
# filename    : solution.py
# description : LC 75 颜色分类


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """ 双指针（头尾） """
        # 初始头尾指针
        left, right = 0, len(nums) - 1
        # 用于遍历数组的指针
        idx = 0
        # 注意下面两个交换操作的先后顺序，必须先处理 2 再处理 0
        # 因为处理 2 的情况后，idx 对应的元素可能是 0
        while idx <= right:
            # 不断将 2 交换至数组尾部，直至 idx 对应元素不再是 2
            while idx <= right and nums[idx] == 2:
                nums[idx], nums[right] = nums[right], nums[idx]
                # 尾指针向后移动
                right -= 1
            # 如果 idx 对应元素是 0，将其交换至数组头部
            if nums[idx] == 0:
                nums[idx], nums[left] = nums[left], nums[idx]
                # 头指针向前移动
                left += 1
            # 完成 idx 对应元素的操作，继续遍历
            idx += 1

    def sortColorsOneScan(self, nums: List[int]) -> None:
        """ 双指针（前后） """
        n = len(nums)
        p0, p1 = 0, 0
        for idx in range(n):
            # 先进行 1 的交换
            if nums[idx] == 1:
                nums[idx], nums[p1] = nums[p1], nums[idx]
                # 一次交换后，p1 指针指向 1 的下一个位置
                p1 += 1
            # 再进行 0 的交换
            elif nums[idx] == 0:
                nums[idx], nums[p0] = nums[p0], nums[idx]
                # 当 1 指针领先 0 指针，说明在进行 0 的交换后，nums[idx] = 1，将 1 交换到 p1 的位置
                if p0 < p1:
                    nums[idx], nums[p1] = nums[p1], nums[idx]
                # 若 p0 和 p1 指针都发生了元素交换，所以均向前移动
                # 若只有 p0 指针发生了元素交换，由于 1 应放在 0 的后面，所以两指针也需要向前移动
                p0 += 1
                p1 += 1

    def sortColorsTwoScan(self, nums: List[int]) -> None:
        """ 单指针（两次遍历） """
        n = len(nums)
        j = 0
        # 第一次扫描，将 0 交换至数组头部
        for idx in range(n):
            if nums[idx] == 0:
                nums[j], nums[idx] = nums[idx], nums[j]
                j += 1
        # 第二次扫描，将 1 交换至 0 的后面
        for idx in range(j, n):
            if nums[idx] == 1:
                nums[j], nums[idx] = nums[idx], nums[j]
                j += 1
