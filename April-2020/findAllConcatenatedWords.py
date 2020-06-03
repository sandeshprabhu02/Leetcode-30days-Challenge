# Concatenate Words
# Video explanation at https://www.youtube.com/watch?v=QGVCnjXmrNg
# Get 100+ more coding videos at http://coderpro.com/

"""
472. Concatenated Words
Hard

571

90

Add to List

Share
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:

Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:

The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.

"""

class Solution(object):
  def findAllConcatenatedWords(self, words):
    wordDict = set(words)
    cache = {}
    return [word for word in words if self._canForm(word, wordDict, cache)]

  def _canForm(self, word, wordDict, cache):
    if word in cache:
      return cache[word]
    for index in range(1, len(word)):
      prefix = word[:index]
      suffix = word[index:]
      if prefix in wordDict:
        if suffix in wordDict or self._canForm(suffix, wordDict, cache):
          cache[word] = True
          return True
    cache[word] = False
    return False

input = ['cat', 'cats', 'dog', 'catsdog']
print(Solution().findAllConcatenatedWords(input))
# ['catsdog']
