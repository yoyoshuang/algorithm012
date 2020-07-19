# 142. 环形链表 II
# https://leetcode-cn.com/problems/linked-list-cycle-ii/
#给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 \
# 如果 pos 是 -1，则在该链表中没有环。
# 说明：不允许修改给定的链表。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visitied = set()
        node = head 
        while node!= None:
            if node in visitied:
                return node
            
            else:
                visitied.add(node)
                node = node.next
        return None