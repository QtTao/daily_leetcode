# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/3/25 06:55
# filename    : solution.py
# description : LC 215 数组中的第K个最大元素

import random


class Solution:
    def partition(self, nums, low, high):
        """ 根据 pivot 将数组划分成左右两部分 """
        i = low - 1
        pivot = nums[high]
        for j in range(low, high):
            # 当前元素 <= pivot
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def quickselect(self, nums, left, right, idx):
        """ 加入随机选择算法的快速排序 """
        # 随机选择索引，并以此作为 pivot 来划分数组，加速搜索
        rand_idx = random.randint(left, right)
        nums[rand_idx], nums[right] = nums[right], nums[rand_idx]
        part_idx = self.partition(nums, left, right)
        if idx == part_idx:
            return nums[idx]
        # 数组划分后，pivot 下标在 k 之前，说明 k 在右半部分
        elif part_idx < idx:
            return self.quickselect(nums, part_idx + 1, right, idx)
        # pivot 下标在 k 之后，说明 k 在左半部分
        else:
            return self.quickselect(nums, left, part_idx - 1, idx)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """ 快速排序 """
        # 由于 partition 方法会将数组分为两部分，左半部分较小，右半部分较大
        # 所以传入 index 应为 n - k
        return self.quickselect(nums, 0, len(nums) - 1, len(nums) - k)

    def findKthLargestWithContainer(self, nums: List[int], k: int) -> int:
        """ 局部淘汰法 """
        # 创建容器
        k_nums = nums[0:k]
        for i in range(k, len(nums)):
            # 寻找容器中最小值以及索引
            min_idx, min_num = 0, k_nums[0]
            for j, num in enumerate(k_nums):
                if min_num > num:
                    min_idx, min_num = j, num
            # 如果容器外的数字大于容器中最小值，执行替换操作
            if k_nums[min_idx] < nums[i]:
                k_nums[min_idx] = nums[i]
        return min(k_nums)

    def minheapify(self, nums, n, i):
        """
        创建最小堆
        nums[i] < nums[2 * i + 1]
        nums[i] < nums[2 * i + 2]
        """
        smallest = i
        # 左右节点下标
        left, right = 2 * i + 1, 2 * i + 2
        # 若左节点更小，更新最小值下标
        if left < n and nums[i] > nums[left]:
            smallest = left
        # 若右节点更小，更新最小值下标
        if right < n and nums[smallest] > nums[right]:
            smallest = right
        # 若最小值下标更新，交换值位置
        if smallest != i:
            nums[i], nums[smallest] = nums[smallest], nums[i]
            # 递归遍历，直至 i 为整个堆最小值下标
            self.minheapify(nums, n, smallest)

    def findKthLargestWithHeap(self, nums: List[int], k: int) -> int:
        """ 最小堆 """
        k_heap = nums[0:k]
        # 建堆
        for i in range(k // 2, -1, -1):
            self.minheapify(k_heap, k, i)

        # 逐步替换堆顶元素
        for num in nums[k:]:
            if k_heap[0] < num:
                # 替换堆顶元素
                k_heap[0] = num
                # 经过一次堆调整使得堆顶元素为最小值
                self.minheapify(k_heap, k, 0)
        return k_heap[0]
