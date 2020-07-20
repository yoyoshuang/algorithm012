# 最近公共祖先
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 如果根是空，返回空
        if root == None: return 
        # 如果根就是pq，返回pq
        if root ==p or root == q: return 
        # 分别递归左右
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 如果左右都没有返回空
        if left==None and right==None: return 
        # 如果左右都有，返回根
        if left!=None and right!=None: return root
        # 如果左没有，返回右
        if left == None: return right
        # 如果右没有，返回左
        if right ==None: return left
    
    