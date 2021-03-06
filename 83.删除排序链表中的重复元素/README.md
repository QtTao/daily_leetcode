# [83. 删除排序链表中的重复元素](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/solution/shan-chu-pai-xu-lian-biao-zhong-de-zhong-49v5/)

## 一次遍历

### 解题思路

1. 由于升序的特性，只需要比较前后两个节点值，即可完成删除重复元素的操作
2. 初始化两指针，分别指向链表中相邻的两个节点
3. 遍历链表，当相邻的节点值相同，则删除靠后的一个节点，当相邻的节点值不同，指针继续向前移动，直至遇到 None 节点

### 复杂度

- 时间复杂度：O(N) 遍历链表
- 空间复杂度：O(1) 保存相邻两个节点的
