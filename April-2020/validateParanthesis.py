"""
Valid Parenthesis String
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:

Input: "()"
Output: True
Example 2:

Input: "(*)"
Output: True
Example 3:

Input: "(*))"
Output: True
Note:

The string size will be in the range [1, 100].

"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        left = list()
        star = list()
        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == '*':
                star.append(i)
            elif c == ')':
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else:
                raise ValueError("Invalid char found: %s" % c)
        if len(left) > len(star):
            return False
        while left and star:
            if left.pop() > star.pop():
                return False
        return True


print(Solution().checkValidString(')('))