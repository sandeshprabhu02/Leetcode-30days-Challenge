"""

Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks.

"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minVal = 0
        self.preVal = 0

    def push(self, x):
        if x < self.minVal:
            self.preVal = self.minVal
            self.minVal = x
        self.stack.append(x)
        
    def pop(self):
        if self.stack:
            top  = self.top()
            if top 
            return self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        return self.minVal


# [4, 2, 5, 6, 1, 2, 3]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Solution:

class MinStack1:

def __init__(self):
    self.stack = []

# @param x, an integer
# @return an integer
def push(self, x):
    curMin = self.getMin()
    if curMin == None or x < curMin:
        curMin = x
    self.stack.append((x, curMin))

# @return nothing
def pop(self):
    self.stack.pop()


# @return an integer
def top(self):
    if len(self.stack) == 0:
        return None
    else:
        return self.stack[len(self.stack) - 1][0]


# @return an integer
def getMin(self):
    if len(self.stack) == 0:
        return None
    else:
        return self.stack[len(self.stack) - 1][1]