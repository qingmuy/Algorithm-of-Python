# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        def demo(target:Optional[TreeNode]):
            if target:
                demo(target.left)
                result.append(target.val)
                demo(target.right)
        demo(root)
        return result
        # 以上为递归解法
        #非递归即为遍历：使用栈储存
        # temp = []
        # result = []
        # while root or temp:
        #     if root:
        #         temp.append(root)
        #         root = root.left
        #     else:
        #         temp1 = temp.pop()
        #         result.append(temp1.val)
        #         root = temp1.right
        # return result