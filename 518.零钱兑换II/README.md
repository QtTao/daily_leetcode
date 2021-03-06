# [518. 零钱兑换II](https://leetcode-cn.com/problems/coin-change-2/solution/ling-qian-dui-huan-ii-by-leetcode/)

`动态规划`

## [背包问题](https://leetcode-cn.com/problems/coin-change-2/solution/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-6kaze/)

- 01 背包问题
    - 最基本的背包问题就是 01 背包问题：一共有 N 件物品，第 i 件物品的重量为 w[i]，价值为 v[i]。在总重量不超过背包承载上限 W 的情况下，能够装入背包的最大价值是多少？
- 完全背包问题
    - 完全背包与 01 背包不同就是每种物品可以有无限多个：一共有 N 种物品，每种物品有无限多个，第 i 种物品的重量为 w[i]，价值为 v[i]。在总重量不超过背包承载上限 W 的情况下，能够装入背包的最大价值是多少？
- 背包问题的特征
    - 根据一个 target （直接给出或间接求出），target 可以是数字也可以是字符串，再给定一个数组 arrs，能否使用 arrs 种的元素做各种排列组合得到 target
- 通用解法
    - 如果是 01 背包，即数组中的元素不可重复使用，外循环遍历 arrs，内循环遍历 target，且内循环倒序
    - 完全背包分两种情况
        - 数组中的元素可重复使用且不考虑元素之间的顺序，arrs 放外循环（保证 arrs 按顺序），target 在内循环，且内循环正序
        - 组合问题需考虑元素之间的顺序，需将 target 放在外循环，将 arrs 放在内循环，且内循环正序

### 解题思路

1. 零钱兑换II 属于完全背包问题，即是否可以用 coins 硬币组合成金额 amount，且不考虑排列顺序的完全背包问题
2. 外循环选择遍历 coins，内循环为 amount，且内循环正序
3. 初始化 `dp[i] = 0 i ∈ [1, amount]` 表示总金额为 i 的硬币组合方法数，其中 `dp[0] = 1` 表示金额为 0 的只有不选择任何硬币这一种组合
4. 对于元素之和等于 `i - coin` 的每一个组合，在最后添加 coin 之后即可得到一个元素之和等于 i 的组合，因此在计算 `dp[i]`，应该计算所有 `dp[i - coin]` 之和
5. 如何保证 dp 在计算过程中不出现重复？这是因为在遍历 coins 得到 `dp[i - coin]` 都是不同组合，再加上 coin 本身就不同，所以得到组合数 dp 是不会重复的
6. 完成双层循环后，`dp[amount]` 就是凑成金额 amount 的所有硬币组合数

### 复杂度

- 时间复杂度：O(金额 * 硬币数)
- 空间复杂度：O(金额) 额外使用数组保存不同金额下的硬币组合数
