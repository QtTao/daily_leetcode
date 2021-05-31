# [382. 链表随机节点](https://leetcode-cn.com/problems/linked-list-random-node/solution/xu-shui-chi-chou-yang-suan-fa-by-jackwener/)

`Reservoir Sampling`

## Reservoir Sampling

当内存无法加载全部数据时，如何从包含未知大小的数据流中随机选取 k 个数据，并且要保证每个数据被抽取的概率相等，具体的证明方法可以参考[这里](../398.随机数索引/README.md)

### 解题思路

1. 初始化 `n = 1` 用于记录链表结点个数，`val = None` 表示最终返回链表结点值
2. 遍历链表，同时以 `1 / n` 的概率更新结点值，第一次更新时，由于 `n = 1`，`random.randrange(0, 1)` 恒小于 1，所以 `val` 一定会被更新
3. 结束链表遍历，返回结点值

### 复杂度

- 时间复杂度：O(N) 其中 N 为链表结点个数
- 空间复杂度：O(1) 无需额外空间
