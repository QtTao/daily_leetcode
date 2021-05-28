# [139. 单词拆分](https://leetcode-cn.com/problems/word-break/solution/dan-ci-chai-fen-by-leetcode-solution/)

`动态规划`

## [动态规划](https://leetcode-cn.com/problems/word-break/solution/dong-tai-gui-hua-ji-yi-hua-hui-su-zhu-xing-jie-shi/)

`dp` 表示字符串 s 的前 i 个字符是否能被空格拆分成若干个字典中出现的单词，状态转移方程可以表述为当 s 的前 i 位可以用 wordDict 表示，即 `dp[i] = True`，那么 `dp[j]`（其中 j 在区间 `[i + 1, n)`）可以表示为 `dp[i] and s[i:j] in wordDict`
，只有当 `dp[i]` 可以用 wordDict 表示，且 `s[i,...,j]` 出现在 wordDict 中，才能说明 s 的前 j 位可以被表示

### 解题思路

1. 初始化状态为 `dp = [False,...,False]`，一共 N + 1 个状态，表示 s 的前 i 位是否可以用 wordDict 中的单词表示
2. 设置 `dp[0] = True` 表示空字符能被表示，也能保证状态转移方程最开始通过判断，触发转移
3. 开始遍历字符串 s，开始索引为 i，区间为 `[0, n)`，同时遍历结束索引 j，区间为 `[i + 1, n]`
    - 当 `dp[i] = True` 且 `s[i,...,j]` 在 wordDict 中，`dp[j] = True`，说明 s 的前 j 位能用 wordDict 的单词表示

### 复杂度

- 时间复杂度：O(N^2) N 为字符串的长度，一共有 N 个状态需要计算，每次计算需要遍历 N 个分割点
- 空间复杂度：O(N) 需要 O(N) 空间来存放 dp 状态

## **回溯**

### 解题思路（回溯算法比较难理解）

1. 建立记忆化函数 `backtrack`，并缓存计算的结果
2. 当 s 长度为 0，表示已经使用 wordDict 的单词分割完成，返回 True
3. 遍历分割索引 i，在区间中 `[1, n]` 中
    - 当 `s[0,...,i - 1]` 在 wordDict 中，且 `(backtrack(s[i,...n - 1])` 可以用 wordDict 中的单词来表示，那么 s 就能被表示
    - 在递归过程中遍历分割索引 i 过程，有可能会多次计算 `backtrack(s[i,...n - 1])`，容易发生超时，所以采用 `fuctools.lru_cache` 装饰器最近最少使用算法缓存计算结果

### 复杂度

- 时间复杂度：O(N^2) N 为字符串的长度，递归深度为 N，每次回溯是需要经历 N 次循环
- 空间复杂度：O(N) 递归调用栈深度为 N
