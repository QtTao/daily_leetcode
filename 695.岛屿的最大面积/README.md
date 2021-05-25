# [695. 岛屿的最大面积](https://leetcode-cn.com/problems/max-area-of-island/solution/dao-yu-de-zui-da-mian-ji-by-leetcode-solution/)

`DFS`

## 深度优先搜索

深度优先搜索的思想是将岛屿中连通的所有陆地搜索出来，然后进行统计，最后取每一块连通形状面积的最大值

### 解题思路

### 复杂度

- 时间复杂度：O(M * N) 其中 M 和 N 分别是网格的行数和列数
- 空间复杂度：O(M * N) 递归的深度最大可能是整个网格的大小，为 M * N
