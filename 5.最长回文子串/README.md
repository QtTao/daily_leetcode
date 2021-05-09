# [5. 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/)

`动态规划` `Manacher`

## [动态规划](https://leetcode-cn.com/problems/longest-palindromic-substring/solution/5-zui-chang-hui-wen-zi-chuan-dong-tai-gu-p7uk/)

考虑 `dp[i][j]` 表示字符串 s 从下标 i 到 j 是否为回文串，即当 `dp[i][j] = True`，`s[i:j + 1]` 是回文串，注意回文串的中心既可以是单字符，如 `aba`，又可以是双字符，如 `abba`，那么怎么在遍历字符串的同时，更新状态呢？分三种情况进行讨论：

- Case 1 j = i，单字符必然是回文串，故 `dp[i][j] = True`
- Case 2 j - i = 1，若 `s[i] == s[j]`，那么 `dp[i][j] = True`
- Case 3 j - i >= 2，若 `s[i] == s[j]`，且 `s[i + i:j]` 是回文串，那么 `s[i: j + 1]` 也是回文串，故 故 `dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]`

由此可以，`dp[i][j]` 的更新依赖 `dp[i + 1][j - 1]` 的状态，所以**不能像普通的动态规划从上至下，再从左至右进行更新**

### 解题思路

1. 初始化 n x n 的二维状态矩阵 `dp`，值为 `False`
2. 先从左至右建立外层循环，设下标 j，其中 `j ∈ [0, n - 1]`
3. 再从上至下建立内层循环，设下标 i，其中 `i ∈ [0, j]`
4. 更新状态矩阵
    - 当 `s[i] != s[j]`，直接进入下一个循环
    - 当 `s[i] == s[j]`，有三种情况需要讨论
        - 下标 i 和下标 j 之间的字符数量不多于一个，那么 `dp[i][j] = True`
        - 如果多于一个，且下标 i 和下标 j 之间的也是回文串，那么 `dp[i][j] = True`
        - 否则 `dp[i][j] = False`，直接进入下一个循环

下面是 `babad` 的 `dp` 状态更新矩阵图例

| i/j | 0 | 1 | 2 | 3 | 4 |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 0 | True | False (ba) | True (bab) | False (baba) | False (babad) |
| 1 | - | True | False (ab) | True (aba) | False (abad) |
| 2 | - | - | True | False (ba) | False (bad) |
| 3 | - | - | - | True | False (ad) |
| 4 | - | - | - | - | True |

### 复杂度

- 时间复杂度：O(N^2) N 为字符串长度
- 空间复杂度：O(N) 使用滚动数组可以将状态矩阵缩减至一维数组

## [中心扩展](https://leetcode-cn.com/problems/longest-palindromic-substring/solution/5-zui-chang-hui-wen-zi-chuan-cc-by-bian-bian-xiong/)

中心扩展的思想是源自于回文串的特点，它的两侧互为镜像，因此回文可以从中心点向两边展开，并且最多只有 `2n - 1` 回文中心

- 单字符回文中心，一共有 `n` 个
- 双字符回文中心，一共有 `n - 1` 个

### 解题思路

1. 遍历字符串，构造回文中心的左边界 `left` 和右边界 `right`
   - 当 `left == right`，说明是单字符回文中心
   - 当 `left + 1 == right`，说明是双字符回文中心
2. 内层循环中根据 `s[left]` 和 `s[right]` 的关系，判断是否向两边扩展
   - 当 `s[left] == s[right]`，向两边扩展，即 `left -= 1; right += 1`
   - 当 `s[left] != s[right]`，结束内层循环，进入下一个回文中心

### 复杂度

- 时间复杂度：O(N^2) N 为字符串长度
- 空间复杂度：O(1)

## [Manacher 算法](https://leetcode-cn.com/problems/longest-palindromic-substring/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-bao-gu/)

`Manacher` 算法首先解决奇数和偶数长度字符串的问题，在每个字符间插入 `#`，在边界两端插入 `$` 和 `!`，用于到达边界后自动结束，经过处理后，字符串的长度永远都是奇数。

另外，算法利用数组 `f` 保存从中心扩展的最大回文半径，而且它刚好等于去掉 `#` 的原字符串的总长度减一，同时在遍历字符串时，维护当前最长回文串的中心点 `im` 和右端点 `rm`，为了找到全局最长回文串，还需要维护回文串的最大长度 `max_f`，以及该回文串的中心点  `im` 和右端点  `rm`

### 解题思路

1. 预处理字符串，插入分隔符 `#` ，首尾停止符 `$` 和 `!`
2. 遍历字符串，更新最大回文半径数组 `f[i]`
    - 当前位置 `t[i]` 在当前最长回文串的右边界左侧，那么先初始化 `f[i] = min(rm - i + 1, f[2 * im - 1])`，保证以 `t[i]` 为中心的回文串在当前最大回文串内
    - 当前位置 `t[i]` 在当前最长回文串的右边界右侧，`f[i] = 0`
3. 以 `t[i]` 为中心向两边扩展，判断 `t[i + f[i]] == t[i - f[i]]`，若条件为真，更新回文半径 `f[i] += 1`
4. 动态维护当前以 i 为中心的最长回文串，包括回文串中心 `im` 和右边界 `rm`
5. 动态维护全局最长回文串，包括回文串中心 `max_im` 和右边界 `max_rm`
6. 完成遍历后，通过回文串中心和右边界反推左边界 `2 * max_im - max_rm`，且设置切片步长为 2，跳过分隔符 `#`，返回预处理字符串的切片结果

### 复杂度

- 时间复杂度：O(N) 由于内部 `while` 循环最多只让右边界 `rm` 访问了一遍字符串，所以 `for + while` 循环需要 O(2N) 时间，另外插入分隔符和切片的时间复杂度都是 O(N)
- 空间复杂度：O(N) 保存每个中心点的最长回文半径
