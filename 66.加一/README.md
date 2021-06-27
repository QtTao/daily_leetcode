# [66. 加一](https://leetcode-cn.com/problems/plus-one/solution/java-shu-xue-jie-ti-by-yhhzw/)

## 数学

### 解题思路

1. 首先对数组末尾数字加一
2. 从后向前遍历数组，进行进位操作
   - 首先加上进位得到每个元素的结果 `num`
   - 计算个位数和对应进位，`digit = num % 10` `carry = num // 10`
    - 原地修改数组
3. 如果数组遍历完后还有进位，直接在数组前加一

### 复杂度

- 时间复杂度：O(N) N 为数组长度
- 空间复杂度：O(1) 原地修改数组无需额外空间
