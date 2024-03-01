'''
Author: Muy lzqm04@gmail.com
Date: 2024-02-29 11:04:27
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2024-02-29 11:04:47
FilePath: \Code\Python\算法练习\LeetCode\二叉树最大深度.py
Description: 
描述
Copyright (c) 2024 by Muy, All Rights Reserved. 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Judge(self, root) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left and root.right:
            return max(1 + self.Judge(root.left),1 + self.Judge(root.right))
        if root.left or root.right:
            return max((1 + self.Judge(root.left)),(1 + self.Judge(root.right)))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.Judge(root)