# [101. 对称二叉树](https://leetcode-cn.com/problems/symmetric-tree/solution/dui-cheng-er-cha-shu-by-leetcode-solution/)

`DFS` `BFS`

## 深度优先搜索

对称的二叉树与 [100.相同的树](https://leetcode-cn.com/problems/same-tree/solution/xiang-tong-de-shu-by-leetcode-solution/) 不同点在于**右子树都与左子树镜像对称**

### 解题思路

1. 首先判断左右子树头结点是否相同
    - 如果都为空，对称
    - 如果其中一个为空，另一个为非空，非对称
    - 如果都为非空，但值不同，非对称
2. 如果左右子树头结点都为非空，且值相同，递归遍历二叉，比较
    - 左结点的左子结点与右结点的右子结点是否对称
    - 左结点的右子结点与右结点的左子结点是否对称

### 复杂度

- 时间复杂度：O(N) N 为二叉树的结点数
- 空间复杂度：O(N) 递归调用栈深度不超过 N

## 广度优先搜索

### 解题思路

### 复杂度

- 时间复杂度：
- 空间复杂度：
