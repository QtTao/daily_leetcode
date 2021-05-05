# [647. 回文子串](https://leetcode-cn.com/problems/palindromic-substrings/solution/hui-wen-zi-chuan-by-leetcode-solution/)

`动态规划` `Manacher`

## [动态规划](https://leetcode-cn.com/problems/palindromic-substrings/solution/shu-ju-jie-gou-he-suan-fa-dong-tai-gui-h-3bms/)

假定 `dp[i][j]` 表示字符串中从下标 i 到 j 是否为回文串，如果 `dp[i][j] = True`，则表示是回文串，否则不是回文串，进一步分析各种情况

- 当 i = j，单字符必定是回文串，故 `dp[i][j] = True`
- 当 j - i = 1，若 `s[i] == s[j]`，两个相同字符也是回文串，故 `dp[i][j] = (s[i] == s[j])`
- 当 j - i >= 2，若 `s[i] == s[j]`，且 `s[i + 1:j]` 也是回文串，那么 `s[i:j + 1]` 也是回文串，故 `dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]`

综上所述，回文子串转化成动态规划问题，这里需要注意 `dp[i][j]` 依赖 `dp[i + 1][j - 1]` 的状态，更新状态时遍历的方向可以先从左往右，然后从上往下进行

### 解题思路

1. 初始化 n x n 二维状态矩阵 `dp`，值为 False
2. 先从左往右建立外层循环，设下标为 j，其中 `j ∈ [0, n - 1]`
3. 然后从上往下建立内层循环，设下标为 i，注意下标 i <= 下标 j，其中 `i ∈ [0, j]`
4. 当 `s[i] != s[j]`，说明 `dp[i][j] = False`，由于初始值就是 False，这里可以直接进入下一个循环
5. 当 `s[i] == s[j]`，这里有三种情况需要考虑
    - 下标 i 和下标 j 之间的字符数量不多于一个，那么 `dp[i][j] = True`
    - 如果多于一个，且下标 i 和下标 j 之间的也是回文串，那么 `dp[i][j] = True`
    - 否则 `dp[i][j] = False`，直接进入下一个循环

### 复杂度

- 时间复杂度：O(N^2) 其中 N 为字符串长度
- 空间复杂度：O(N) 通过滚动数组可以将空间降低至一维数组

## 中心扩展

### 解题思路

### 复杂度

- 时间复杂度：
- 空间复杂度：

## Manacher 算法

### 解题思路

### 复杂度

- 时间复杂度：
- 空间复杂度：


