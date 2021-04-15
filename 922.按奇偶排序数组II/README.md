# [922. 按奇偶排序数组II](https://leetcode-cn.com/problems/sort-array-by-parity-ii/solution/an-qi-ou-pai-xu-shu-zu-ii-by-leetcode-solution/)

`双指针`

## 双指针

利用双指针分别指向奇数位和偶数位，实现原地修改数组

### 解题思路

1. 遍历数组偶数指针 `even_idx ∈ [0, 2, ...]`
2. 当遇到偶数指针 `even_idx` 指向奇数时，开始遍历数组奇数指针 `odd_idx ∈ [1, 3, ...]`，直至奇数指针遇到偶数
3. 交换偶数指针和奇数指针对应的元素，重复步骤 1，2，完成数据的遍历

### 复杂度

- 时间复杂度：O(N) N 为数组长度
- 空间复杂度：O(1)
