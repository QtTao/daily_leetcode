# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/6/14 16:32
# filename    : solution.py
# description : LC 912 排序数组


import random


class Solution:
    def partition(self, nums: List[int], low: int, high: int):
        """ 以 nums[random_index] 为主元，将数组分成两部分 """
        # 选取随机主元
        idx = random.randint(low, high)
        # 与下标 low 交换位置
        nums[idx], nums[low] = nums[low], nums[idx]
        pivot, j = nums[low], low
        for i in range(low + 1, high + 1):
            # 寻找小于等于 pivot 的元素，并记录它出现的最后一个位置
            if nums[i] <= pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]
        # 循环结束，下标 j 对应的是区间 [low, high] 中最后一个大于等于 pivot
        # 故将它与 pivot 对应的下标 low 交换位置
        nums[low], nums[j] = nums[j], nums[low]
        return j

    def quick_sort_between(self, nums: List[int], low: int, high: int):
        """ 分而治之 """
        # 当 high < low，上界小于下界，不成立，跳出递归
        if high < low:
            return None
        m = self.partition(nums, low, high)
        # 递归处理 m 的左半部分
        self.quick_sort_between(nums, low, m - 1)
        # 递归处理 m 的右半部分
        self.quick_sort_between(nums, m + 1, high)

    def sortArray(self, nums: List[int]) -> List[int]:
        """ 快速排序，原地排序 """
        self.quick_sort_between(nums, 0, len(nums) - 1)
        return nums

    def max_heapify(self, heap, root, heap_len):
        """ 将数组调整为大根堆 """
        p = root
        while p * 2 + 1 < heap_len:
            left, right = p * 2 + 1, p * 2 + 2
            if heap_len <= right or heap[right] < heap[left]:
                next = left
            else:
                next = right
            if heap[p] < heap[next]:
                heap[p], heap[next] = heap[next], heap[p]
                p = next
            else:
                break

    def build_head(self, heap):
        """ 建大根堆 """
        for i in range(len(heap) - 1, -1, -1):
            self.max_heapify(heap, i, len(heap))

    def heap_sort(self, nums):
        """ 堆排序实现方式 """
        # 首次建堆，堆顶元素为全局最大值
        self.build_head(nums)
        for i in range(len(nums) - 1, -1, -1):
            # 将堆顶元素与末尾元素交换
            nums[i], nums[0] = nums[0], nums[i]
            # 排除末尾元素，对剩下元素再次为大根堆
            self.max_heapify(nums, 0, i)

    def sortArrayHeapSort(self, nums: List[int]) -> List[int]:
        """ 堆排序 """
        self.heap_sort(nums)
        return nums

    def merge_sort(self, nums, left, right):
        """ 归并排序实现方式 """
        # 当数组中只有一个元素，不需要排序，直接返回
        if left == right:
            return None
        # 计算中间下标，将数组平均分成两部分
        mid = (left + right) // 2
        # 对左半部分进行归并排序
        self.merge_sort(nums, left, mid)
        # 对右半部分进行归并排序
        self.merge_sort(nums, mid + 1, right)
        # 线性合并两个有序的子序列
        tmp = []
        # 两个区间的起始下标
        i, j = left, mid + 1
        while i <= mid or j <= right:
            # 当 i 已越过左半部分或者右半部分元素 nums[j] 小于左半部分元素 nums[i]
            # 将 nums[j] 加入临时数组
            if i > mid or (j <= right and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            # 否则将 nums[i] 加入临时数组
            else:
                tmp.append(nums[i])
                i += 1
        # 覆盖原始数组
        nums[left:right + 1] = tmp

    def sortArrayMergeSort(self, nums: List[int]) -> List[int]:
        """ 归并排序 """
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums
