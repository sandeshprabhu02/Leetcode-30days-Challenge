"""
Diameter of Binary Tree
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 

          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        def depth(node):
            if not node:
                return 0, 0 # height, diameter
            left_depth, left_diameter = depth(node.left)
            right_depth, right_diameter = depth(node.right)
            print(node.val)
            print(left_depth, left_diameter)
            print(right_depth, right_diameter)
            print('depth', max(left_depth + 1, right_depth + 1), max(left_diameter, right_diameter, left_depth + right_depth))
            print('------------')
            return max(left_depth + 1, right_depth + 1), max(left_diameter, right_diameter, left_depth + right_depth)
        
        _, diameter = depth(root)
        return diameter
        
    


if __name__ == '__main__': 
    root = TreeNode(1)  
    root.left = TreeNode(2)  
    root.right = TreeNode(3)  
    root.left.left = TreeNode(4)  
    root.left.right = TreeNode(5)  
    
    print(Solution().diameterOfBinaryTree(root))