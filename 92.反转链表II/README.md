# [92. 反转链表II](https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/fan-zhuan-lian-biao-ii-by-leetcode-solut-teyq/)

## 朴素解法

在 `left` 和 `right` 的部分使用反转链表的方法，另外需要记录 `left` 的前驱节点和 `right` 的后继节点，用于拼接反转后的链表

### 解题思路

1. 创建哑节点 `dummy`
2. 从哑节点出发前进 `left - 1` 步到达 `left` 的前驱节点 `pre_node`
3. 从 `pre_node` 出发前进 `right - left + 1` 步到达 `right` 节点
4. 截取待反转链表区域，注意切断前后节点关系
5. 使用递归或迭代法反转链表
6. 将反转链表与 `left` 的前驱节点和 `righ` 的后继节点连接起来

### 复杂度

- 时间复杂度：O(N) 遍历链表，最坏的情况需要遍历两次，一次用于寻找 `left` 和 `right`，另一次用于反转
- 空间复杂度：O(1)

## 头插法

在遍历链表的过程不断将新节点移动到反转部分的起始位置

### 解题思路

1. 创建哑节点 `dummy`
2. 从哑节点出发前进 `left - 1` 步到达 `left` 的前驱节点 `pre_node`，并将 `left` 节点定义为 `cur_node`
3. 将 `cur_node` 的后继节点 `next_node` 移动到第一个要反转节点的前面（即头插法），这里注意记录 `next_node` 的后继节点
4. 经过一次头插法操作后，`cur_node` 变相前进一步，而 `pre_node` 的后继节点变成了 `next_node`，继续步骤 3 的操作，由于待反转链表节点数为 `right - left + 1`，所以只需 `right - left` 次头插操作即可完成局部链表反转

### 关键变量注释

- `cur_node` 指向待反转区域的第一个节点 `left`，这个节点会随着头插不断往前移动
- `next_node` 永远指向 `cur_node` 的后继节点，随着 `cur_node` 的变化而变化
- `pre_node` 永远指向待反转区域的第一个节点 `left` 的前驱节点，操作过程位置不变

### 复杂度

- 时间复杂度：O(N) 一次遍历
- 空间复杂度：O(1)
