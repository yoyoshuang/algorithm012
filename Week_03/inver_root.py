# 226. 翻转二叉树
# https://leetcode-cn.com/problems/invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        orgroot = root
        def do_invert(root):
            if root== None:
                return
            tmp = root.left
            root.left = root.right
            root.right = tmp
    
            do_invert(root.left)
            do_invert(root.right)

        do_invert(orgroot)
        return orgroot