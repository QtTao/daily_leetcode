# [12. 整数转罗马数字](https://leetcode-cn.com/problems/integer-to-roman/solution/zheng-shu-zhuan-luo-ma-shu-zi-by-leetcod-75rs/)

## 数学

罗马数字的表示方法是唯一的规则是对于从左到右的每一位，选择尽可能大的符号值，为了表示一个给定的整数 num，从符号-数值对中寻找不超过 num 的最大符号值，将 num 减去该符号值，然后继续寻找，直到 num 为 0

### 解题思路

1. 初始化值 value 和符号 roman 的映射关系，注意字典应按值 value 从大到小进行排序
2. 遍历值和符号映射关系，初始化结果为 `ans = ''`
    - 若当前数值 value 不超过 num，则从 num 中不断减去 value，同时，将对应的符号跟此前的结果进行拼接，直至 num 小于 value
    - 然后遍历下一个值与符号映射对，完成字符串拼接，当 num 被减至 0，跳出循环，返回结果 `ans`

### 复杂度

- 时间复杂度：O(1) 由于数字和符号值对的长度都是固定，所以循环次数也是固定的
- 空间复杂度：O(1)
