# [415. 字符串相加](https://leetcode-cn.com/problems/add-strings/solution/zi-fu-chuan-xiang-jia-by-leetcode-solution/)

## [字符串遍历](https://leetcode-cn.com/problems/add-strings/solution/add-strings-shuang-zhi-zhen-fa-by-jyd/)

### 解题思路

1. 初始化 i，j 两指针分别指向 num1 和 num2 数组的尾部，模拟竖式加法的过程，进位 `carry = 0`
2. 遍历字符串，当 i 或 j 在数组内部
    - 判断指针 i 是否溢出，当 `i >= 0`，num1 的当前位为 `int(num1[i])`，否则为 0
    - 判断指针 j 是否溢出，当 `j >= 0`，num1 的当前位为 `int(num2[j])`，否则为 0
    - 计算当前位，`num = n1 + n2 + carry`，并将余数 `num % 10` 添加到 ans 的头部
    - 计算进位，`carry = num // 10`，代表当前位相加是否有进位
    - 当 num1 且 num2 遍历完，跳出循环，并根据 carry 值决定是否在头部添加进位 1，最终返回 ans 即可

### 复杂度

- 时间复杂度：O(max(M, N)) 其中 M，N 是两个数组的长度
- 空间复杂度：O(1)
