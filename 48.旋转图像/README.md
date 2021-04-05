# [48. 旋转图像](https://leetcode-cn.com/problems/rotate-image/solution/xuan-zhuan-tu-xiang-by-leetcode-solution-vu3m/)

## 两次翻转

用翻转操作代替旋转操作，即通过水平翻转+主对角线翻转实现旋转操作

### 解题思路

以下面矩阵为例

|  5  |  1 |  9 |  11  |
| :---: | :---: | :---: | :---: |
|  2   |  4   |  8   |  10  |
|  13  |  3   |  6   |  7   |
|  15  |  14  |  12  |  16  |

1. 通过水平翻转 `matrix[i][j]` 与 `matrix[n - i - 1][j]` 交换元素，得到

   |  15  |  14  |  12  |  16  |
      | :---: | :---: | :---: | :---: |
   |  13  |  3   |  6   |  7   |
   |  2   |  4   |  8   |  10  |
   |  5   |  1   |  9   |  11  |

2. 通过主对角线翻转 `matrix[i][j]` 与 `matrix[j][i]` ，得到

   |  15  |  13  |  2   |  5   |
      | :---: | :---: | :---: | :---: |
   |  14  |  3   |  4   |  1   |
   |  12  |  6   |  8   |  9   |
   |  16  |  7   |  10  |  11  |

### 复杂度

- 时间复杂度：O(N^2) 枚举矩阵中一半的元素，进行交换操作
- 空间复杂度：O(1) 原地翻转

## 一次旋转

### 解题思路

根据旋转中关键规律，其中 i 代表行下标，j 代表列下标：

- `matrix[i][j]` 的新位置 `matrix[j][n - i - 1]`，使用 `temp` 临时变量暂存 `matrix[j][n - i - 1]`, 即 `temp = matrix[j][n - i - 1] matrix[j][n - i - 1] = matrix[i][j]`
- `matrix[j][n - i - 1]` 的新位置 `matrix[n - i - 1][n - j - 1]`，使用 `temp` 临时变量暂存 `matrix[n - i - 1][n - j - 1]`,
  即 `temp = matrix[n - i - 1][n - j - 1] matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1] matrix[j][n - i - 1] = matrix[i][j]`
- `matrix[n - i - 1][n - j - 1]` 的新位置 `matrix[n - j - 1][i]`，使用 `temp` 临时变量暂存 `matrix[n - j - 1][i]`,
  即 `temp = matrix[n - j - 1][i] matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1] matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1] matrix[j][n - i - 1] = matrix[i][j]`
- 最后，`matrix[n - j - 1][i]` 的新位置 `matrix[i][j]`，
  综上，`temp = matrix[i][j] matrix[i][j] = matrix[n - j - 1][i] matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1] matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1] matrix[j][n - i - 1] = matrix[i][j]`
- 注意 i 和 j 枚举的范围
    - 当 n 为偶数时，`0 < i < n / 2; 0 < j < n / 2`
    - 当 n 为奇数时，`0 < i < (n - 1) / 2; 0 < j < (n + 1) / 2`
    - 范围可以合并为 `0 < i < n / 2; 0 < j < (n + 1) / 2`

### 复杂度

- 时空复杂度与第一种方法一致
