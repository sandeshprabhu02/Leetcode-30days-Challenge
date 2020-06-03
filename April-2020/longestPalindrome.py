"""
Longest Palindromic Substring
Medium

6004

487

Add to List

Share
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

"""

class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     if self._isPalindrome(s):
    #         return s
    #     substr=['']
    #     length=0
    #     result=''
    #     for i in s:
    #         substr+=[i + sub for sub in substr]
    #     print('substr', substr)
    #     for item in substr:
    #         if self._isPalindrome(item):
    #             if len(item)>length:
    #                 result=item
    #                 length=len(item)
    #     return result

    # def _isPalindrome(self, s):
    #     return s==s[::-1]


    def __init__(self):
        self.res_len=0
        self.res=''
    
    def longestPalindrome(self, s):
        s_len =  len(s)
        for i in range(s_len):
            self.helper(s, s_len, i, i)
            self.helper(s, s_len, i, i+1)
        return self.res
    

    def helper(self, s, s_len, left, right):
        while left>-1 and right<s_len and s[left]==s[right]:
            left, right = left-1, right+1
        current_pal = s[left+1:right]
        if len(current_pal) > self.res_len:
            self.res, self.res_len = current_pal, len(current_pal)

    


print(Solution().longestPalindrome("abcda"))
print('------------------')
print(Solution().longestPalindrome("cbbd"))