# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        mn,mx,idx,cur,prev,previdx,fidx = 1e5+1, -1, 0, head, None, -1, None
        while cur.next:
            if  prev and (prev < cur.val > cur.next.val or prev > cur.val < cur.next.val):
                if  fidx:  mn,mx = min(mn, idx-previdx), idx-fidx
                else:      fidx  = idx
                previdx  = idx
            prev,cur,idx = cur.val, cur.next, idx+1
        return [mn if mn <= 1e5 else -1,mx]
        