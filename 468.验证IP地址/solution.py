# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/18 10:37
# filename    : solution.py
# description : LC 468 验证IP地址

import re


class Solution:
    # IPv4 包含五种情况
    # 如果只包含一位数字：[0-9]
    # 如果包含两位数字：[1-9][0-9]
    # Case 1 包含三位数字：1[0-9][0-9]
    # Case 2 包含三位数字：2[0-4][0-9]
    # Case 3 包含三位数字：25[0-5]
    pattern_ipv4 = re.compile(r'^({chunk}\.){{3}}{chunk}$'.format(chunk=r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'))
    # {1, 4} 匹配 1 到 4 次 [0-9a-fA-F]
    pattern_ipv6 = re.compile(r'^({chunk}\:){{7}}{chunk}$'.format(chunk=r'([0-9a-fA-F]{1,4})'))

    @staticmethod
    def safe_int(x, base=10, default=-1):
        try:
            return int(x, base)
        except ValueError:
            return default

    def validate_ipv4(self, IP: str) -> bool:
        """ 检查 ipv4 地址格式"""
        nums = IP.split('.')
        # 少于四组数字，不符合 ipv4 地址格式
        if len(nums) != 4:
            return False
        for num in nums:
            # 转换成十进制，转换失败返回 -1
            int_num = self.safe_int(num)
            # 如果不在 [0, 255] 范围内，或非零数字有前置 0，不符合 ipv4 格式
            if int_num > 255 or int_num < 0 or (len(num) > 1 and num.startswith('0')):
                return False
        return True

    def validate_ipv6(self, IP: str) -> bool:
        """ 检查 ipv6 地址格式 """
        nums = IP.split(':')
        # 少于八组数字，不符合 ipv6 地址格式
        if len(nums) != 8:
            return False
        for num in nums:
            # 转换成十进制，转换失败返回 -1
            int_num = self.safe_int(num, base=16)
            # 如果不在 [0, 65535] 范围内，或者超过四位，不符合 ipv6 格式
            if int_num < 0 or int_num > 65535 or len(num) > 4:
                return False
        return True

    def validIPAddress(self, IP: str) -> str:
        """ 分块判断 """
        if '.' in IP and self.validate_ipv4(IP):
            return 'IPv4'
        elif self.validate_ipv6(IP):
            return 'IPv6'
        return 'Neither'

    def validIPAddressRegexp(self, IP: str) -> str:
        """ 正则表达式，统一判断 """
        if '.' in IP and self.pattern_ipv4.match(IP):
            return 'IPv4'
        elif self.pattern_ipv6.match(IP):
            return 'IPv6'
        return 'Neither'
