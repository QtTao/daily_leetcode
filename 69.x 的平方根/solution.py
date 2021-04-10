# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/10 14:41
# filename    : solution.py
# description : LC 69 x 的平方根

class Solution:
    def mySqrt(self, x: int) -> int:
        """ 二分查找 """
        ans = -1
        left, right = 0, x
        # 注意这里的条件包含等号，当 left = right，仍然需要判断是否小于等于 x
        # 小于等于 x，left 被采纳，否则保持上一个循环的 ans
        while left <= right:
            # 计算中间值
            mid = (right - left) // 2 + left
            # 如果中间值的平方小于等于 x，那么更新结果值和左边界
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            # 否则更新右边界
            else:
                right = mid - 1
        return ans

    def mySqrtNewton(self, x: int) -> int:
        """ 牛顿迭代法 """
        if x <= 1:
            return x
        c, x0 = float(x), float(x)
        while True:
            # 牛顿迭代公式
            xi = 0.5 * (x0 + c / x0)
            # 当 x0 = x1，即为 x^2 - c = 0 的根
            if abs(x0 - xi) < 1e-7:
                return int(x0)
            x0 = xi
