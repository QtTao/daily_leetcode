# [1462. 课程表IV](https://leetcode-cn.com/problems/course-schedule-iv/solution/an-ti-shi-zuo-by-abear-2-rvm7/)

`Floyd`

## 搜索

此题可以采用 `Floyd` 算法来解决，具体实现方法可参考[这里](https://leetcode-cn.com/problems/course-schedule-iv/solution/pythonshuang-bai-floyd-warshall-transitive-closure/)

### 解题思路

1. 初始化 `is_reachable` 记录课程之间是否有通路，默认值为 False
2. 遍历 prerequisites 所有课程依赖关系，如果课程 i 是课程 j 的先修课程，那么设 `is_reachable[i][j] = True`
3. 在内层中遍历所有课程，找出与课程 i 和课程 j 有关的所有课程，有以下两种情况
    - 如果当前课程 k 是课程 i 的先修课程，即 `is_reachable[k][i] = True`，那么课程 k 同样是课程 j 的先修课程，设 `is_reachable[k][j] = True`
    - 如果课程 j 是当前课程 k 的先修课程，即 `is_reachable[j][k] = True`，那么课程 i 同样是课程 k 的先修课程，设 `is_reachable[i[k] = True`
4. 完成 prerequisites 的遍历后，得到记录任意两个课程之间是否有通路的二维数组 `is_reachable`
5. 基于二维数组 `is_reachable`，判断 `queries` 中的依赖关系是否存在

### 复杂度

- 时间复杂度：O(N * M) 其中 N 为 prerequisites 的长度，而 M 是课程数量
- 空间复杂度：O(M^2) 需要 M^2 的空间来记录任意两个课程之间是否有通路
