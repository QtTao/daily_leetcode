# [69. x 的平方根](https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode-solution/)

`二分查找` `数学`

## 二分查找

`x` 的平方的整数部分满足 `k^2 <= x` 的最大 `k` 值，可以考虑在 `[0, x)` 的范围内对 `k` 进行二分查找

### 解题思路

1. 计算中间元素 `mid = (right - left) // 2 + left`，其中第一轮循环中 `right = x left = 0`
2. 比较 `mid` 的平方与 `x` 的大小
    - 如果比 `x` 大，更新右边界 `right -= 1`
    - 否则记录当前 `mid`（可行解），并更新左边界 `left += 1`
3. 当 `left` 和 `right` 重合时，重复步骤 2，再次比较 `mid` 与 `x` 大小， 直至左边界大于右边界

### 复杂度

- 时间复杂度：O(logN) 二分查找复杂度
- 空间复杂度：O(1)

## [牛顿迭代法](https://zh.wikipedia.org/wiki/牛顿法#求解最值問題)

`x` 的平方根实质上是求 `f(x) = x^2 - c` 的零点，根据牛顿迭代法，切线方程的解可以写成 `xn+1 = xn - f(xn) / f'(xn) = xn - (xn^2 - c) / 2xn = (xn + c/xn) / 2`，当 `xn+1 = xn`
即为 `x^2 - c = 0` 的根

### 解题思路

1. 初始化 `xn` 和 `c` 为 `x`
2. 根据公式计算 `xn+1 = (xn + c/xn) / 2`
3. 将 `xn+1` 带入上述公式中 `xn`，反复迭代直至 `abs(xn+1 - xn)` 差距足够小
4. 可以认为 `xn` 就是 `x` 的平方根的近似解

### 复杂度

- [时间复杂度](https://en.citizendium.org/wiki/Newton's_method#Computational_complexity): O(logN) 这里的 N 为精度位数，不是迭代次数
- 空间复杂度：O(1)
