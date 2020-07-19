# N叉树的层次遍历
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if root == None:
            return []
        outs = []
        this_level = [root]
        next_nodes = []
        this_vals = []
        
        while this_level :
            next_nodes = [] # 保存下一个层次的所有儿子节点
            tmp = [] # 保存当前层次的值
            for n in this_level: # 遍历当前层次所有节点
                tmp.append(n.val)
                for child in n.children:
                    if child!=None:
                        next_nodes.append(child)
            outs.append(tmp) # 结果加到输出列表中
            this_level = next_nodes # 当前层次遍历完成，进入下一个层次
            
        return  outs