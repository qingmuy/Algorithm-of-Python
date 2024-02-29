'''
Author: Muy lzqm04@gmail.com
Date: 2024-02-29 10:09:41
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2024-02-29 10:10:08
FilePath: \Coded:\Note\Algorithm-of-Python\Code\对称二叉树.py
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        def judge(rootleft:Optional[TreeNode],rootright:Optional[TreeNode]) -> bool:
            if not rootleft and not rootright:
                return True
            if not rootleft or not rootright:
                return False
            if rootleft.val != rootright.val:
                return False
            else:
                return judge(rootleft.left,rootright.right) and judge(rootleft.right,rootright.left)
            return True
        return judge(root.left,root.right)
    
# 改进
class Solution:
    def judge(self,rootleft:Optional[TreeNode],rootright:Optional[TreeNode]) -> bool:
            if not rootleft and not rootright:
                return True
            if not rootleft or not rootright:
                return False
            if rootleft.val != rootright.val:
                return False
            else:
                return self.judge(rootleft.left,rootright.right) and self.judge(rootleft.right,rootright.left)
            return True
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.judge(root.left,root.right)