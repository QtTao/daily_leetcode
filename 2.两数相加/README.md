# [2. 两数相加](https://leetcode-cn.com/problems/add-two-numbers/solution/liang-shu-xiang-jia-by-leetcode-solution/)

## 链表遍历

由于输入的两个链表都是逆序存储数字的位数的，因此两个链表中同一位置的数字可以直接相加

### 解题思路

1. 同时遍历两个链表，逐位计算它们的和，并与当前位置的进位相加
   - 当两个链表的结点同时存在，那么它们的和就是 `l1.val + l2.val + carry`
   - 当只有其中一个链表的结点存在，那么两数之和就是 `l1.val + carry` 或者 `l2.val + carry`
   - 当两个链表的结点都为空，结束遍历
2. 如果链表遍历结束后，且进位大于 0，还需要链表后面添加一个结点，其中结点的值为 `carry`

### 复杂度

- 时间复杂度：O(max(M, N)) 其中 M 和 N 分别为两个链表的结点数
- 空间复杂度：O(1)
