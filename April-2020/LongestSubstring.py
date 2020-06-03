'''
	Given a string, find the length of the longest substring without repeating characters.

	Examples:

	Given "abcabcbb", the answer is "abc", which the length is 3.

	Given "bbbbb", the answer is "b", with the length of 1.

	Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapSet = {}
        startIndex, result = 0, 0
        for currentIndex in range(len(s)):
            if s[currentIndex] in mapSet:
                startIndex = max(mapSet[s[currentIndex]], startIndex)
            maxlen = currentIndex-startIndex+1
            result = max(result, maxlen)
            mapSet[s[currentIndex]] = currentIndex+1
        print(mapSet)
        return result
        
        


print(Solution().lengthOfLongestSubstring("ababcabcd"))