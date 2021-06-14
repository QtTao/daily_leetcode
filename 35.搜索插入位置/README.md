# [35. 搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/solution/sou-suo-cha-ru-wei-zhi-by-leetcode-solution/)

`二分查找`

## [二分查找](https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/)

假设这个插入位置在数组中的下标为 `pos`，那么它成立的条件为 `nums[pos - 1] < target <= nums[pos]`，若数组中存在这个目标值，那么直接返回下标也是 `pos`，因此搜索插入位置的目标是在一个有序数组中找第一个大于等于 target 的下标。考虑使用二分查找逼近第一个大于等于 target 的下标

### 解题思路

1. 初始化 `i = 0`，`j = len(nums) - 1`，分别指向数组 `nums` 的头部和尾部
2. 通过二分查找逼近大于等于 target 的下标，其中 `mid = (i + j) // 2`
    - 当 `nums[mid] == target`，直接返回 mid
    - 当 `nums[mid] > target`，更新尾指针 `j = mid - 1`
    - 当 `nums[mid] < target`，更新头指针 `i = mid + 1`
3. 如果数组中没有跟 target 相等的数字，那么有以下三种情况
    - 当数组中所有数字都大于 target，那么循环结束时，`i = len(nums) > j = len(nums) - 1`，返回 i
    - 当数组中所有数字都小于 target，那么循环结束时，`i = 0 > j = -1`，同样返回 i
    - 当 target 在数组的内部，那么在最后一轮比较中
        - `nums[i] == nums[j] > target`，`j -= 1`，循环结束，返回 i，为第一个大于 target 的下标
        - `nums[i] == nums[j] < target`，`i += 1`，循环结束，同样返回 i

### 复杂度

- 时间复杂度：O(logN) 其中 N 为数组的长度，二分查找所需的时间复杂度
- 空间复杂度：O(1)
