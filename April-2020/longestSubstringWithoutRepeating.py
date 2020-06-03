"""
3. Longest Substring Without Repeating Characters
Medium

8406

509

Add to List

Share
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
             
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, left, right = 0, 0, 0
        char = set()
        n=len(s)
        while left<n and right<n:
            if s[right] not in char:
                char.add(s[right])
                right += 1
                longest=max(longest, right-left)
            else:
                char.remove(s[left])
                left += 1
        return longest
        # counter = dict()
        # result = 0
        # left = 0
        # for right in range(len(s)):
        #     if s[right] not in counter:
        #         counter[s[right]] = 1
        #         result = max(result, right-left + 1)
        #     else:
        #         while s[left] != s[right]:
        #             counter.pop(s[left])
        #             left += 1
        #         left += 1
        # return result