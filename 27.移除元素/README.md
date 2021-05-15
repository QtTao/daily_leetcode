# [27. 移除元素](https://leetcode-cn.com/problems/remove-element/solution/yi-chu-yuan-su-by-leetcode-solution-svxi/)

`双指针`

## 双指针

利用数组头尾双指针，在双指针往中间移动的过程中将指定的元素进行替换，最终达到移除元素的效果

### 解题思路

1. 初始化指针 `left` 和 `right` 分别指向数组头尾，向中间移动
2. 当 `left` 指针指向的元素等于 val，将 `right` 指针指向的元素赋值到 `left` 指针的位置，然后 `right` 指针左移一位
3. 如果步骤 2 赋值的结果依然等于 val，重新赋值操作，`right` 指针再次左移一次，直至 `left` 指针指向的元素的值不等于 val 为止
4. 当 `left` 指针指向元素不等于 val，`left` 指针右移一位
5. 当 `left` 指针越过 `right` 指针时，数组遍历完成结束循环，此时 `left` 指针下标值就是移除元素后的数组长度

### 复杂度

- 时间复杂度：O(N) N 为数组长度
- 空间复杂度：O(1) 常数空间
