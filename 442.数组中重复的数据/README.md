# [442. 数组中重复的数据](https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/solution/shu-zu-zhong-zhong-fu-de-shu-jian-dan-bi-utnm/)

## 数组索引标记

### 解题思路

根据题意，数组元素值在 `[1, n] n 为数组的长度` 的范围内，正好与数组索引范围重合，所以利用数组索引存储数组元素值，而元素值可以用于标记是否已被访问，标记方法是取相反数（或者赋值为 0）

1. 遍历数组，并将第 `num` 个数置为 `-num`，标记为已访问
2. 当第 `num` 个数为负数，表示出现重复数

### 复杂度

- 时间复杂度：O(N) 一次遍历
- 空间复杂度：O(1) 利用索引原地修改数组
