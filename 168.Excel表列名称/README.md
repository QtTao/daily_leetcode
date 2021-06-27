# [168. Excel表列名称](https://leetcode-cn.com/problems/excel-sheet-column-title/solution/168-by-ikaruga/)

## 数学

### 解题思路

1. 迭代列下标 col_idx = columnNumber
2. 计算 `col_idx, remainder = divmod(col_idx, 26)`
   - 其中 col_idx 表示满 26 后的进位，remainder 表示 Excel 表列名称从后向前遍历的字母
   - 当 remainder 不等于 0，说明 col_idx 不能被 26 整除，那么直接将它转换成对应的字母即可 `chr(remainder + 26)`
   - 当 remainder 等于 0，说明 col_idx 可以被 26 整除，对应字母一定为 Z，同时将 col_idx 的满 26 后的进位减一
3. 循环计算 col_idx，直至 `col_idx = 0`，将得到的字母反转然后合并即可

### 复杂度

- 时间复杂度：O(1)
- 空间复杂度：O(1)
