# [102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/er-cha-shu-de-ceng-xu-bian-li-by-leetcode-solution/)

`BFS` `DFS`

## BFS 广度优先

广度优先遍历需要利用队列作为辅助数据结构来实现，根据先进先出的特性，完成二叉树的遍历

### 解题思路

1. 首先将根节点入队
2. 根节点出队，如果左右节点不为空，就将它们入队，完成第一次遍历后，队列中剩下根节点的子节点
3. 根节点的左子节点，重复步骤 2 的操作，将其子节点入队（从左往右）
4. 如何区分二叉树每一层？
    - 在每一层遍历前，先记录队列中节点数量（也就是这一层的节点数量），利用 `for` 循环，将它们全部出队，并将它们子节点全部入队

### 复杂度

- 时间复杂度：O(N) 遍历二叉树
- 空间复杂度：O(N) 保存节点值

## [DFS 深度优先](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/die-dai-di-gui-duo-tu-yan-shi-102er-cha-shu-de-cen/)

### 解题思路

1. 按照深度优先遍历的顺序（二叉树的前序遍历），首先访问左边所有节点
2. 每次递归都需要记录当前的层数 `level`，用于寻找节点值存放的层级，如果当前层是第一次记录，那么加入一个空的列表
3. 如何区分二叉树的每一层？
   - 递归过程中隐式维护栈，方便在节点各层之间跳转

### 复杂度

- 时间复杂度：O(N) 遍历二叉树
- 空间复杂度：O(N) = O(N) 保存节点值 + O(h) 递归调用栈的深度
