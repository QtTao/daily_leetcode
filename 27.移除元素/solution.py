# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/5/15 23:25
# filename    : solution.py
# description : LC 27 移除元素

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """ 双指针 """
        # 初始化指针分别指向数组头尾，向中间移动
        left, right = 0, len(nums) - 1
        # 当左指针越过右指针时，遍历完成结束循环
        while left <= right:
            # 当左指针指向的元素等于 val，将右指针指向的元素赋值到左指针的位置，然后右指针左移一位
            # 赋值的结果依然等于 val，重新赋值操作，右指针再次左移一次，直至左指针指向的元素的值不等于 val 为止
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            # 当左指针指向元素不等于 val，左指针右移一位
            else:
                left += 1
        return left
