'''
Author: Muy lzqm04@gmail.com
Date: 2024-03-01 20:28:26
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2024-03-01 20:28:41
FilePath: \Code\Python\算法练习\LeetCode\路经总和.py
Description: 
    
Copyright (c) 2024 by Muy, All Rights Reserved. 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        else:
            if root.left and root.right:
                return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
            elif not root.left and not root.right and targetSum - root.val == 0:
                return True
            else:
                return self.hasPathSum(root.left, targetSum - root.val) if root.left else self.hasPathSum(root.right, targetSum - root.val)