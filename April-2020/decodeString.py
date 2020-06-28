"""

Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
s = "5[abab]2[n" return <Error> ??

"""

class Stack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
         self.stack.append(x)
        
    def pop(self):
        if self.stack:
            return self.stack.pop()
    
    def top(self):
        return stack[-1]


# def decodeString(s):
#     stack = Stack()
#     repeatNum = 0
#     temp = ""
#     mainStr =
#     for x in reversed(s):
#         if x.isdigit():
#             repeatNum = x
#             while stack.top == ']':
#                 temp += stack.pop()
            
#         else:
#             stack.push(x)




#         # if x == ']':
#         #     continue
#         # elif x.isalpha():
#         #     stack.push(x)
#         # elif x.isdigit():
#         #     while stack.top:

#         #     repeatNum = int(x)
#         # elif x == '[':
#         #     while stack:
#         #         temp += stack.pop()
#     return temp


def decodeString(s):
    stack = []; curNum = 0; curString = ''
    for c in s:
        if c == '[':
            stack.append(curString)
            stack.append(curNum)
            curString = ''
            curNum = 0
        elif c == ']':
            num = stack.pop()
            prevString = stack.pop()
            curString = prevString + num*curString
        elif c.isdigit():
            curNum = curNum*10 + int(c)
        else:
            curString += c
        print(stack)
    return curString



print(decodeString("3[a2[cbb]]"))