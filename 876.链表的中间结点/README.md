# [876. 链表的中间结点](https://leetcode-cn.com/problems/middle-of-the-linked-list/solution/lian-biao-de-zhong-jian-jie-dian-by-leetcode-solut/)

`数组` `快慢指针`

## 数组

由于链表不能通过下标访问对应的元素，因此可以考虑对链表进行遍历，与此同此将结点依次放入数组中，那么对应的中间结点就是 `n // 2` 下标对应的数组元素

### 解题思路

1. 遍历链表，加入数组
2. 链表的中间结点就是数组下标 `n // 2` 对应的元素
    - 当 n 为奇数，`n // 2` 是中间结点
    - 当 n 为偶数，`n // 2` 是中间两个结点中靠右的元素

### 复杂度

- 时间复杂度：O(N) N 为链表的结点个数
- 空间复杂度：O(N) 数组所用的空间

## [快慢指针](https://leetcode-cn.com/problems/middle-of-the-linked-list/solution/kuai-man-zhi-zhen-zhu-yao-zai-yu-diao-shi-by-liwei/)

为了找出链表中的结点，考虑使用两个指针变量，初始时都位于链表的头结点，一个永远一次只走一步，另一个永远一次只走两部，当快指针走到链表尾部，慢指针正好位于链表的中间位置，这就是快慢指针法

### 解题思路

1. 创建慢指针 `slow` 和快指针 `fast`，同时指向链表的头结点
2. `slow` 指针每次只走一步，而 `fast` 指针每次只走两步
3. 当 `fast` 或 `fast.next` 到达链表尾部，循环结束，此时 `slow` 正好位于链表的中间结点
    - 当链表结点个数为奇数时，`slow` 位于正中间结点
    - 当链表结点个数为偶数时，`slow` 位于中间两个结点中的靠右那一个
    - 如果要让 `slow` 在循环结束时指向靠左的中间结点，那么应该让循环快一步结束，即快指针可以前进的条件改成 `while fast.next and fast.next.next`

### 复杂度

- 时间复杂度：O(N) N 为链表的结点个数
- 空间复杂度：O(1) 常数空间存放快慢指针
