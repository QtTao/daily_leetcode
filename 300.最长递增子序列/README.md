# [300. 最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/)

`动态规划` `二分查找` `贪心算法`

## 动态规划

### 解题思路

1. 定义状态，如果直接使用子序列的长度作为状态，状态转移难以确定，原因是不知道子序列中包含了什么元素，不符合动态规划中的[无后效性](https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/)
    - `dp[i]` 表示以 `nums[i]` 结尾的递增子序列的长度，这里 `nums[i]` 必须是子序列的最后一个元素
    - 这样设计可以确定 `nums[i]` 必需选中，满足无后效性
2. 状态转移方程
    - 如果 `nums[i]` 严格大于它位置之前的某个数，那么步骤一定义的状态长度加一，然后比较出从位置 0 到 i 的最大值，即 `dp[i] = max(dp[i], dp[j] + 1)`
    - 如果 `nums[i]` 小于等于它位置之前的数，不属于递增子序列，不处理
3. 初始状态
    - 将初始状态的 `dp[i]` 置为 1，表示每个元素至少可以单独成为子序列，长度为 1
4. 返回值
    - 计算所有 `nums[i]` 结尾的递增子序列的最大长度就是最长递增子序列的长度

### 复杂度

- 时间复杂度：O(N^2) 双层遍历
- 空间复杂度：O(N) 保持以数组中每个元素结尾的状态

## [贪心算法 + 二分查找](https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-e/)

### 解题思路

1. 创建数组保存最长递增子序列
2. 当遇到比数组的所有元素还要大（严格），当前最长递增子序列长度加一
3. 当遍历的元素没有严格大于数组中所有元素，那么**用它来替换比它大，但最小的那个元素**，目的是让后续元素有更大可能加入到最长递增子序列中
4. 数组的长度即最长递增子序列的长度，但注意该数组未必是真实的最长递增子序列

### 复杂度

- 时间复杂度：O(NlogN) = O(N) 遍历原数组 * O(logN) 二分查找元素在新建数组中位置
- 空间复杂度：O(N) 保存最长递增子序列的数组
