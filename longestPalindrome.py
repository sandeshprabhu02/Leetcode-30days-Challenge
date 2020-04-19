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
    def longestPalindrome(self, s: str) -> str:
        if self._isPalindrome(s):
            return s
        substr=['']
        length=0
        result=''
        for i in s:
            substr+=[i + sub for sub in substr]
        print('substr', substr)
        for item in substr:
            if self._isPalindrome(item):
                if len(item)>length:
                    result=item
                    length=len(item)
        return result

    def _isPalindrome(self, s):
        return s==s[::-1]


print(Solution().longestPalindrome("babad"))