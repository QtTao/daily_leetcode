# [905. 按奇偶排序数组](https://leetcode-cn.com/problems/sort-array-by-parity/solution/an-qi-ou-pai-xu-shu-zu-by-leetcode/)

`双指针`

## 双指针

利用双指针对数组进行前后遍历，在指针行进的过程中，交换奇偶的位置

### 解题思路

1. 创建双指针 `left` 和 `right`，分别指向数组的头部 `0` 和尾部 `len(A) - 1`
2. 当 `A[left]` 为奇数，`A[right]` 为偶数时，交换位置
3. 当 `A[left]` 为偶数，`left` 指针向前移动，直至指向偶数或者双指针重合
4. 当 `A[right]` 为奇数，`right` 指针向后移动，直至指向奇数或者双指针重合
5. 当双指针重合后，完成数组奇偶排序

### 复杂度

- 时间复杂度：O(N) 只需遍历一次数组
- 空间复杂度：O(1) 原地修改数组，不需要额外空间
