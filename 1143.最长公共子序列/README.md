# [1143. 最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/solution/zui-chang-gong-gong-zi-xu-lie-by-leetcod-y7u0/)

`动态规划`

## 动态规划

状态假设：`dp[i + 1][j + 1]` 为 text1 的前 i 个字符和 text2 的前 j 的字符，形成的最长公共子序列长度，那么

- 当 `text1[i] == text2[j]` 时，`dp[i + 1][j + 1] = dp[i - 1][[j - 1]` 代表使用 `text1[i]` 与 `text2[j]` 形成最长公共子序列的长度
- 当 `text1[i] != text2[j]` 时，`dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])` 代表不使用 `text1[i]` 形成最长公共子序列的长度、不使用 `text2[j]` 形成最长公共子序列的长度，取两者中的最大值

### 解题思路

假设 `n1` 为 text1 的长度，`n2` 为 text2 的长度

1. 初始化 `(n1 + 1, n2 + 1)` 二维 dp 矩阵，赋值为零
2. 建立双层循环 `range(n1) * range(n2)`
3. 分情况计算 `dp[i + 1][j + 1]`
    - 当 `text1[i] == text2[j]` 时，`dp[i + 1][j + 1] = dp[i - 1][[j - 1]`
    - 当 `text1[i] != text2[j]` 时，`dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])`

### 演算过程

| | 初始值 | a | c | e |
| --- |--- | --- | --- | --- |
| 初始值 | 0 | 0 | 0 | 0 |
| a | 0 | 1 | 0 | 0  |
| b | 0 | 1 | 1 | 1 |
| c | 0 | 1 | 2 | 2  |
| d | 0 | 1 | 2 | 2  |
| e | 0 | 1 | 2 | 3  |

### 复杂度

- 时间复杂度：O(NM) 其中 N 和 M 分别是字符串 text1 和 text2 的长度
- 空间复杂度：O(NM) 使用 (N + 1) * (M + 1) 的二维矩阵
