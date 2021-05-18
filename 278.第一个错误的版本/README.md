# [278. 第一个错误的版本](https://leetcode-cn.com/problems/first-bad-version/solution/di-yi-ge-cuo-wu-de-ban-ben-by-leetcode/)

`二分查找`

## 二分查找

由于版本号是递增的，通过二分查找可以在每次操作中减少一般的搜索空间，故使用二分查找算法

### 解题思路

1. 计算版本序列的中间点 `mid = (left + right) // 2`
2. 当 `isBadVersion(mid)` 为 `true`，那么 `(mid, right]` 的所有版本一定不可能是第一个错误的版本，故令 `right = mid` 让下次的搜索空间为 `[left, mid]`
3. 当 `isBadVersion(mid)` 为 `false`，那么 `[left, mid]` 的所有版本都是正确的，故令 `left = mid + 1` 让下次的搜索空间为 `[mid + 1, right]`
4. 当 `left == right`，表示已经找到了第一个错误的版本

### 复杂度

- 时间复杂度：O(logN) N 为版本数，搜索空间每次减少一般
- 空间复杂度：O(1)
