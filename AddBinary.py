#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"


Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

"""

class Solution:
    def addBinary(self, x, y):
        max_len = max(len(x), len(y))

        x = x.zfill(max_len)
        y = y.zfill(max_len)
        
        print(x)
        print(y)
        
        result = ''
        carry = 0

        for i in range(max_len-1, -1, -1):
            val = carry
            val += 1 if x[i] == '1' else 0
            val += 1 if y[i] == '1' else 0
            result = ('1' if val % 2 == 1 else '0') + result
            carry = 0 if val < 2 else 1
            print(result)
            print(carry)
            print('***')
            

        if carry !=0 : result = '1' + result

        return result.zfill(max_len)


print(Solution().addBinary("101", "1011"))