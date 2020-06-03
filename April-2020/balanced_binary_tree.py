"""

Balanced Binary Tree
Easy

1900

150

Add to List

Share
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postOrder(self, node):
        if node is None:
            return 0
        
        left = self.postOrder(node.left)
        right = self.postOrder(node.right)
        
        #check if leaf is empty <or> value of left node is > right node (for balanced tree)
        if (left == -1) or (right == -1) or abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1
        
        
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return True if self.postOrder(root) > 0 else False
    



if __name__ == '__main__':
    root = TreeNode(1)  
    root.left = TreeNode(2)  
    root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)


print(Solution().isBalanced(root))