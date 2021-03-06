# [88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/solution/he-bing-liang-ge-you-xu-shu-zu-by-leetco-rrb0/)

`双指针`

## 双指针

由于 nums1 与 nums2 已经是有序的，创建临时数组 tmp，将 nums1 和 nums2 看作队列，每次从两个数组头部取出较小的数字放到临时数组中

### 解题思路

1. 初始化 i 和 j 分别指向 nums1 和 nums2 数组的头部
2. 当 i 超过 m 或 `nums2[j] < nums1[i]` 时，其中 m 是 nums1 中有序数字的个数，将较小的 `nums2[j]` 放入临时数组中，然后 j 向前移动
3. 否则将较小的 `nums1[i]` 放入临时数组中，然后指针 j 向前移动
4. 当 `i >= m` 且 `j >= n`， 结束遍历，利用临时数组 tmp 修改 nums1

### 复杂度

- 时间复杂度：O(M + N) 双指针移动的最多为 M + N 次
- 空间复杂度：O(M + N) 临时数组需要 O(M + N) 的额外空间

## **逆向双指针**

方法一中使用临时变量的原因是如果直接合并到数组 nums1 中，数组元素可能会在取出之前就被覆盖，那么可以利用 nums1 的后半部分，直接覆盖空的部分不会影响结果，所以可以将指针设置为从后向前遍历，每次取出两个数组的较大者放到 nums1 的后面

### 解题思路

1. 初始化 tail 指针，指向 nums1 数组末尾，另外 `i, j = m - 1, n - 1`，分别指向 nums1 数组有序部分的末尾和 nums2 数组的末尾
2. 遍历两个数组，当 i 越界（小于 0），或者 `nums1[i] <= nums2[j]`，将较大的 `nums2[j]` 放进 nums1 的后面，同时指针 j 向前移动一位
3. 否则将较大的 `nums1[i]` 放进 nums1 的后面，同时指针 i 向前移动一位
4. 当指针 j 越界（小于 0），结束遍历

### 复杂度

- 时间复杂度：O(M + N) 双指针移动的最多为 M + N 次
- 空间复杂度：O(1) 需要额外空间
