# [121. 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/121-mai-mai-gu-piao-de-zui-jia-shi-ji-by-leetcode-/)

`DP`

## 遍历

### 解题思路

1. 遍历数组，每次记录当前最低价格，假设当天以`min_price`买入该股票
2. 每次比较当前最大收益`max_profit`与当日卖出的价格的收益`price - min_price`比较
3. 遍历结束后即可得到最大收益

### 复杂度

- 时间复杂度：O(N) 遍历一次数组
- 空间复杂度：O(1) 只使用常量空间

## 动态规划

### 解题思路

假设 `f(i)` 为第 i 天卖出股票获得的收益，那么题目要求的最大收益就是 `max(f(0), ..., f(n))`，若已知第 i - 1 天的收益是 `f(i - 1)`，那么 `f(i) = max(f(i - 1) + prices[i] - prices[i - 1], prices[i] - prices[i - 1])`
。这里可以解读为第 i 天收益是由第 i - 1 天的收益和价格波动组成的。根据题目的意思，f(i-1) 最小值为 0，所以状态转移方程可以改写成 `f(i) = max(f(i - 1), 0) + prices[i] - prices[i - 1]`

1. 初始化变量 profit，等同于上述假设的 `f(i)`
2. 遍历数组，计算每天卖出股票的收益，即 `profit = max(profit, 0) + prices[i] - price[i - 1]`
3. 跟当前最大收益比较，并更新

### 复杂度

- 时空复杂度与第一种方法一致
