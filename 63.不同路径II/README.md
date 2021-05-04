# [63. 不同路径II](https://leetcode-cn.com/problems/unique-paths-ii/solution/bu-tong-lu-jing-ii-by-leetcode-solution-2/)

`动态规划`

## 动态规划

区别于 [62.不同路径](https://leetcode-cn.com/problems/unique-paths/solution/bu-tong-lu-jing-by-leetcode-solution-hzjf/), 这里的状态转移方程 `f(m, n)` 为

- 0 `obstacleGrid[m][n] = 0`
- `f(m - 1, n) + f(m, n - 1)` `obstacleGrid[m][n] != 0`

需要注意的地方是初始化状态的时候，**遇到障碍物之后的状态均为 0**

### 解题思路

1. 分别初始化二维状态矩阵的首行和首列状态
2. 通过 m x n 双层循环更新矩阵状态
    - 当遇到障碍物时，状态 `dp[i][j]` = 0
    - 正常情况下，状态 `dp[i][j] = dp[i - 1][j] + dp[i][j - 1]`
3. 由于状态 (i, j) 只跟 (i - 1, j) 和 (i, j - 1) 有关，所以可以利用滚动数组进行空间复杂度优化，降低至 O(n)

### 复杂度

- 时间复杂度：O(mn)
- 空间复杂度：O(n) n 为网格的列数
