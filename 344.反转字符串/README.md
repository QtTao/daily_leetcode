# [344. 反转字符串](https://leetcode-cn.com/problems/reverse-string/solution/fan-zhuan-zi-fu-chuan-by-leetcode-solution/)

`双指针`

## 双指针

利用指向字符串首尾的双指针，进行元素交换的操作，达到反转字符串的效果

### 解题思路

1. 初始化双指针 `left` 和 `right`，分别指向字符串的首尾，向中间移动，对数组进行遍历
2. 当 `left < right`
    - 交换 `s[left]` 和 `s[right]`
    - `left` 指针右移一位
    - `right` 指针左移一位
3. 当 `left >= right`，字符串遍历完成

### 复杂度

- 时间复杂度：O(N) N 为字符个数，一共执行了 N/2 次交换操作
- 空间复杂度：O(1)
