"""

Construct Binary Search Tree from Preorder Traversal
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insert(self, root, val):
        if val <= root.val:
            if root.left != None:
                self.insert(root.left, val)
            else:
                root.left = TreeNode(val)
        elif root.right != None:
            self.insert(root.right, val)
        else:
            root.right = TreeNode(val)
    
    def bstFromPreorder(self, preorder):
        root = TreeNode(preorder[0])
        
        for i in range(1, len(preorder)):
            self.insert(root, preorder[i])
            
        return root


    # def bstFromPreorder(self, preorder):
    #     root = TreeNode(preorder[0])
    #     stack = [root]
    #     for value in preorder[1:]:
    #         if value < stack[-1].val:
    #             stack[-1].left = TreeNode(value)
    #             stack.append(stack[-1].left)
    #         else:
    #             while stack and  value > stack[-1].val:
    #                 last = stack.pop()
    #             last.right = TreeNode(value)
    #             stack.append(last.right)
    #     return stack



print(Solution().bstFromPreorder([8,5,1,7,10,12]))
