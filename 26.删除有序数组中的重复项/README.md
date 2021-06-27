# [26. 删除有序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/shan-chu-pai-xu-shu-zu-zhong-de-zhong-fu-tudo/)

`双指针`

## 双指针

### 解题思路

1. 初始化 i 指针用于遍历 nums 数组元素，而 j 指针用于指向已排序的元素
2. num 为当前最新的排序元素
3. 遍历 nums 数组元素，若当前的元素跟当前最新的排序元素不同
    - 将当前元素加入排序结果
    - 更新 `j = j + 1`
    - 更新最新排序元素 `num = nums[i]`
4. 当 `i >= len(nums)`，直接返回 j，这是因为处理完最后一个排序元素后，j + 1 刚好等于删除重复有序数组后的数组长度

### 复杂度

- 时间复杂度：O(N) 其中 N 为数组长度，i 和 j 指针最多移动 N 次
- 空间复杂度：O(1)
